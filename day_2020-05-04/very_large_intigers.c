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
    // Max length of result is length of longer number + 1
    sum->len = len + 1;
    sum->digits = (char*)malloc(sum->len*sizeof(char));

    // Adding numbers
    for(int i = 0; i < len; i++){
        if(i < a->len)
            sum->digits[i] += a->digits[i];
        if(i < b->len)
            sum->digits[i] += b->digits[i];

	// Carry to next column
	sum->digits[i+1] += sum->digits[i] / 10;

	// Keep only unit digit 
	sum->digits[i] %= 10;
    }

    return sum;
}

vli* multiply_vli(vli *a, vli *b){
    vli *result = (vli*)malloc(sizeof(vli));

    // Max length of result is length of a + length of b
    result->len = a->len + b->len;
    result->digits = (char*)malloc(result->len*sizeof(char));

    for(int i = 0; i < a->len; i++){
        // Multiply b * a[i] and add it to result
        for(int j = 0; j < b->len; j++){
            result->digits[i+j] += a->digits[i] * b->digits[j];

            // Carry to next column
	    result->digits[i+j+1] += result->digits[i+j] / 10;

	    // Keep only unit digit 
	    result->digits[i+j] %= 10;
        }
    }

    return result;
}
int main(){
    // Digits in REVERSED ORDER
    char n1[] = {3, 9, 2, 3, 9, 2, 2, 9, 2, 9, 2};
    char n2[] = {9, 3, 2, 1, 3, 0, 0, 0, 3, 3};

    vli a = {n1, 11};
    vli b = {n2, 10};

    vli *sum = add_vli(&a, &b);
    vli *mul = multiply_vli(&a, &b);

    print_vli(&a);
    putchar('\n');
    print_vli(&b);
    putchar('\n');
    print_vli(sum);
    putchar('\n');
    print_vli(mul);
    putchar('\n');

    return 0;
}
