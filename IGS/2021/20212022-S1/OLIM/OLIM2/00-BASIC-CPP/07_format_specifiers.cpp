#include <cstdio>
#include <cstddef>

int main(){
	size_t size_char = sizeof(char);
	printf("Char : %zd \n\n", size_char); // %zd %x %zx

	size_t size_short = sizeof(short);
	printf("Short : %zd \n\n", size_short);

	size_t size_size_t = sizeof(size_t);
	printf("Size_t : %d\n\n", size_size_t);
}
