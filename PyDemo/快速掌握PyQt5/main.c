#include <stdio.h>

void hexdecode(char *hexstr, int inlen, char *out) {
	printf("%s\n", hexstr);

	int i = 0;
	char *data = out;
	for (i=0; i<inlen; i++) {
		char tmp;
		printf("%c\n", hexstr[i]);
		if ( hexstr[i] >= '0' && hexstr[i] <='9' ) {
			tmp = hexstr[i] - '0';	
		}
		else if (( hexstr[i] >= 'A' && hexstr[i] <='F' ) ) {
			tmp = hexstr[i] - 'A' + 10;	

		}
		else if ((hexstr[i] >= 'a' && hexstr[i] <='f')) {
			tmp = hexstr[i] - 'a' + 10;	
		}

		else {
			
			//tmp = hexstr[i];
			printf("eeeeeeeeeeee\n");
		}

		if ( i % 2 == 0 ) {
		 	data[i/2] = tmp<<4; 
		}
		else {
			data[i/2] = data[i/2] | tmp;
		}

		printf("tmp :%02x\n", tmp);
	}

}

int main() {
	char out[16];
	hexdecode("11AF", 4, out);

	int i = 0;
	for (i=0; i<2; i++) {
		printf("%p: %02X\n", out+i, *(out+i));
	}
	printf("\n");
}
