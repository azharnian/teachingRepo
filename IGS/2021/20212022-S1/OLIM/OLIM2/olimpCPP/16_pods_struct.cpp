//Plain Old Data Classes - Class / User Defined type that contain data and functions.
//Struct C compatible (useful low-level)
#include <cstdio>

struct Book
{
	char name[256];
	size_t year;
	size_t pages;
	bool hardcover;
};

int main()
{
	Book neuromancer;
	neuromancer.pages = 271;
	printf("Neuromancer has %d pages.\n",neuromancer.pages);
	return 0;
}