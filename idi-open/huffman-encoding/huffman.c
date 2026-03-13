#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "priority-queue.h"


typedef struct Node {
    char ch;
    struct Node *left;
    struct Node *right;
    int freq;
} Node;


Node*
huffman(Node* arr[], int length) {
    Data queue[length];
    int heapsize = 0;

    for (int i = 0; i < length; i++) {
        Data new_data;
        new_data.key = arr[i]->freq;
        new_data.ptr = arr[i];
        min_heap_insert(queue, &heapsize, length, new_data);
    }

    for (int i = 0; i < length-1; i++) {

        Node* node = malloc(sizeof(Node));
        Data left = heap_extract_min(queue, &heapsize);
        Data right = heap_extract_min(queue, &heapsize);


        node->left = left.ptr;
        node->right = right.ptr;
        node->freq = left.key + right.key;

        Data new_data;
        new_data.key = node->freq;
        new_data.ptr = node;
        min_heap_insert(queue, &heapsize, length, new_data);
    }

    return heap_extract_min(queue, &heapsize).ptr;
}

char* 
concat(char* s1, char* s2) {
    char *result = malloc(strlen(s1) + strlen(s2) + 1);
    strcpy(result, s1);
    strcat(result, s1);
    return result;
}

int level(Node* node) {
    if (node == NULL) {
        return 0;
    }

    int current_level = 0;

    if (node->left != NULL) {
        int new_level = level(node->left);
        if (new_level > current_level) {
            current_level = new_level;
        }
    }

    if (node->right != NULL) {
        int new_level = level(node->right);
        if (new_level > current_level) {
            current_level = new_level;
        }
    }

    return current_level+1;
}

int count_nodes(Node* node) {
    if (node == NULL) {
        return 0;
    }

    int count = 1;

    if (node->left != NULL) {
        int left_count = count_nodes(node->left);
        count += left_count;
    }

    if (node->right != NULL) {
        int right_count = count_nodes(node->right);
        count += right_count;
    }

    return count;
}

void bfs(Node* node, int node_count) {
    Node* arr[node_count];
    int head = 0;
    int tail = 0;

    arr[head] = node;
    head++;


    while (head != tail) {

        Node* current = arr[tail];
        tail++;

        if (current->left != NULL) {
            arr[head] = current->left;
            head++;
        }
        if (current->right != NULL) {
            arr[head] = current->right;
            head++;
        }

        int current_level = level(current);

        printf("%d ", current->freq);
        printf("%d \n", current_level);

    }
}

void
print_tree(char * string[], Node* node) {

    int this_level = level(node);

    printf("%*d",this_level, node->freq*2);
    

    if (node->left != NULL) {
        print_tree(string, node->left);
    }

    if (node->right != NULL) {
        print_tree(string, node->right);
    }
}

int main() {

    int letters = 6;
    char chars[] = "abcdef";
    int freq[] = {10, 20, 25, 3, 180, 2};

    Node* arr[letters];


    for (int i = 0; i < letters; i++) {
        Node* node = malloc(sizeof(Node));
        node->ch = chars[i];
        node->freq = freq[i];
        arr[i] = node;
    }

    Node *root = huffman(arr, letters);

    // printf("%d\n", root->freq);

    // printf("%s", walk(root));

    int node_count = count_nodes(root);

    char string_grid[node_count];



    // bfs(root, node_count);

    return 0;
}
