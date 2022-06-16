#include <cstdio>
//#include <cstddef>

int main(){
	size_t size_c = sizeof(char);
	printf("char: %zd\n", size_c); //%zx

	size_t size_s = sizeof(short);
	printf("short: %zd\n", size_s);

	size_t size_i = sizeof(int);
	printf("int: %zd\n", size_i);

	size_t size_l = sizeof(long);
	printf("long: %zd\n", size_l);

	size_t size_f = sizeof(float);
	printf("float: %zd\n", size_f);

	size_t size_T = sizeof(size_t);
	printf("size_t: %zd\n", size_T);
}