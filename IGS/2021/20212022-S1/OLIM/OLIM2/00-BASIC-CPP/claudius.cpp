#include <cstdio>

class Tree {
	char name[];
	int age;

	public:
	char getName(){
		return name;
	}

	int getAge(){
		return age;
	}

	void setName(char a_name[]) {
		name = a_name;
	}

	void setAge(int an_age) {
		age = an_age;
	}
};

int main(){
	Tree t1;
	t1.setName("t1")
	t1.setAge(5)
	printf("the first tree's name: %c\n", t1.getName() );
	printf("the first tree's age: %d", t1.getAge())
};