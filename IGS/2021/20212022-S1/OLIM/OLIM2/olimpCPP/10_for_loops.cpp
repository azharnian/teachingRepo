//#include <cstddef>
#include <cstdio>

int main(){
	unsigned long maximum = 0;
	unsigned long values[] = {10, 50, 20, 40, 0};

	for(size_t i=0; i < 5; i++){
		printf("%d, %d\n", i, maximum);
		if(values[i] > maximum) maximum = values[i];
	}
	printf("The maximum value is %lu\n", maximum);
}