#include <stdio.h>
#include "priority-queue.h"


typedef struct {
    char ch;
    struct Node* left;
    struct Node* right;
    int freq;
} Node;


Node*
huffman(Node arr[], int length) {
    Data queue[length];
    int heapsize = 0;

    for (int i = 0; i <= length; i++) {
        Data new_data;
        new_data.key = arr[i].freq;
        new_data.ptr = &arr[i];
        min_heap_insert(queue, &heapsize, length, new_data);
    }

    for (int i = 0; i <= length; i++) {
        printf("%d", queue[i].key);
    }

    return NULL;
}

int 
main2() 
{
    char a = 'a';
    char b = 'b';
    char c = 'c';

    Data data1 = {&a, 4};
    Data data2 = {&b, 1};
    Data data3 = {&c, 8};
    Data data4 = {&c, 2};

    Data arr[] = {data1, data2, data3, data4};
    int length = 4;
    int heapsize = length;

    build_min_heap(arr, heapsize);
    // heap_decrease_key(arr, 2, 2);
    Data min = heap_extract_min(arr, &heapsize);
    Data min2 = heap_extract_min(arr, &heapsize);

    min_heap_insert(arr, &heapsize, length, data3);
    
    for (int i = 0; i < heapsize; i++) {
        printf("%d\n", arr[i].key);
    }
    
    return 0;
}

int main() {


    int letters = 6;
    char chars[] = "abcdef";
    int freq[] = {10, 20, 25, 3, 120, 2};

    Node arr[letters];


    for (int i = 0; i <= letters; i++) {
        Node node = {chars[i], NULL, NULL, freq[i]};
        arr[i] = node;
    }

    huffman(arr, letters);

    return 0;
}
