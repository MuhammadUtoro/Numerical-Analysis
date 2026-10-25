// This practices the 1D wave unidirectional 1D wave equation
// It is also called 1D linear advention equatio
// I tried to solve it with FTBS scheme (forward in time, backward in space)
// The equation itself: U_t = -c*U_x or U_t + c*U_x = 0
#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

int main() {
  // Define parameters
  int num = 100;
  double L = 1.0;
  double dx = 0.01;
  double dt = 0.005;
  double c = 0.5;
  double K = (c*dt/dx);
  double tMax = 0.5;
  int steps = static_cast<int>(tMax/dt);

  // Array to store values
  std::vector<double> u(num+1, 0.0);
  std::vector<double> u_new(num+1, 0.0);

  // ICs
  for (int i = 0; i<num; i++) {
    double x = i*dx;
    // Gaussian Pole
    u[i] = 2 * std::exp(-100.0*(x-0.3)*(x-0.3));
    // Sin(x)
    // u[i] = std::sin(M_PI * x/L);
  }

  // BCs
  u[0] = 0.0;
  u[num] = 0.0;

  // Update formula
  for (int n = 1; n<steps; n++) {
    // Enforce BCs

    for (int i = 1; i<num; i++) {
      u_new[i] = u[i] -K * (u[i] - u[i-1]);
    }

    std::swap(u, u_new);

    // Print to plot
    std::ofstream fout("1d_advection_FTBS.dat");
    fout << "# t = " << n*dt << "\n";
    for (int i = 0; i<num; i++) {
      fout << i*dx << " " << u[i] << "\n";
    }
    fout <<"\n";
    fout.close();
  }
}
