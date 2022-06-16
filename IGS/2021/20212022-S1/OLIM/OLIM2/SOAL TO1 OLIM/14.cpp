int wow(int n){
	int res, i, count;
	res = 1;
	for (i=2, i<=n; i++){
		count = 0;
		while (n%i == 0) do{
			n = int(n/i);
			count += 1;
		}
		res *= (count+1);
	}
	return res;
}

