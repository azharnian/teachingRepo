#include <cstdio>

int main(){
	unsigned long max = 0;
	unsigned long values[] = { 10, 50, 20, 40, 0};

	for (unsigned long value : values){
		if (value > max) max = value;
	}
	printf("The Maximum value in that array is %lu \n", max);
	return 0;
}
// 26 April 2020
// Bryan
// Danil
// Fioreno Malvin, 
// Fatah,
// Kenzie,
// Olivia,
// Putri Sahira
// Raven
// Samuel Natanael
// Vergeo
// Devan
// Trisha
// Vinita