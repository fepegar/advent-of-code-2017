#include <stdio.h>

int main() {
  int a = 1;
  int b, c, d, e, f;
  int h = 0;

  b = 67;  // 1 set b 67
  c = b;  // 2 set c b
  b *= 100;  // 5 mul b 100
  b += 100000;  // 6 sub b -100000
  c = b;  // 7 set c b
  c += 17000;  // 8 sub c -17000

  do {
    f = 1;  // 9 set f 1
    d = 2;  // 10 set d 2
    do {
      e = 2;  // 11 set e 2
      do {
        if ((d * e) == b) {
          f = 0;  // 16 set f 0
        }
        e += 1;  // 17 sub e -1
      } while(e != b);
      d += 1;  // 21 sub d -1
    } while(d != b);
    if (f == 0) {  // 25 jnz f 2
      h += 1;  // 26 sub h -1
    }
    if (b == c) {
      break;  // 30 jnz 1 3
    }
    b += 17;  // 31 sub b -17
  } while(1);  // 32 jnz 1 -23

  printf("h: %d\n", h);
  return 0;
}
