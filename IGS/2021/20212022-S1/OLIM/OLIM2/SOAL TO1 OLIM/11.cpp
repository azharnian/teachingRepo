int panggil(int x){
	if (x < 3)
	{
		return 0;
	} else {
		return panggil(x-1) + 2*panggil(x-2) +3;
	}
}

