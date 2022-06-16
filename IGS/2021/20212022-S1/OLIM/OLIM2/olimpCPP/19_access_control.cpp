// a setter and getter, and label private

#include <cstdio>

struct ClockOfTheLongNow{
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

	private:
		int year;
};

int main(){
	ClockOfTheLongNow clock;
	//clock.year = 2017;
	clock.set_year(2020);

	clock.add_year();
	printf("Year : %d\n", clock.get_year());

	clock.add_year();
	printf("Year : %d\n", clock.get_year());
}