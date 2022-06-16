#include <cstdio>

int main(){
	char alphabet[27];

	alphabet[0] = 'a'; //  a = 97, A = 65
	printf("first : %c\n", alphabet[0]);
	printf("first : %d\n", alphabet[0]); // decimal code
	printf("first : %x\n", alphabet[0]); // hexa code

	alphabet[1] = 100;
	printf("first : %c\n", alphabet[1]);
	printf("first : %d\n", alphabet[1]);
	printf("first : %x\n", alphabet[1]);

	for (size_t i = 0; i < 26; i++) alphabet[i] = i+97;
	alphabet[26] = 0;
	printf("%s\n", alphabet);
	printf("%d\n", alphabet[26]);



	return 0;
}