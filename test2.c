#include <stdio.h>

int a(int b, int c) {
    return b+c;
}

int main() {
    int (*b)(int,int) = a;
    int c = 7;
    printf("%d", b(c, 7));
}