#include <cstdio>

union Variant {
	char string[10];
	int integer;
	double floating_point;
};

int main(){
	Variant v;
	printf("Size of string[10] is %d\n", sizeof(v.string));
	printf("Size of integer is %d\n", sizeof(v.integer));
	printf("Size of floating_point is %d\n\n", sizeof(v.floating_point));

	printf("Address of string[10] is %p\n", &v.string);
	printf("Address of integer is %p\n", &v.integer);
	printf("Address of floating_point is %p\n\n", &v.floating_point);

	v.integer = 42;
	printf("The ultimate answer: %d\n\n", v.integer);


	v.floating_point = 2.7182818284;
	printf("Euler's number e: %f\n\n", v.floating_point);

	printf("A dumpster fire (no update): %d\n\n", v.integer);

	v.integer = 42;
	printf("The ultimate answer: %d\n\n", v.integer);


}