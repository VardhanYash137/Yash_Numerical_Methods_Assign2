#include <stdio.h>
#include <math.h>
#include <float.h>

int main() {
    // Storing p and 2.0
    float pi = M_PI;
    float two = 2.0;

    // Calculating relative errors
    float relative_error_pi = fabs((pi - (float)pi) / pi);
    float relative_error_two = fabs((two - (float)two) / two);

    printf("Relative Error for p: %e\n", relative_error_pi);
    printf("Relative Error for 2.0: %e\n", relative_error_two);

    return 0;
}

