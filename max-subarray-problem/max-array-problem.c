#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

void printarr(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

struct Max{
    int max_left;
    int max_right;
    int sum;
};

struct Max find_max_crossing_subarray(int A[], int low, int mid, int high) {

    int max_left;
    int left_sum = INT_MIN;
    int sum = 0;

    for (int i = mid; i >= low; i--) {
        sum += A[i];
        if (sum > left_sum) {
            left_sum = sum;
            max_left = i;
        }
    }

    int max_right;
    int right_sum = INT_MIN;
    sum = 0;

    for (int j = mid + 1; j <= high; j++) {
        sum += A[j];
        if (sum > right_sum) {
            right_sum = sum;
            max_right = j;
        }
    }

    struct Max max;

    max.max_left = max_left;
    max.max_right = max_right;
    max.sum = left_sum + right_sum;

    return max;
}

struct Max find_maximum_subarray(int A[], int low, int high) {
    struct Max max;

    if (high == low) {
        max.max_left = low;
        max.max_right = high;
        max.sum = A[low];
        return max;
    }

    int mid = floor((low + high) / 2);

    struct Max left_max = find_maximum_subarray(A, low, mid);
    struct Max right_max = find_maximum_subarray(A, mid + 1, high);
    struct Max cross_max = find_max_crossing_subarray(A, low, mid, high);

    if (left_max.sum >= right_max.sum && left_max.sum >= cross_max.sum) {
        max.max_left = left_max.max_left;
        max.max_right = left_max.max_right;
        max.sum = left_max.sum;
    }
    else if (right_max.sum >= left_max.sum && right_max.sum >= cross_max.sum) {
        max.max_left = right_max.max_left;
        max.max_right = right_max.max_right;
        max.sum = right_max.sum;
    }
    else {
        max.max_left = cross_max.max_left;
        max.max_right = cross_max.max_right;
        max.sum = cross_max.sum;
    }

    return max;
}


int main() {
    int longlen = 1000000;
    int longarr[longlen];

    long epoch = time(NULL);


    srandom(epoch);

    for (int i = 0; i < longlen; i++) {
        longarr[i] = floor(random() - (INT_MAX / 2));
    }

    struct Max max = find_maximum_subarray(longarr, 0, longlen);

    // printarr(longarr, longlen);
    printf("%d %d %d\n", max.max_left, max.max_right, max.sum);

    return 0;
}
