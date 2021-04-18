//#include <stdio.h>
#define EOF (-1)

char line[1024];
int main() {
    while (1) {
        char* c = line;
        while (((*c)=getc(stdin)) != '\n' && *(c++) != (char)EOF);
        if (*(c-1) == EOF) exit(0);
        *c = 0;
        puts(line);
    }
}