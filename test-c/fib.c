//#include <stdio.h>
//#define int_print(x) printf("%d\n", x);

int fib(int x);
void dec(int* x);
int main() {
    puts("fib:");
    int_print(fib(10));
}

int fib(int x) {
    if (x < 2) return x;
    dec(&x);
    int a = fib(x);
    dec(&x);
    int b = fib(x);
    return a + b;
}

void dec(int* x) {
    *x = *x - 1;
}