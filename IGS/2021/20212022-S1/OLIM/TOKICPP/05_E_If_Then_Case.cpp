#include <bits/stdc++.h>
using namespace std;

int number;

int main(){
	scanf("%d", &number);
	if (number < 10) printf("satuan\n");
	else if (number < 100) printf("puluhan\n");
	else if (number < 1000) printf("ratusan\n");
	else if (number < 10000) printf("ribuan\n");
	else if (number < 100000) printf("puluhribuan\n");
	
	return 0;
}
