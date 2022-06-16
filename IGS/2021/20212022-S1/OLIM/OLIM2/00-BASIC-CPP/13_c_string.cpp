#include <cstdio>

int main(){
	char house[] = "a house of gold.";
	printf("A book holds %s\n\n", house);

	printf("Size of char : %d\n", sizeof(char));
	printf("Size of house : %d\n", sizeof(house));
	printf("Length of house : %d\n", sizeof(house)-1);
	return 0;
}