#include <cstdio> // getter, setter IDE ECLIPS / NETBEANS / CODEBLOCK

class ClockOfTheLongNow{
	int year;

	public:
		void add_year(){
			year++;
		}

		bool set_year(int new_year){
			if (new_year < 2019) return false;
			year = new_year;
			return true;
		}

		int get_year(){
			return year;
		}

};

int main(){
	ClockOfTheLongNow clock;

	clock.set_year(2019);

	clock.add_year();
	printf("Year : %d\n", clock.get_year());
	clock.add_year();
	printf("Year : %d\n", clock.get_year());
}

// 8 May 2021
// Devan
// Trisha
// Jesse 
// Daniel
// Fioreno Malvin
// Gregorius Wilson
// Kemas Fatah
// Kenzie
// Malvin Ferdinand
// Putri Sahira
// Raven
// Samuel
// Vergeo
// Vinita