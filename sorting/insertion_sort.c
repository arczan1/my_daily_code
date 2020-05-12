#include <stdio.h>
#include <stdlib.h>

// Sort array using insertion sort algorithm
void insertion_sort(int* array, size_t size){
    int value, j;
    for(int i = 1; i < size; i++){
        // Save value to insert
        value = array[i];
        j = i;
        // Move all greater values one place right
        while(j > 0 && value < array[j-1]){
            array[j] = array[j-1];
            j--;
        }
        // Insert value
        array[j] = value;
    }
}

int main(){
    int array[] = {3, 2, -3, 9, 2, 0};
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);

    insertion_sort(array, 6);
    printf("\nSorted:\n");
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);
    printf("\n");
}
