/*
corner case: kalo n = 1e9, m = 1e9, a = 1
ans = 1e18
*/

#include <bits/stdc++.h>
using namespace std;

long long n, m ,a;

int main() {
	cin >> n >> m >> a;
	
	long long x, y;
	
	if (n % a == 0) x = n / a;
	else x = (n / a) + 1;
	
	if (m % a == 0) y = m / a;
	else y = (m / a) + 1;
	
	cout << x * y << "\n";
}