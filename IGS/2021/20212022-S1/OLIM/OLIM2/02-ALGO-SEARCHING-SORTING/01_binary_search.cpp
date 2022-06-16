#include <cstdio>

int binary_search(int arr[], unsigned int arr_size, int item){
	int low = 0;
	int high = arr_size - 1;
	unsigned int mid;
	int guess;

	while (low <= high){
		mid = int((low+high)/2);
		guess = arr[mid];
		if(guess == item){
			return mid;
		} else if (guess > item){
			high = mid - 1;
		} else {
			low = mid + 1;
		};
	};
	return -1;

}

int main(){
	int my_array[] = {1, 3, 5, 7, 9};
	unsigned int my_array_size = sizeof(my_array)/sizeof(my_array[0]);
	printf("%d\n", binary_search(my_array, my_array_size, 3));
	printf("%d\n", binary_search(my_array, my_array_size, 11));
	return 0;
}