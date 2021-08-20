#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <unistd.h>


char* readFlag() {
    FILE* fp = fopen("flag.txt","r");
    if(!fp) {
        printf("Error opening flag file!\n");
        return NULL;
    }
    fseek(fp,0,SEEK_END);
    long len = ftell(fp);
    fseek(fp,0,SEEK_SET);
    char* buf = (char*)malloc(len+1);
    if(!buf) {
        printf("Error allocating 0x%lx bytes for reading\n",len);
        fclose(fp);
        return NULL;
    }
    fread(buf,len,1,fp);
    fclose(fp);
    return buf;
}


int main(int argc, char* argv[]) {
    char* flag = readFlag();
    char name[33];
    printf("Welcome to Blue's Greeter!\n==========================\nIf you are the attacker, it is okay! I'm totally over it.\n\n");
    printf("What is your name?: ");
    fflush(stdout);
    scanf("%32s",&name);
    printf("Hello, I'm glad you're here, ");
    printf(name);
    free(flag);
    return 0;
}