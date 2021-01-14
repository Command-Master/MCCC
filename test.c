
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
    exit();
    int i = 0;
    for (i = 0; i < 10; i++) {
        int_print(i);
        if (i == 5) break;
        int_print(calloc(i, 10));
    }
}
