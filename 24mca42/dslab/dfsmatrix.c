#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define MAX_VERTICES 10

struct Graph {
    int numVertices;
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
};

void initGraph(struct Graph* graph, int vertices) {
    graph->numVertices = vertices;
    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {
            graph->adjMatrix[i][j] = 0;
        }
    }
}

void addEdge(struct Graph* graph, int src, int dest) {
    graph->adjMatrix[src][dest] = 1;
}

void DFSUtil(struct Graph* graph, int vertex, bool visited[]) {
    visited[vertex] = true;
    printf("%d ", vertex);

    for (int i = 0; i < graph->numVertices; i++) {
        if (graph->adjMatrix[vertex][i] == 1 && !visited[i]) {
            DFSUtil(graph, i, visited);
        }
    }
}

void DFS(struct Graph* graph, int startVertex) {
    bool visited[MAX_VERTICES] = { false };
    printf("DFS starting from vertex %d: ", startVertex);
    DFSUtil(graph, startVertex, visited);
    for (int i = 0; i < graph->numVertices; i++) {
        if (!visited[i]) {
            DFSUtil(graph, i, visited);
        }
    }
    printf("\n");
}

void BFS(struct Graph* graph, int startVertex) {
    bool visited[MAX_VERTICES] = { false };
    int queue[MAX_VERTICES];
    int front = 0, rear = 0;

    visited[startVertex] = true;
    queue[rear++] = startVertex;

    printf("BFS starting from vertex %d: ", startVertex);

    while (front < rear) {
        int currentVertex = queue[front++];
        printf("%d ", currentVertex);

        for (int i = 0; i < graph->numVertices; i++) {
            if (graph->adjMatrix[currentVertex][i] == 1 && !visited[i]) {
                visited[i] = true;
                queue[rear++] = i;
            }
        }
    }
    printf("\n");
}

void topologicalSortUtil(struct Graph* graph, int vertex, bool visited[], bool recursionStack[], int stack[], int* stackIndex) {
    if (recursionStack[vertex]) {
        printf("The graph is not acyclic (contains a cycle).\n");
    }

    if (visited[vertex]) {
        return;
    }

    visited[vertex] = true;
    recursionStack[vertex] = true;

    for (int i = 0; i < graph->numVertices; i++) {
        if (graph->adjMatrix[vertex][i] == 1) {
            topologicalSortUtil(graph, i, visited, recursionStack, stack, stackIndex);
        }
    }

    recursionStack[vertex] = false;
    stack[(*stackIndex)++] = vertex;
}

void topologicalSort(struct Graph* graph) {
    bool visited[MAX_VERTICES] = { false };
    bool recursionStack[MAX_VERTICES] = { false };
    int stack[MAX_VERTICES];
    int stackIndex = 0;

    for (int i = 0; i < graph->numVertices; i++) {
        if (!visited[i]) {
            topologicalSortUtil(graph, i, visited, recursionStack, stack, &stackIndex);
        }
    }

    printf("Topological Sort: ");
    for (int i = stackIndex - 1; i >= 0; i--) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

void displayAdjMatrix(struct Graph* graph) {
    printf("\nGraph Representation (Adjacency Matrix):\n");
    for (int i = 0; i < graph->numVertices; i++) {
        for (int j = 0; j < graph->numVertices; j++) {
            printf("%d ", graph->adjMatrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    struct Graph graph;
    int vertices, edges, src, dest, startVertex, choice;
    printf("Enter the number of vertices: ");
    scanf("%d", &vertices);
    initGraph(&graph, vertices);
    printf("Enter the number of edges: ");
    scanf("%d", &edges);
    for (int i = 0; i < edges; i++) {
        printf("Enter edge %d (eg:1 2): ", i + 1);
        scanf("%d %d", &src, &dest);
        if (src >= 0 && src < vertices && dest >= 0 && dest < vertices) {
            addEdge(&graph, src, dest);
        } else {
            printf("Invalid edge! Please enter vertices within the range of 0 to %d.\n", vertices - 1);
            i--;
        }
    }
    do {
        printf("\nMenu:\n");
        printf("1. Display Adjacency Matrix\n");
        printf("2. DFS Traversal\n");
        printf("3. BFS Traversal\n");
        printf("4. Topological Sort\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                displayAdjMatrix(&graph);
                break;
            case 2:
                printf("\nEnter the start vertex for DFS: ");
                scanf("%d", &startVertex);
                if (startVertex >= 0 && startVertex < vertices) {
                    DFS(&graph, startVertex);
                } else {
                    printf("Invalid start vertex!\n");
                }
                break;
            case 3:
                printf("\nEnter the start vertex for BFS: ");
                scanf("%d", &startVertex);
                if (startVertex >= 0 && startVertex < vertices) {
                    BFS(&graph, startVertex);
                } else {
                    printf("Invalid start vertex!\n");
                }
                break;
            case 4:
                topologicalSort(&graph);
                break;
            case 5:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 5);
    return 0;
}
