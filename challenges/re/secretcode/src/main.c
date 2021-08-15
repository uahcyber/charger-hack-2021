// correct input is UAH{h4rdc0d3d_PaSsw0rd5_aRe_n0T_th3_m0v}

#include <stdio.h>
#include <unistd.h>
#include <string.h>

int VERIFICATION_PASSWORD[] = {143, 120, 128, 112, 94, 41, 98, 
                                87, 85, 65, 140, 64, 138, 86, 92, 
                                138, 93, 118, 115, 55, 120, 137, 
                                57, 96, 131, 111, 125, 100, 116, 
                                77, 112, 104, 142, 129, 71, 108, 
                                123, 69, 134, 142};

int verify_password(char* password) {
    if (strlen(password) != sizeof(VERIFICATION_PASSWORD)/4) {
        return -1;
    }
    for (int i = 0; i < strlen(password); i++) {
        if (VERIFICATION_PASSWORD[i]-18 != (password[i]^(strlen(password)-i))) {
            return -1;
        }
    }
    return 0;
}

int main(int argc, char* argv[]) {
    printf("Give me password: ");
    fflush(stdout);
    char input[41] = {0};
    read(STDIN_FILENO,&input,40);
    int result = verify_password(input);
    if (result != 0) {
        printf("Wrong password! Get off my computer!!!!!\n");
        return -1;
    }
    printf("Access granted :)\n");
    return 0;
}