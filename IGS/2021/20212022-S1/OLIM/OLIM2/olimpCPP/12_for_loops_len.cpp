#include <cstdio>

int main(){
	short array[] = {104, 105, 32, 98, 105, 108, 109, 0};
	size_t len = sizeof(array) / sizeof(short);
	printf("%zd\n", len);
}