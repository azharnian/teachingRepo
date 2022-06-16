#include <cstdio>

using namespace std;

enum Race{
	Dinan,
	Teklan,
	Ivyn,
	Moiran,
	Camite,
	Julian,
	Aidan
};

int main(){
	Race race = Dinan;

	switch(race){
	case Dinan: {
		printf("You work hard.\n");
	} break;
	case Teklan: {
		printf("You are very string\n");
	} break;
	case Ivyn: {
		printf("You are a great leader\n");
	} break;
	case Moiran: {
		printf("My, how versatile you are!\n");
	} break;
	case Camite: {
		printf("You are incredibly helpful\n");
	} break;
	case Julian: {
		printf("Anything you want\n");
	} break;
	case Aidan: {
		printf("What an enigma\n");
	} break;
	default: {
		printf("Error: unknown race!\n");
	}
	};
	return 0;
}