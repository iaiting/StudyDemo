/*******************************************************************************
 *
 * 当fahr=0, 20, ..., 300时，分别打印华氏温度与摄氏温度对照表
 *
 ******************************************************************************/
#include <stdio.h>

int main(int argc, char *argv) {
	int fahr, celsius;

	int lower, upper, step;
	
	lower = 0;
	upper = 300;
	step = 20;

	fahr = lower;
	while (fahr < upper) {
		celsius = 5 * (fahr - 32) / 9;
		printf("%6d\t%6d\n", fahr, celsius);	
		fahr += step;
	}

}

