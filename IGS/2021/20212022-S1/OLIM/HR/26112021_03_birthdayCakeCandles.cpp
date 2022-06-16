#include <bits/stdc++.h>

using namespace std;

int main(){
    long N;
    long int candles[1000001];
    
    cin >> N;
    
    for (int i=0; i < N; i++){
        cin >> candles[i];
    }
    
    long temp, max;
    for (int i=0; i<N; i++){
        temp = (candles[i] + candles[i+1] + abs(candles[i] - candles[i+1])) / 2;
        if (i == 0) max = temp;
        if (temp > max) max = temp;
    }
    
    long counter = 0;
    for (int i=0; i<N; i++){
        if (candles[i] == max) counter++;
    }
    
    cout << counter << "\n";
    return 0;
}
