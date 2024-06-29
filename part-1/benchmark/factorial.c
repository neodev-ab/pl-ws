#include <stdio.h>
int factorial(int n) {
  int result = 1;
  for (int i = 1; i <= n; ++i)
    result *= i;
  return result;
}

int main() {
  // Loop through 0 to 12
  for (int i = 0; i <= 12; ++i)
    printf("%d\n", factorial(i));
  return 0;
}
