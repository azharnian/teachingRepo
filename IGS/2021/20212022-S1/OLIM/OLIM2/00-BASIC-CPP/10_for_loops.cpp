#include <cstdio>
//#include <cstddef>

int main(){
	unsigned long max = 0;
	unsigned long values[] = { 10, 50, 20, 40, 0};

	//for (size_t i = 0; i < 5; i++){ // len(values)
	for (size_t i = 0; i < (sizeof(values)/sizeof(unsigned long)) ; i++){
		if (values[i] > max) max = values[i];
	}

	printf("The Maximum value in that array is %lu \n", max);

	return 0;
}