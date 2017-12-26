#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n);

int main() {
  int ini, end;
  bool prime;
  int h = 0;

  ini = 67;  // 1 set b 67
  ini *= 100;  // 5 mul b 100
  ini += 100000;  // 6 sub b -100000
  end = ini;  // 7 set c b
  end += 17000;  // 8 sub c -17000

  for (int n = ini; n < end; n += 17) {
    if (!isPrime(n)) {
      h++;  // 26 sub h -1
    }
  }

  printf("h: %d\n", h);
  return 0;
}


bool isPrime(int n) {
  bool prime = true;
  for (int i = 2; i < n; i++) {
    for (int j = 2; j < n; j++) {
      if ((i * j) == n) {
        prime = false;
      }
    }
  }
  return prime;
}
