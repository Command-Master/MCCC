// uncomment this if you want to compile
//#include <stdio.h>
//#define int_print(x) printf("%d\n", (x))



#define EOF -1
#define bool int
#define pop() (*(--sp))
#define push(x) ((*(sp++)) = (x))
#define isspace(x) ((x)==' ')
#define isnum(x) (((x)>='0')&&((x)<='9'))
#define is_operator(c)  ((c) == '+' || (c) == '*' || (c) == '/' || (c) == '-')

typedef struct calculation {
    int size;
    double value;
} calc;

int get_precedence(char op) {
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return -1;
}


calc reverse_prefix(char* p) {
    int size = 0;
    while (isspace(*p)) {
        p--;
        size++;
    }
    if (is_operator(*p)) { // assuming 2ary operator
        calc s1 = reverse_prefix(p-1);
        calc s2 = reverse_prefix(p-s1.size-1);
        calc res;
        res.size = s1.size + s2.size + size + 1;
        if (*p == '+') {
            res.value = s1.value + s2.value;
        }
        else if (*p == '-') {
            res.value = s1.value - s2.value;
        }
        else if (*p == '*') {
            res.value = s1.value * s2.value;
        }
        else if (*p == '/') {
            res.value = s1.value / s2.value;
        }
        else res.value = -1;
        return res;
    } else {
        calc res;
        res.value = 0;
        while (isnum(*p)) {
            res.value *= 10;
            res.value += *p - '0';
            size++;
            p--;
        }
        res.size = size;
        return res;
    }
}


int main() {
    char equation[256];
    char x;
    char* p = equation;
    int i = 0;
    while((x = getc(stdin)) != EOF) {
        *(p++) = x;
        i++;
    }
    char stack[256];
    char* sp = stack;
    *(sp++) = ')';
    char prefix[256];
    char* pp = prefix;
    while (p--, i--) {
        int thing = 1;
        if (*p == ')') {
            push(')');
        }
        else if (*p == '(') {
            int x;
            while ((x=pop()) != ')') {
                *(pp++) = x;
            }
        }
        else if (is_operator(*p)) {
            char thing;
            while (get_precedence(thing = pop()) >= get_precedence(*p)) {
                *(pp++) = thing;
            }
            push(thing);
            push(*p);
        } else {
            *(pp++) = *p;
            thing = 0;
        }
        if (thing) {
            *(pp++) = ' ';
        }
    }
    *pp = 0;
    int thing;
    while ((thing = pop()) != ')') {
        *(pp++) = thing;
    }
    *pp = 0;
    pp--;
    calc answer = reverse_prefix(pp);
    float_print(answer.value);
}