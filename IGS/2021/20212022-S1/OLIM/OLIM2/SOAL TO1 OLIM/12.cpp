int sikat(int x, int y){
	if (x >= y)
	{
		return x;
	} else {
		return 3*sikat(x+1, y) + 2*sikat(x, y-1);
	}
}

