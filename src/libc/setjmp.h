#ifndef SETJMP
#define SETJMP
typedef struct __jmp_buf {
    int value;
    int point;
} jmp_buf;
jmp_buf _get_setjmp();
void longjmp(jmp_buf env, int val);
#define setjmp(a) (a=_get_setjmp()).value
#endif