#include <stdio.h>

typedef struct {
    char ch;
    int value;
} Satdata;

int parent(int i) {
    return i / 2;
}

int 
left(int i) {
    if (i == 0) {
        return 1;
    }
    return 2*i;
}

int 
right(int i) {
    if (i == 0) {
        return 2;
    }
    return 2*i + 1;
}

void 
min_heapify(int A[], int heapsize, int i)
{
    int l = left(i);
    int r = right(i);
    int smallest;

    if (l < heapsize && A[l] < A[i]) {
        smallest = l;
    } else {
        smallest = i;
    }
    if (r < heapsize && A[r] < A[smallest]) {
        smallest = r;
    }

    if (smallest != i) {
        int temp = A[i];
        A[i] = A[smallest];
        A[smallest] = temp;
        min_heapify(A, heapsize, smallest);
    }
}

void 
build_min_heap(int A[], int length) 
{
    for (int i = length / 2; i >= 0; i--) {
        min_heapify(A, length, i);
    }
}

int 
heap_extract_min(int A[], int length) 
{
    if (length < 0) {
        return -1;
    }
    int min = A[0];
    A[0] = A[length-1];
    min_heapify(A, length-1, 0);
    return min;
}

int 
heap_decrease_key(int A[], int i, int key) 
{
    if (key > A[i]) {
        return -1;
    }

    A[i] = key;
    while (i > 0 && A[parent(i)] > A[i]) {
        int temp = A[i];
        A[i] = A[parent(i)];
        A[parent(i)] = temp;
        i = parent(i);
    }

    return 0;
}


int 
main() 
{


    Satdata data1 = {'a', 5};
    Satdata data2 = {'b', 10};
    Satdata data3 = {'c', 13};

    int arr[] = {1, 3, 4, 5, 2};
    int len = 5;

    build_min_heap(arr, len);
    heap_decrease_key(arr, 3, 0);
    
    for (int i = 0; i < len; i++) {
        printf("%d\n", arr[i]);
    }
    
    return 0;
}



