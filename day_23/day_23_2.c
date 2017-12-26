#include <stdio.h>
#include <stdbool.h>

bool isPrime(int n);

int main() {
  int b, c;
  bool prime;
  int h = 0;

  b = 67;  // 1 set b 67
  b *= 100;  // 5 mul b 100
  b += 100000;  // 6 sub b -100000
  c = b;  // 7 set c b
  c += 17000;  // 8 sub c -17000

  while (1) {
    if (!isPrime(b)) {  // 25 jnz f 2
      h += 1;  // 26 sub h -1
    }

    if (b == c) {
      break;  // 30 jnz 1 3
    }

    b += 17;  // 31 sub b -17
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
