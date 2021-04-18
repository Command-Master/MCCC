#ifndef STDIO
#define STDIO
#include <stdarg.h>
typedef char FILE;

FILE* stdin = 0;
FILE* stdout = 1;
FILE* stderr = 1;
#define EOF (-1)

void float_print(float);
void int_print(int);
void putc(char, FILE*);
void putchar(char);
void puts(char*);
char getc();
int printf(char*, ...);

#endif