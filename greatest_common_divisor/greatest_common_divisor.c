#include <stdio.h>

// Returns greates common divisor of two number
unsigned int gcd(unsigned int a, unsigned int b){

    unsigned int tmp;
    while(b != 0){
        tmp = b;
        b = a % b;
        a = tmp; 
    }
    
    return a;
}

int main(){
    printf("GCD(%u, %u) = %u\n", 3, 9, gcd(3, 9));
    printf("GCD(%u, %u) = %u\n", 0, 4, gcd(0, 4));
    printf("GCD(%u, %u) = %u\n", 0, 0, gcd(0, 0));
    printf("GCD(%u, %u) = %u\n", 21, 56, gcd(21, 56));

    return 0;
}
