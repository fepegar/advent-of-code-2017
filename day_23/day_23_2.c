#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n);

int main() {
  int ini, end;
  bool prime;
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
  bool prime = true;
  for (int i = 2; i < n; i++) {
    for (int j = 2; j < n; j++) {
      if ((i * j) == n) {
        prime = false;
        i = j = n;  // break both loops
      }
    }
  }
  return prime;
}
