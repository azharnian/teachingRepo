#include <cstdio>
// https://ideone.com/0UZQQ0

int binary_search(int arr[],unsigned int arr_size, int item){
	unsigned int low = 0;
	unsigned int high = arr_size-1;
	unsigned int mid;
	unsigned int guess; 

	while (low <= high){
		mid = int((low+high)/2);
		guess = arr[mid];
		if (guess == item){
			return mid;
		} else if(guess > item){
			high = mid -1;
		} else {
			low = mid + 1;
		}
	};
	return -1;
}

int main(){
	int my_array[] = {1, 3, 5, 7, 9, 11, 13};
	unsigned int my_array_size = (sizeof(my_array) / sizeof(int));
	printf("%d\n",binary_search(my_array, my_array_size, 13));
	return 0;
}