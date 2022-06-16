//User-Defined Type
#include <cstdio>

//seveneves book
enum class Race {
	Dinan,
	Teklan,
	Ivyn,
	Moiran,
	Camite,
	Julian,
	Aidan
};

enum class Sex {
	Male,
	Female,
	Other
};

int main(){
	Race race = Race::Dinan;

	switch(race){
	case Race::Dinan : {
		printf("You work so hard.\n");
	} break;
	case Race::Teklan : {
		printf("You are very strong\n");
	} break;
	case Race::Ivyn : {
		printf("You are great leader/\n");
	} break;
	default : {
		printf("Error : unknown race!\n");
	}
	};
	return 0;
}