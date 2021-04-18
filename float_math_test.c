#include <stdio.h>
//#define float_print(x) printf("%f\n", x)


int main() {
//    float a = (((2.0/3.96)*(9.64/5.62))/((9.68*6.87)*(7.78*1.62)));
//    float_print( a );
//    puts("expected 0.0010335912454337171 ");
//    float d = (((5.84/7.38)*(2.28/4.33))-((4.91/1.27)*(7.36+3.72)));
//    float_print( d );
//    puts("expected -42.42016964490716 ");
//    float g = (((3.25*2.05)+(7.62*2.5))+((5.66+0.63)-(6.66*9.67)));
//    float_print( g );
//    puts("expected -32.39970000000001 ");
//    float j = (((3.25/1.4)/(0.47*9.79))/(3.89+(5.51*5.23)));
//    float_print( j );
//    puts("expected 0.015425174335384179 ");
//    float m = (((6.14/0.46)/1.13)*((2.21/3.52)-(0.43*1.4)));
//    float_print( m );
//    puts("expected 0.305238903074609 ");
//    float p = (3.31-(4.97*(2.22/5.09)));
//    float_print( p );
//    puts("expected 1.142337917485265 ");
//    float s = (((9.55+0.58)*(8.63*3.52))/((9.79/3.59)*(4.66-3.93)));
//    float_print( s );
//    puts("expected 154.57946547637377 ");
//    float v = (((2.3/4.1)*(1.69*1.98))+((7.16/6.97)/9.18));
//    float_print( v );
//    puts("expected 1.9890385117668943 ");
//    float y = (((2.4-4.77)*(8.93/4.01))*((2.89-6.02)+(3.52/1.75)));
//    float_print( y );
//    puts("expected 5.903630317064477 ");
    int i;
    int mul = 1;
    float ans = 0;
    for (i = 1; i <= 10; i++) {
        ans += 1.0/mul;
        mul *= i;
    }
    float_print(ans);
}