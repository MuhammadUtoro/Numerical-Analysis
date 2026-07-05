#include <cstdio>
#include <iostream>
#include <cstdlib>

int main() {
  FILE *pipe = popen("gnuplot -persist", "w");

  if(!pipe) {
    perror("popen failed!");
    return 1;
  }

  fprintf(pipe, "set terminal 'x11'\n");
  fprintf(pipe, "set title 'Sine Function'\n");
  fprintf(pipe, "set grid\n");
  fprintf(pipe, "plot sin(x)\n");
  fflush(pipe);

  pclose(pipe);

  return 0;
}
