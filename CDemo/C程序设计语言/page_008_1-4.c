/*******************************************************************************
 *
 * 练习1-4 编写一个程序打印摄氏温度转换为相应华氏温度的转换表
 *
 ******************************************************************************/

#include <stdio.h>

int main(int argc, char *argv) {
	float celsius;
	float fahr;

	for (celsius=0; celsius<=300; celsius+=20) {
		fahr = (celsius * 9 / 5) + 32;
		printf("%3.0f %6.1f\n", celsius, fahr);

	}

}
