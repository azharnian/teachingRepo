int mangga(int rambutan){
	if (rambutan == 1){
		return 1;
	} else {
		if (rambutan % 2 == 1)
		{
			return mangga(3 * rambutan + 1);
		} else {
			return mangga(int(rambutan/2));
		}
	}
}

int jeruk(int anggur, int melon){
	if (melon == 1)
	{
		return 0;
	} else {
		return mangga(anggur) * anggur + jeruk(anggur, melon-1);
	}
}

