#include <stdio.h>
#include <stdlib.h>

// Returns nth fibonacci number
unsigned long fib_number(unsigned int n){
    if(n <= 1)
        return 0;

    unsigned long a = 0, b = 1, tmp;
    for(int i = 0; i < (n - 2); i++){
        tmp = b;
        b = a + b;
        a = tmp;
    }

    return b;
}

// Returns fibonacci sequence
unsigned long* fib_sequence(size_t count){
    unsigned long* sequence;
    sequence = (unsigned long*)malloc(count * sizeof(unsigned long));

    if(count >= 1)
        sequence[0] = 0;
    if(count >= 2)
        sequence[1] = 1;

    for(int i = 2; i < count; i++){
        sequence[i] = sequence[i-1] + sequence[i-2];
    }

    return sequence;
}

int main(){
    // Test fib_number(0 to 9)
    for(int i = 0; i < 10; i++)
        printf("%d\n", fib_number(i));

    // Test fib_sequence(1 to 10)
    unsigned long *fi;
    for(int i = 0; i < 10; i++){
    	fi = fib_sequence(i);
    	for(int j = 0; j < i; j++)
    	    printf("%d ", fi[j]);
    	printf("\n");
    	free(fi);
    }

    return 0;
}
