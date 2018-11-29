#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char* argv[]){

	if (argc != 4){
		printf("\n calc needs 3 arguments - operator1 operation operator2. E.g. \"calc 2 + 2\" \n");
		printf("	asterisk should be escaped: \"calc 2 \\* 2\" \n\n");
		//return 4;
	}

	switch(argv[2][0]){
		case '*':
			printf("\n%.2f\n\n", strtof(argv[1], NULL) * strtof(argv[3], NULL));
			break;
		case '+':
			printf("\n%.2f\n\n", strtof(argv[1], NULL) + strtof(argv[3], NULL));
			break;
		case '-':
			printf("\n%.2f\n\n", strtof(argv[1], NULL) - strtof(argv[3], NULL));
			break;
		case '/':
			printf("\n%.2f\n\n", strtof(argv[1], NULL) / strtof(argv[3], NULL));
			break;
	}

	return 0;
}