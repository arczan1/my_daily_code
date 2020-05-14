#include <stdio.h>
#include <stdlib.h>

// Sort array using counting sort algorithm
void counting_sort(unsigned int* array, size_t size){
    // If array is empty, don't do anything
    if(size <= 0)
        return;

    // Find max values is array
    unsigned int max_value=array[0];
    for(int i = 0; i < size; i++){
        if(array[i] > max_value)
            max_value = array[i];
    }

    // Create array to count values
    unsigned int *count;
    count = (unsigned int*)malloc((max_value + 1) * sizeof(unsigned int));

    // Count values
    for(int i = 0; i < size; i++)
        count[array[i]] += 1;

    // Fill array with sorted values
    unsigned int value = 0;    
    for(int i = 0; i < size; i++){
        // If count of current value is 0 then go to next value
        while(count[value] == 0)
            value += 1;
        array[i] = value;
        count[value]--;
    }

    free(count);
}

int main(){
    unsigned int array[] = {3, 2, 3, 9, 2, 0};
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);

    counting_sort(array, 6);
    printf("\nSorted:\n");
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);
    printf("\n");
}
