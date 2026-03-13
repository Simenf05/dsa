#include <stdio.h>

void insertion_sort(int A[], int len) {
    int j;
    for (j = 1; j < len; j++) {
        int key = A[j];

        int i = j - 1;
        while (i >= 0 && A[i] > key) {
            A[i + 1] = A[i];
            i -= 1;
        }
        A[i + 1] = key;
    }
}

int main() {

    int nums[] = { 7, 2, 4, 3, 4, 7, 8, 9, 6, 1 };
    int numslen = sizeof(nums) / sizeof(*nums);

    int longlen = 1000000;
    int longarr[longlen];

    for (int i = 0; i < longlen; i++) {
        longarr[i] = nums[i % numslen];
    }

    insertion_sort(longarr, longlen);

    return 0;

    for (int i = 0; i < longlen; i++) {
        printf("%d ", longarr[i]);
    }
    printf("\n");

}
