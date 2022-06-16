/*
YES jika w genap dan w / 2 genap --> w % 2 == 0 dan w != 2
NO selainnya
*/

#include <bits/stdc++.h>
using namespace std;

int w;

int main() {
	cin >> w;
	
	if (w % 2 == 0 and w != 2) {
		cout << "YES\n";
	}
	else cout << "NO\n";
}