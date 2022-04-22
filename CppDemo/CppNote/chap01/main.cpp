#include <stdio.h>
#include <iostream>

#include "chap01.h"

void foo()  {
	int j = 0;
	static int k = 0;
	
	++j;
	++k;
	printf("j: %d, k: %d\n", j, k);
}


void test1() {
	const int ci = 10;
	auto auto_ci = ci;
	auto_ci = 20;

	const int &cr = ci;
	auto auto_cr = cr;
	auto_cr = 30;

	const int *cp = &ci;
	auto auto_cp = cp;
}

void test2() {
	const int i = 42;
	// const int k; 错误
}


extern const int m = 100;

int main(void) {
	for (int i=0; i<=5; i++) {
		printf("[%d] ",i);
		foo();
	}

	test1();
	
//	extern int m;
	std::cout<<"m:" << m << std::endl;

	chap01_4_001();
}
