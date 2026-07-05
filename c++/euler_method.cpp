#include <iostream>
#include <utility>
#include <cmath>
#include <cstdio>

// Practicing Numerical Methods in C++. First try, Euler Methods

// Define the function
double dydx(double x, double y) {
  return 3*x + y;
}

// Define the analytical solution
double exact_sol(double x) {
  return -3*x - 3 + 2*std::exp(x);
}

int main() {

  // Set number of steps and step size
  int N = 100; // number of steps
  double h = 0.01; // step size

  // Create dynamic array
  double* x = new double[N];
  double* y1 = new double[N];
  
  // Define the initial condition
  x[0] = 0;
  y1[0] = -1;

  // The main loop - Euler's Method
  for (int i = 0; i<N-1; i++) {
      x[i+1] = x[i] + h;

      y1[i+1] = y1[i] + h * dydx(x[i], y1[i]);
  }
  
  // Final Result
  for (int i=0; i<N; i++) {
    double y_exact = exact_sol(x[i]);
    double error = std::abs(y_exact - y1[i]);
    std::cout << i << "\t" 
              << x[i] << "\t" 
              << y1[i] << "\t"  
              << y_exact << "\t"
              << error << "\n";
  }
  
  // We use pipe to plot direct from the program
  FILE* pipe = popen("gnuplot -persist", "w");
  if (!pipe) {
    perror("popen failed!");
    return 1;
  }

  // gnuplot commands
  fprintf(pipe, "set terminal 'qt'\n");
  fprintf(pipe, "set title 'Euler vs Exact'\n");
  fprintf(pipe, "set xlabel 'x'\n");
  fprintf(pipe, "set ylabel 'y'\n");
  fprintf(pipe, "set grid\n");
  fprintf(pipe, "plot '-' with linespoints title 'Euler', '-' with lines title 'Exact'\n");
  

  // We send the data to the pipe
  for (int i=0; i<N; i++) {
    fprintf(pipe, "%.2f %.2f\n", x[i], y1[i]);
  }
  fprintf(pipe, "e\n");

  for (int i=0; i<N; i++) {
    fprintf(pipe, "%f %f\n", x[i], exact_sol(x[i]));
  }
  fprintf(pipe, "e\n");

  fflush(pipe);
  pclose(pipe);

  delete[] x;
  delete[] y1;
  
  return 0;
}
