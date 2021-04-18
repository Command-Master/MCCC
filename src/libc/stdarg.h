#ifndef STDARG
#define STDARG
typedef void* va_list;
#define va_start(list, arg) ((list)=(&arg+1))
#define va_arg(list, type) ((list+=sizeof(type)),(*(type*)(list-sizeof(type))))
#define va_copy(dst, src) ((dst) = (src))
#define va_end(list)
#endif