#include <stdio.h>
#include <stdlib.h>

#include "list.h"

struct List *create_list() {
    struct List *new_list = malloc(sizeof(struct List));
    if (new_list == NULL) {
        printf("Memory did not allocate.");
        return NULL;
    }
    new_list->total_length = 10;
    new_list->current_length = 0;
    new_list->data = calloc(new_list->total_length, sizeof(struct Node));
    return new_list;
}

void add_element(struct List *list, struct Node *element) {
    if (list->total_length == list->current_length) {
        int new_size = list->total_length+10;
        struct Node *tmp = realloc(list->data, new_size * sizeof(struct Node));
        if (tmp == NULL) {
            printf("Memory resize failed.\n");
            return;
        }

        list->data = tmp;
        list->total_length = new_size;
    }

    struct Node *data = list->data;
    data[list->current_length] = *element;
    list->current_length++;
}

void free_list(struct List *list) {
    free(list->data);
    free(list);
}

