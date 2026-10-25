// Now we are trying to use central scheme for the same 1D linear advection
// equation and observe the behaviour
//
#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

int main() {
  // Define Parameters - same as the FTBS
  int num = 100;
  double L = 1.0;
  double dx = 0.01;
  double dt = 0.02;
  double c = 0.5;
  double K = (c*dt/dx);
  double tMax = 0.3;
  int steps = static_cast<int>(tMax/dt);

  // Array to store values
  std::vector<double> u_prev(num+1, 0.0);
  std::vector<double> u(num+1, 0.0);
  std::vector<double> u_new(num+1, 0.0);

  // ICs
  for (int i = 0; i<=num; i++) {
    double x = x = i*dx;
    // Gaussian Pole
    u_prev[i] = std::exp(-100.0*(x-0.3)*(x-0.3));
    // Sin(x)
    // u_prev[i] = std::sin(M_PI * x/L);
  }

  // BCs
  u[0] = 0.0;
  u[num] = 0.0;

  // Initialization formula
  for (int i = 1; i<num; i++) {
    u[i] = u_prev[i] - 0.5*K*(u_prev[i+1] - u_prev[i-1]);
  }

  // Update equation - main loop
  for (int n = 1; n<steps; n++) {
    // Enforce BCs
    u_new[0] = 0.0;
    u_new[num] = 0.0;

    for (int i = 1; i<num; i++) {
      u_new[i] = u_prev[i] - K*(u[i+1] - u[i-1]);
    }

    std::swap(u_prev, u);
    std::swap(u_prev, u_new);
    
    // Print to plot
    std::ofstream fout("1d_advection_central.dat");
    fout << "# t = " << n*dt << "\n";
    for (int i = 0; i<num; i++) {
      fout << i*dx << " " << u[i] << "\n";
    }
    fout << "\n";
    fout.close();
  }
}
