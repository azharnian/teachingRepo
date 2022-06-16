#include <bits/stdc++/h>
using namespace std;

int N, M;
long long fib[105];

long long f(int n){
	if (n == 0 or n == 1) return 1;
	return f(n-1) + f(n-2);
}

int main(){
	cin >> N;
	cout << f(N) << "\n";
}
