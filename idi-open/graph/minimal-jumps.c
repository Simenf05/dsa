#include<stdio.h>
#include<stdbool.h>
#include<limits.h>
#include<stdlib.h>

#include "list.h"

struct Node create_node(int id) {
    struct List *list = create_list();
    struct Node node = { id, list };
    
    return node;
}

int shortest_path_to_node(struct Node current_node, int goal, struct List *visited) {
    add_element(visited, &current_node);

    if (current_node.id == goal) {
        return 0;
    }

    if (current_node.id == 1 && visited->current_length > 1) {
        printf("exit\n");
        exit(0);
    }


    int amount_of_neighbors = current_node.neighbors->current_length;

    int length_of_paths[amount_of_neighbors];

    for (int i = 0; i < amount_of_neighbors; i++) {
        struct Node visiting_node = current_node.neighbors->data[i];

        bool already_visited = false;

        printf("current node: %d\n", current_node.id);
        for (int j = 0; j < visited->current_length; j++) {
            struct Node node = visited->data[i];
            printf("%d\n", visiting_node.id);
            printf("%d\n", node.id);

            if (visiting_node.id == node.id) {
                printf("skipping\n");
                printf("\n");
                already_visited = true;
                length_of_paths[i] = -1;
                break;
            }
            printf("\n");
        }

        if (already_visited) {
            continue;
        }

        int path = shortest_path_to_node(visiting_node, goal, visited);
        length_of_paths[i] = path;
    }

    int smallest = -1;

    for (int i = 0; i < amount_of_neighbors; i++) {
        int length = length_of_paths[i];

        if (smallest < 0) {
            smallest = length;
            continue;
        }

        if (length < smallest && length >= 0) {
            smallest = length;
        }
    }

    if (smallest == -1) {
        return -1;
    }

    return smallest + 1;
}


int main() {

    struct Node node1 = create_node(1);
    struct Node node2 = create_node(2);
    struct Node node3 = create_node(3);
    struct Node node4 = create_node(4);

    add_element(node1.neighbors, &node2);
    add_element(node2.neighbors, &node3);
    // add_element(node3.neighbors, &node1);
    // add_element(node2.neighbors, &node4);
    add_element(node2.neighbors, &node1);


    struct List *visited_nodes = create_list();
    int path_length = shortest_path_to_node(node1, 4, visited_nodes);

    printf("distance: %d\n", path_length);

    free_list(node1.neighbors);
    free_list(node2.neighbors);
    free_list(node3.neighbors);
    free_list(node4.neighbors);
    free_list(visited_nodes);

    return 0;
}
