#include <stdarg.h>
#include <stdio.h>
int sum(int, ...);
int main() {
   puts("10 + 20 + 30");
   int_print(sum(3, 10, 20, 30));
   puts("4 + 20 + 25 + 30");
   int_print(sum(4, 4, 20, 25, 30));
}
int sum(int n, ...) {
   int s = 0;
   va_list l;
   int i;
   va_start(l, n);
   for(i = 0; i < n; i++) {
      s += va_arg(l, int);
   }
   va_end(l);
   return s;
}