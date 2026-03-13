#ifndef LIST_H
#define LIST_H

struct Node {
    int id;
    struct List* neighbors;
};

struct List {
    int total_length;
    int current_length;
    struct Node *data;
};

struct List *create_list();
void add_element(struct List *list, struct Node *element);
void free_list(struct List *list);

#endif

