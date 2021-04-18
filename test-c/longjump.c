#include <stdio.h>
#include <setjmp.h>
int main() {
    int i;
    jmp_buf a;
    if (setjmp(a)) {
        puts("jumped");
        return 0;
    }
    puts("first");
    longjmp(a, 1);
    puts("unreachable");
}