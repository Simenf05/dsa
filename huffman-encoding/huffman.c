#include <stdio.h>

struct Node {
    char ch;
    struct Node* left;
    struct Node* right;
};


struct Node* 
make_tree(char chars[], int freq[], int letters)
{
    for (int i = 0; i <= letters; i++) {

        printf("%c", chars[i]);

    }

    struct Node* node;
    return node;
}


int main() {

    int letters = 6;
    char chars[] = "abcdef";
    int freq[] = {10, 20, 25, 3, 120, 2};


    struct Node* root = make_tree(chars, freq, letters);


    return 0;
}
