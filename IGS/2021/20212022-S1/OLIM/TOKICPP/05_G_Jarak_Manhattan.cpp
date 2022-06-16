#include <bits/stdc++.h>

using namespace std;

int x_init, y_init, x_final, y_final;

int main(){
	scanf("%d %d %d %d", &x_init, &y_init, &x_final, &y_final);
	int distance = abs(x_init - x_final) + abs (y_init - y_final);
	printf("%d\n", distance);
	
	return 0;
}
