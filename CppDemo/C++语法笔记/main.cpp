#include <stdio.h>

void foo()  {
	int j = 0;
	static int k = 0;
	
	++j;
	++k;
	printf("j: %d, k: %d\n", j, k);
}

int main(void) {
	for (int i=0; i<=5; i++) {
		printf("[%d] ",i);
		foo();
	}
}
