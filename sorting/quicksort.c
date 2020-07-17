#include <stdio.h>

// Split array in two pieces(left smaller than pivot, right greater than pivot)
// Pivot is value of element at last_index
int make_partition(int* array, int first_index, int last_index);

// Sort array using quicksort algorithm
void quick_sort(int* array, int first_index, int last_index){
    if(last_index > first_index){
        int p = make_partition(array, first_index, last_index);
        quick_sort(array, first_index, p-1);
        quick_sort(array, p+1, last_index);
    }
}

int make_partition(int* array, int first_index, int last_index){
    int pivot = array[last_index];
    int p = first_index;
    int tmp;

    // Move elements smaller than pivot to the left side of array
    for(int i = first_index; i < last_index; i++){
        if(array[i] < pivot){
            tmp = array[p];
            array[p] = array[i];
            array[i] = tmp;
            p++;
        }
    }

    // Place pivot at the right place
    array[last_index] = array[p];
    array[p] = pivot;

    return p;
}

int main(){
    int array[] = {3, 2, -3, 9, 2, 0};
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);

    quick_sort(array, 0, 5);
    printf("\nSorted:\n");
    for(int i = 0; i < 6; i++)
        printf("%d ", array[i]);
    printf("\n");
}
