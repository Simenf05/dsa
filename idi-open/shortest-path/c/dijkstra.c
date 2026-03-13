#include <stdlib.h>
#include <err.h>
#include "priority-queue.h"


void print_graph(int n, int (*adj)[n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
             printf("%d ", adj[i][j]);
        }
        printf("\n");
    }
}

int *dijkstra(int n, int (*adj)[n], int s, int t) {

    int *path;
    path = malloc(sizeof(int)*(n+1));
    if (path == NULL) {
        err(EXIT_FAILURE, "path malloc");
    }

    
    Data queue[n];


    // Data *data = malloc(sizeof(Data));

    print_graph(n, adj);

    return path;
}

int main() {

    int nodes = 6;
    int edges[] = {0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 0};
    int weight[] = {1, 2, 3, 4, 5, 1};

    int (*adj)[nodes];
    adj = malloc(sizeof(int[nodes])*nodes);
    if (adj == NULL) 
        err(EXIT_FAILURE, "graph malloc.");

    for (int i = 0; i < nodes; i++) {
        for (int j = 0; j < nodes; j++) {
            adj[i][j] = 0;
        }
    }

    for (int i = 0; i < sizeof(edges) / 4; i += 2) {
        int u = edges[i];
        int v = edges[i+1];

        int weight_index = i / 2;

        adj[u][v] = weight[weight_index];
    }

    void *path;
    path = dijkstra(nodes, adj, 0, 4);
    if (path == NULL) 
        err(EXIT_FAILURE, "malloc");

    free(adj);
    free(path);

    return 0;
}
