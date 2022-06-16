#include <bits/stdc++.h>

using namespace std;

char temp[] = "";

int main(){	
//	gets(temp);
	scanf("%[^\n]", &temp);
	string text = temp;
	while (text.length() != 0){
		printf("%s\n", text.c_str());		
//		gets(temp);
		scanf("%[^\n]", &temp);
		text = temp;
	}	
	return 0;
}
