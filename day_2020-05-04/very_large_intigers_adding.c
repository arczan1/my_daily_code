#include <stdio.h>
#include <stdlib.h>

// Very large intiger representation
typedef struct{
    // Digits are in reversed order example:
    // {1, 2, 3, 4} represents 4321 
    char *digits; 
    size_t len;
}vli;

void print_vli(vli *number){
    for(int i = number->len; i > 0; i--){
        putchar('0' + number->digits[i-1]); 
    }
}

vli* add_vli(vli *a, vli *b){
    vli *sum = (vli*)malloc(sizeof(vli));

    size_t len = (a->len>b->len)?a->len:b->len;
    // Max length of result is len of longer number + 1
    sum->len = len + 1;
    sum->digits = (char*)malloc(sum->len*sizeof(char));

    // Adding numbers
    for(int i = 0; i<len;i++){
        if(i < a->len)
            sum->digits[i] += a->digits[i];
        if(i < b->len)
            sum->digits[i] += b->digits[i];

	// Carry to next column
	sum->digits[i+1] = sum->digits[i] / 10;

	// Keep only unit digit 
	sum->digits[i] %= 10;
    }

    return sum;
}

int main(){
    // Digits in REVERSED ORDER
    char n1[] = {3, 3, 2, 3, 9, 2, 2, 9, 2, 9, 2};
    char n2[] = {9, 3, 2, 1, 3, 0, 0, 0, 3, 3};

    vli a = {n1, 11};
    vli b = {n2, 10};

    vli* sum = add_vli(&a, &b);

    print_vli(&a);
    putchar('\n');
    print_vli(&b);
    putchar('\n');
    print_vli(sum);
    putchar('\n');

    return 0;
}
