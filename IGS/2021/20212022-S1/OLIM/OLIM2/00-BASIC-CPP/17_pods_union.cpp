#include <cstdio>

union Variant {
	char string[2];
	int integer;
	double floating_point;
};

union Something {
	char dataString[2];
	int dataInteger;
	double dataFloat;
	bool dataBool;
}

int main(){
	Variant v;

	printf("Address of string id %p\n", &v.string);
	printf("Address of integer id %p\n", &v.integer);
	printf("Address of floating_point id %p\n", &v.floating_point);

	v.string[0] = 'a';
	v.string[1] = 0;
	printf("%c\n\n", v.string[0]);

	v.integer = 2020;
	printf("%d\n\n", v.integer);

	printf("%c\n\n", v.string[0]);

}