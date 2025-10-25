#include <limits.h>
#include "priority-queue.h"

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
min_heapify(Data A[], int heapsize, int i)
{
    int l = left(i);
    int r = right(i);
    int smallest;

    if (l < heapsize && A[l].key < A[i].key) {
        smallest = l;
    } else {
        smallest = i;
    }
    if (r < heapsize && A[r].key < A[smallest].key) {
        smallest = r;
    }

    if (smallest != i) {
        Data temp = A[i];
        A[i] = A[smallest];
        A[smallest] = temp;
        min_heapify(A, heapsize, smallest);
    }
}

void 
build_min_heap(Data A[], int length) 
{
    for (int i = length / 2; i >= 0; i--) {
        min_heapify(A, length, i);
    }
}

Data 
heap_extract_min(Data A[], int *heapsize) 
{
    Data min = A[0];
    A[0] = A[(*heapsize)-1];
    (*heapsize)--;
    min_heapify(A, *heapsize, 0);
    return min;
}

int 
heap_decrease_key(Data A[], int i, int key) 
{
    if (key > A[i].key) {
        return -1;
    }

    A[i].key = key;
    while (i > 0 && A[parent(i)].key > A[i].key) {
        Data temp = A[i];
        A[i] = A[parent(i)];
        A[parent(i)] = temp;
        i = parent(i);
    }

    return 0;
}

int
min_heap_insert(Data A[], int *heapsize, int length, Data new_data) {
    if ((*heapsize) > length) {
        return -1;
    }
    (*heapsize)++;
    int key = new_data.key;
    void *ptr = new_data.ptr;
    Data data = {ptr, INT_MAX};
    A[(*heapsize)-1] = data;


    heap_decrease_key(A, (*heapsize)-1, key);

    return 0;
}


