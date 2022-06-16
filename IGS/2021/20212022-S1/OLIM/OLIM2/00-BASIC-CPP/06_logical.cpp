#include <cstdio>

int main(){
	bool t = true;
	bool f = false;
	printf("!true %d\n", !t);
	printf("true && false %d\n", t && f);
	printf("false || true %d\n", f || f);
}