#include <limits.h>
#include <math.h>
#include <stdio.h>

void printarr(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void merge(int A[], int p, int q, int r) {
    int n_1 = q - p + 1;
    int n_2 = r - q;

    int L[n_1 + 1];
    int R[n_2 + 1];

    for (int i = 0; i < n_1; i++) {
        L[i] = A[p + i];
    }
    for (int i = 0; i < n_2; i++) {
        R[i] = A[q + i + 1];
    }

    L[n_1] = INT_MAX;
    R[n_2] = INT_MAX;
    int i = 0;
    int j = 0;

    for (int k = p; k <= r; k++) {
        if (L[i] <= R[j]) {
            A[k] = L[i];
            i++;
        }
        else {
            A[k] = R[j];
            j++;
        }
    }
}

void merge_sort(int A[], int p, int r) {
    if (p < r) {
        int q = floor((p + r) / 2);
        merge_sort(A, p, q);
        merge_sort(A, q + 1, r);
        merge(A, p, q, r);
    }
}

int main() {

    int nums[] = { 1, 5, 2 ,3 ,5 ,6 ,9, 8 ,3, 1, 2, 4};
    int numslen = sizeof(nums) / sizeof(*nums);

    int longlen = 1000000;
    int longarr[longlen];

    for (int i = 0; i < longlen; i++) {
        longarr[i] = nums[i % numslen];
    }

    merge_sort(longarr, 0, longlen - 1);

    // printarr(nums, numslen);

}
