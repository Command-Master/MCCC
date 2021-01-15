#define EOF (-1)

int c;
int main() {
    if (1) {
        int a = 3;
        int* b = &a;
        int* d = &c;
        c = 3;
        a = 5;
        int_print(*d);
        int_print(*b);
        *b = 12;
        *d = 102;
        int_print(a);
        int_print(c);
    }
    while (0 != 0) {
        puts("hi!");
    }
    char equation[256];
    char x;
    char* p = equation;
    int i = 0;
    while((x = getc(stdin)) != EOF) {
        *(p++) = x;
        i++;
    }
    puts(equation);
    int i = 1;
    int_print(i++); // 1
    int_print(++i); // 3
    int_print(i--); // 3
    int_print(--i); // 1
    exit();
    int i = 0;
    for (i = 0; i < 10; i++) {
        int_print(i);
        if (i == 5) break;
        int_print(calloc(i, 10));
    }
}
