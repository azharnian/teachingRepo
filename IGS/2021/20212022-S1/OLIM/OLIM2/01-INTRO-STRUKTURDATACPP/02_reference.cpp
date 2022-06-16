#include <cstdio>

int main(){
	int a = 10; // integer

	int &b = a;

	printf(" Nilai dari a = %d\n", a);
	printf(" Nilai dari b = %d\n\n", b);

	printf("Alamat dari a = %p\n", &a);
	printf("Alamat dari b = %p\n\n", &b);


	b = 20; // integer
	printf(" Nilai dari a = %d\n", a);
	printf(" Nilai dari b = %d\n\n", b);
}