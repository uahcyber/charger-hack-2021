#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define PASSWORD "z3R0-c00!B1U3"

void printFlag() {
    FILE* fp = fopen("flag.txt","r");
    if(!fp) {
        printf("Error opening flag file!\n");
        return;
    }
    fseek(fp,0,SEEK_END);
    long len = ftell(fp);
    fseek(fp,0,SEEK_SET);
    char* buf = (char*)malloc(len+1);
    if(!buf) {
        printf("Error allocating 0x%lx bytes for reading\n",len);
        fclose(fp);
        return;
    }
    fread(buf,len,1,fp);
    fclose(fp);
    puts(buf);
    fflush(stdout);
    free(buf);
}

int main(int argc, char* argv[]) {
    char user_input[33] = {0};
    printf("Enter the password: ");
    fflush(stdout);
    scanf("%32s",&user_input);
    if(strncmp(user_input,PASSWORD,strlen(user_input)) == 0) {
        printFlag();
    } else {
        printf("Incorrect password! Stop trying to hack me !!!\n");
    }
    return 0;
}