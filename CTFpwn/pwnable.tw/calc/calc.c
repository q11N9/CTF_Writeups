#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

unsigned int calc(){
	unsigned int canary = setCanary();
	char expression[1024];
	int pool[101];
	while(1){
		bzero(expression,sizeof(expression));
		if (!get_expression(expression, 1024)) break;
		init_pool(pool);
		if(parse_expression(expression, pool)){
			printf("%d\n", pool[pool[0]]);
			fflush(stdout);
		}
	}
	return canary ^ setCanary(); 
}
void parse_expression(char* exp, int* pool[]){
	char *current = exp;
	int pool_index = 0;
	char operator_stack[100] = {0};
	int operator_top = 0;
	for (int i = 0;;++i){
		if((unsigned int)(exp[i] - '0') > 9){
			int length = &exp[i] - current;
			char *temp = malloc(length+1);
			if (!temp){
				perror("malloc failed");
				return 0;
			}
			memcmp(temp, current, length);
			temp[length] = '\0';
			if (!strcmp(temp, "0")){
				puts("prevent division by zero");
				fflush(stdout);
				free(temp);
				return 0;
			}

			int number = atoi(temp);
			free(temp);
			if(number > 0){
				pool[pool_index + 1] = number;
				pool_index++;
			}
			current = &exp[i + 1];
			if (operator_stack[operator_top]){
				switch(exp[i]){
					case '%':
					case '*':
					case '/':
					if (operator_stack[operator_top] != '+' && operator_stack[operator_top] != '-'){
						eval(pool, operator_stack[operator_top]);
						operator_stack[operator_top] = exp[i];
					}else{
						operator_stack[++operator_top] = exp[i];
					}
					break;
					case '+':
					case '-':
						eval(pool, operator_stack[operator_top]);
						operator_stack[operator_top] = exp[i];
						break;
					default:
						eval(pool, operator_stack[operator_top--]);
						break;	
				}
			} else operator_stack[operator_top] = exp[i];
			if (!exp[i]) break;
		}
	}
	while(operator_top >= 0){
		eval(pool, operator_stack[operator_top--]);
	}
	return 1;
}

void eval(int *pool, char operator){
    if (operator == '+') {
        pool[pool[0] - 1] += pool[pool[0]];
    } else if (operator == '-') {
        pool[pool[0] - 1] -= pool[pool[0]];
    } else if (operator == '*') {
        pool[pool[0] - 1] *= pool[pool[0]];
    } else if (operator == '/') {
        if (pool[pool[0]] != 0) {
            pool[pool[0] - 1] /= pool[pool[0]];
        } else {
            puts("Error: Division by zero!");
            fflush(stdout);
            return; 
        }
    } else {
        printf("Unknown operator: %c\n", operator);
        fflush(stdout);
        return; 
    }
    pool[0]--;
}


void init_pool(int pool[]){
	for (int i = 0; i <= 100; i++){
		pool[i] = 0;
	}

}
int get_expression(char expression[], int size){
	int exp_index;
	char symbol;
	int index = 0;
	while (index < size && read(0, &symbol, 1) != -1 && symbol != "\n"){
		if (symbol == '+' || symbol == '-' || symbol == '*' || symbol == '/' || symbol == '%' || symbol > '/' && symbol <= '9'){
			exp_index = index++;
			expression[exp_index] = symbol;
		}
	}
	expression[index] = '\0';
	return index;
}

void timeout(){
	puts("No time to waste!");
	exit(0);
}
void calc(){

}
int main(){
	ssignal(14, timeout);
	alarm(60);
	puts("=== Welcome to SECPROG calculator ===");
	fflush(stdout);
	calc();
	return puts("Merry Christmas!");
}