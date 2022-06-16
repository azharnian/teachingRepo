#include <cstdio>

int b;

int main(){
	int a = 5; //integer
	int b = 6; // integer
	//scanf("%d", &b);

	printf(" Nilai dari a adalah %d\n", a);
	printf("Alamat dari a adalah %p\n", &a); //format prinf specifier -> f"" / %
	printf(" Nilai dari b adalah %d\n", b);
	printf("Alamat dari b adalah %p\n", &b);

	int *c = &a; // integer pointer

	printf("Alamat dari c adalah %p\n", c);
	printf(" Nilai dari c adalah %d\n", *c);

	*c = 7;
	printf(" Nilai dari a adalah %d\n", a);
	printf(" Nilai dari c adalah %d\n", *c);

	a = 10;
	printf(" Nilai dari a adalah %d\n", a);
	printf(" Nilai dari c adalah %d\n", *c);

}