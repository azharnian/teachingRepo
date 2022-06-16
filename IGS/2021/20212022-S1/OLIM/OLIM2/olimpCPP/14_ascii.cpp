#include <cstdio>

int main()
{
	char alphabet[27];

	for (size_t i=0; i<26; i++)
	{
		alphabet[i] = i + 97;
	}
	alphabet[26] = 0;
	printf("%s\n", alphabet);
	printf("%c\n", alphabet[20]);
	printf("%d\n", alphabet[20]);
	printf("%x\n", alphabet[20]);

	for (size_t i=0; i<26; i++){
		alphabet[i] = i + 65;
	}
	printf("%s\n", alphabet);
	printf("%c\n", alphabet[20]);
	printf("%d\n", alphabet[20]);
	printf("%x\n", alphabet[20]);

	return 0;
}