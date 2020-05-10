#include <stdio.h>
#include <stdlib.h>

// Sort array using selection sort algorithm
void selection_sort(int* array, size_t size){
    int tmp, min_index;
    for(int i = 0; i < (size - 1); i++){
        min_index = i;
        for(int j = (i + 1); j < size; j++){
            // Find index of min value
            if(array[j] < array[min_index])
                min_index = j;
        }
	// Move min value to the right place
        tmp = array[i];
        array[i] = array[min_index];
        array[min_index] = tmp;
    }
}

int main(){
    int array[] = {3, 2, -3, 9, 2, 0};
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);

    selection_sort(array, 6);
    printf("\nSorted:\n");
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);
    printf("\n");
}
