//Plain Old Data Classes - User-Defined Type, that contain data and functions.

#include <cstdio>

struct Book {
	char title[256];
	size_t year;
	size_t pages;
	bool hardcover;
};

int main(){
	Book PerahuKertas;
	PerahuKertas.pages = 342;
	printf("Perahu Kertas memiliki jumlah halaman sebanyak %d\n", PerahuKertas.pages);
	return 0;
}