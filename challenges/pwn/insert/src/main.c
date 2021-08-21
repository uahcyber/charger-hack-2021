#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define AUTHOR "Blue"

void giveFlag() {
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
    unsigned long addr = 0;
    unsigned long data = 0;
    printf("%s's data modifier\n=====================\n\n",AUTHOR);
    printf("%s (%p) is the best coder!\n", AUTHOR, &AUTHOR);
    printf("Where?: ");
    fflush(stdout);
    scanf("%lx",&addr);
    printf("What?: ");
    fflush(stdout);
    scanf("%lx",&data);
    *((volatile unsigned long*) addr) = data;
    return 0;
}