#ifndef MIN_HEAP_H
#define MIN_HEAP_H

#include <stdio.h>
#include <limits.h>

/* 
 * A simple key–value struct for heap elements.
 * 'ptr' can store a pointer to any associated data.
 */
typedef struct {
    void *ptr;
    int key;
} Data;

/* Function prototypes */

/* Core heap operations */
void min_heapify(Data A[], int heapsize, int i);
void build_min_heap(Data A[], int length);
Data heap_extract_min(Data A[], int *heapsize);
int heap_decrease_key(Data A[], int i, int key);
int min_heap_insert(Data A[], int *heapsize, int length, Data new_data);

#endif /* MIN_HEAP_H */
