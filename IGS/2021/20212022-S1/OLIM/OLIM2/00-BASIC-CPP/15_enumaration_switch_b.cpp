#include <cstdio>

using namespace std;

//seveneves book
enum Race {
	Dinan,
	Teklan,
	Ivyn,
	Moiran,
	Camite,
	Julian,
	Aidan
};

enum Sex {
	Male,
	Female,
	Other
};

int main(){
	Race race = Dinan;

	switch(race){
	case Dinan : {
		printf("You work so hard.\n");
	} break;
	case Teklan : {
		printf("You are very strong\n");
	} break;
	case Ivyn : {
		printf("You are great leader/\n");
	} break;
	default : {
		printf("Error : unknown race!\n");
	}
	};
	return 0;
}