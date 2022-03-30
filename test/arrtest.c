// 3/31 2022 haruki1234
// emcc arrtest.c -o arrtest.js -s WASM=1 -s "EXPORTED_FUNCTIONS=['_main','_add','_img']" --js-library api.js
void print(int num);

int main() {
  return 0;
}

int add(int a,int b) {
  return a+b;
}

void img(unsigned char* iarr,int x,int y) {
  print(sizeof(unsigned char*));
  for (int i=0;i<x*y*4;i++) {
    iarr[i] = 1;
  }
}