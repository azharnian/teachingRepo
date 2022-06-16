#include <cstdio>

int main(){
	bool t = true;
	bool f = false;
	printf("!true: %d\n", !t);
	printf("true  &&  false:\n", t &&  f);
	printf("true  && !false:\n", t && !f);
	printf("true  ||  false:\n", t ||  f);
	printf("true  ||  false:\n", f ||  f);
}