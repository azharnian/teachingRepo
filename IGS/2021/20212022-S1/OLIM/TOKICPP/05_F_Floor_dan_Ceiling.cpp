#include <bits/stdc++.h>
#include <cmath>
using namespace std;

float number;

int main(){
	scanf("%f", &number);
	int int_number = trunc(number);
	if (number == int_number) printf("%d %d\n", int_number, int_number);
	else {
		if (number > 0) printf("%d %d\n", int_number, int_number+1);
		else printf("%d %d\n", int_number-1, int_number);	
	}
	
	return 0;
}
