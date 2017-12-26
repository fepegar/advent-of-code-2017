#include <stdio.h>

int main() {
  int a = 1;
  int b, c, d, e, f, g;
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
        g = d * e;  // 13 set g e
        g = g - b;  // 14 sub g b
        if (g == 0) {  // 15 jnz g 2
          f = 0;  // 16 set f 0
        }
        e += 1;  // 17 sub e -1
        g = e - b;  // 19 sub g b
      } while(g != 0);  // 20 jnz g -8
      d += 1;  // 21 sub d -1
      g = d - b;  // 23 sub g b
    } while(g != 0);  // 24 jnz g -13
    if (f == 0) {  // 25 jnz f 2
      h += 1;  // 26 sub h -1
    }
    g = b - c;  // 28 sub g c
    if (g == 0) {  // 29 jnz g 2
      break;  // 30 jnz 1 3
    }
    b += 17;  // 31 sub b -17
  } while(1);  // 32 jnz 1 -23

  printf("h: %d\n", h);
  return 0;
}
