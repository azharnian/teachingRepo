#include <bits/stdc++.h>
using namespace std;

int number, temp, total;

int main(){
	total = 0;
	scanf("%d", &number);
	for (int i=0;i < number; i++){
		scanf("%d", &temp);
		total += temp;
	}
	printf("%d\n", total);
	
	return 0;
}
