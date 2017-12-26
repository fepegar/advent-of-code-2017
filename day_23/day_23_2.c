#include <stdio.h>

int main() {
  int a = 1;
  int b, c, i, j, prime;
  int h = 0;

  b = 67;  // 1 set b 67
  c = b;  // 2 set c b
  b *= 100;  // 5 mul b 100
  b += 100000;  // 6 sub b -100000
  c = b;  // 7 set c b
  c += 17000;  // 8 sub c -17000

  while (1) {
    prime = 1;  // 9 set f 1

    for (int i = 2; i < b; i++) {
      for (int j = 2; j < b; j++) {
        if ((i * j) == b) {
          prime = 0;  // 16 set f 0
        }
      }
    }

    if (!prime) {  // 25 jnz f 2
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
