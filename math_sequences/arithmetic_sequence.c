#include <stdio.h>

typedef struct ArithmeticSequence{
    /*
    Formula: an = a1 + (n - 1) * r
    an - nth element
    a1 - first element 
    r - difference
    */
    double first_element;
    double diff;
}ArithmeticSequence;

// Returns nth element of arithmetic sequence(n >= 1)
double get_element(ArithmeticSequence seq, unsigned int n){
    // an = a1 + (n - 1) * r
    return seq.first_element + (n - 1) * seq.diff;
}

// Returns sum of the first n elements of arithmetic sequence
double sum(ArithmeticSequence seq, unsigned int n){
    // Sum = ((2 * a1) + (n - 1) * r) * (n / 2)
    return ((2 * seq.first_element) + (n - 1) * seq.diff) * (n / 2.0);
}

int main(){
    // 5.3, 3.3, 1.3...
    ArithmeticSequence seq = {5.3, -2};
    for(int i = 1; i < 10; i++){
        // Print ith element and sum of the first i elements
        printf("%.1f %.1f\n", get_element(seq, i), sum(seq, i));
    }
    return 0;
}
