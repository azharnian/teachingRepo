#include <cstdio>

// int tambah(int a){
// 	return a + 20;
// }
void tambah(int &xRef){
	xRef = xRef + 20;
}

int main(){
	int x = 10;
	// x = tambah(x);
	tambah(x); // assign pointer -> alamat bukan value.
	printf("Nilai x = %d\n", x);
}

//linked list
//double linked list
//etcß