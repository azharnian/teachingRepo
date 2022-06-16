#include <bits/stdc++.h>

using namespace std;

int n;

int main(){
	cin >> n;
	for(int row = 0; row < n; row++){
		for(int col = 0; col < n; col++){
			if (row + col >= n - 1){
				cout << "#";
			} else{
				cout << " ";
			}
			
		}
		cout << "\n";
	}
	
	return 0;
}
