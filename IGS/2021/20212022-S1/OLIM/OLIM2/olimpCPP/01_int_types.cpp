#include <cstdio>

int main(){
	//short , unsigned short(1 bit tdk digunakan untuk tanda) (2 bytes) %hd, %hu
	//int , unsigned int (4 bytes) %d, %u
	//long , unsigned long (Win 4 bytes, Linux/Mac 8 bytes), %ld. %lu
	//long long, unsigned long long (8 bytes), %lld, %llu

	//literal value -> decimal (0-9), binary(0&1) prefix : 0b, octal(0,7) prefix : 0, hexadecimal(0,f) prefix 0x

	unsigned short a = 0b10101010;
	printf("%hu\n\n", a);

	int b = 0123;
	printf("%d\n\n", b);

	unsigned long long d = 0xfffffffffffff;
	printf("%llu\n", d);
}