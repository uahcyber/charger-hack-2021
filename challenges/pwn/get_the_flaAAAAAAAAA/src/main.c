#include <stdio.h>
#include <stdlib.h>

void setup() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

void hax() {
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

void vuln() {
    char buffer[32];
    printf("Hi! How are you today?: ");
    gets(buffer);
}

int main(int argc, char* argv[]) {
    setup();
    vuln();
    return 0;
}