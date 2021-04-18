#include <stdio.h>

int main () {
   int a = 10;
   puts("Start");
   while (a < 20) {
      if( a == 15) {
         a++;
         goto label;
      }
      int_print(a);
      a++;
   };
   label:
   int_print(a);
   puts("End");
}