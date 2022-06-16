int hitung(int n){
	if (n==0){
		return 0;
	} else {
		return hitung(int(n/5)) + (n%5);
	}
}

