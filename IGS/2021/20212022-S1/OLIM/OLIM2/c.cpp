/*
Kalo n habis dibagi 3, c1 = c2, c2 = n / 3

Kalo n % 3 == 1, c1 = c2 + 1, c2 = n / 3

Kalo n % 3 == 2, c2 = c1 + 1, c1 = n / 3
*/

#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
	cin >> N;
	
	for (int i = 1; i <= N; i++) {
		int n; cin >> n;
		
		int c1, c2;
		if (n % 3 == 0) {
			c2 = n / 3; c1 = c2;
		}
		else if (n % 3 == 1) {
			c2 = n / 3; c1 = c2 + 1;
		}
		else {
			c1 = n / 3; c2 = c1 + 1;
		}
		
		cout << c1 << " " << c2 << "\n";
	}
}