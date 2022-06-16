#include <cstdio>

// int tambah(int a){
// 	return a + 20;
// }
void tambah(int *xPointer){
	*xPointer = *xPointer + 20;
}

int main(){
	int x = 10;
	// x = tambah(x);
	tambah(&x); // assign pointer -> alamat bukan value.
	printf("Nilai x = %d\n", x);
}