#include <stdio.h>
#include <math.h>

typedef struct GeometricSequence{
    /*
    Formula: an = a1 * r^(n-1)
    an - nth element
    a1 - first element 
    r - common ratio
    */
    double first_element;
    double common_ratio;
}GeometricSequence;

// Returns nth element of geometric sequence(n >= 1)
double get_element(GeometricSequence seq, unsigned int n){
    // an = a1  * r^(n-1)
    return seq.first_element * pow(seq.common_ratio, n - 1);
}

// Returns sum of the first n elements of geometirc sequence
double sum(GeometricSequence seq, unsigned int n){
    if(seq.common_ratio == 1)
        // Sum = a1 * n, for r == 1
        return seq.first_element * n;
    else
        // Sum = a1 * ((1 - r^n) / (1 - r)), for r != 1
        return seq.first_element *
            ((1 - pow(seq.common_ratio, n)) / (1 - seq.common_ratio));
}

int main(){
    // 0,5, 1, 2, 4, 8, ...
    GeometricSequence seq = {0.5, 2};
    for(int i = 1; i < 10; i++){
        // Print ith element and sum of the first i elements
        printf("%.1f %.1f\n", get_element(seq, i), sum(seq, i));
    }
    return 0;
}
