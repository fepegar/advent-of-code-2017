#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int n);

int main() {
  int ini, end;
  int notPrimes = 0;

  ini = 106700;
  end = 123700;

  for (int n = ini; n < end; n += 17) {
    if (!isPrime(n)) {
      notPrimes++;
    }
  }

  printf("h: %d\n", notPrimes);
  return 0;
}


bool isPrime(int n) {
  for(int i = 2; i <= sqrt(n); i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}
