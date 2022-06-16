#include <bits/stdc++.h>

using namespace std;

int arr[5], Min, Max, Sum;

int main(){
	long int len_arr = sizeof(arr)/sizeof(arr[0]); // hr -1
	for (int i = 0; i < len_arr; i++){
		cin >> arr[i];
	}
	
	for (int i = 0; i < len_arr; i++){
		Sum = 0;
		for (int j = 0; j < len_arr; j++){
			if (i != j) Sum+=arr[j];
		}
		if (i == 0) {
			Min = Sum;
			Max = Sum;
		}
		if (Sum < Min) Min = Sum;
		if (Sum > Max) Max = Sum;
	}
	cout << Min << " " << Max << "\n";
	return 0; 
}
