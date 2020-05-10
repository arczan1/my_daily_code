#include <stdio.h>
#include <stdlib.h>

// Sort array using bubble sort algorithm
void bubble_sort(int* array, size_t size){
    int tmp;
    for(int i = 0; i < size; i++){
        for(int j = 0; j < (size - i - 1); j++){
            if(array[j] > array[j+1]){
                // Swap values
                tmp = array[j];
                array[j] = array[j+1];
                array[j+1] = tmp;
            }
        }
    }
}

int main(){
    int array[] = {3, 2, -3, 9, 2, 0};
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);

    bubble_sort(array, 6);
    printf("\nSorted:\n");
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);
    printf("\n");
}
