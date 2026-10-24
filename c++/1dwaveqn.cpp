// Practicing 1D wave equation - We use central scheme for both temporal and
// spatial meshes

#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

int main() {
  // Define parameters
  int num = 100; // number of spatial mesh
  double L = 1.0; // length of the string
  double c = 1.0; // speed of the wave
  double dx = L / num; // distance between spatial mesh
  double dt = 0.000024; // temporal mesh
  
  double tmax = 2.0;
  int steps = static_cast<int>(tmax/dt); // time-step
  double r = (c*dt)/dx;

  // Create dynamic array to store the solution
  std::vector<double> u_prev(num+1, 0.0);
  std::vector<double> u(num+1, 0.0);
  std::vector<double> u_new(num+1, 0.0);

  // Apply BCs. We need u(0,t) & u(L,t) = 0
  // Since wave equation is 2nd order in time, then we need two ICs. u(x,0) or
  // the initial displacement and u_t(x,0) or the initial velocity
  // Initial displacement
  for (int i = 0; i<num; i++) {
    double x = i*dx;
    u_prev[i] = std::sin(M_PI * x/L);
  }

  // Fixed endpoints
  u_prev[0] = 0.0;
  u_prev[num] = 0.0;

  // Initial velocity 
  std::vector<double> v(num+1, 50);
  
  // Calculate the first step
  u[0] = 0.0;
  u[num] = 0.0;

  int save_every = steps/7;

  for (int i = 1; i<num; i++) {
   u[i] = u_prev[i] + dt*v[i] + 0.5 * r * r * (u_prev[i+1] - 2.0*u_prev[i] + u_prev[i-1]);
  }

  // Calculate the main time steps
  for (int n = 1; n<steps; n++) {
    // Enforce BCs
    u_new[0] = 0.0;
    u_new[num] = 0.0;

    for (int i = 1; i<num; i++) {
      u_new[i] = 2.0 * u[i] - u_prev[i] + r * r * (u[i+1] - 2*u[i] +u[i-1]);
    }

    std::swap(u_prev, u);
    std::swap(u, u_new);

    if (n % save_every == 0 || n == steps-1) {
      std::ofstream fout("1dwaveqn.dat");
      fout << "# t = " << n*dt << "\n";
      for (int i = 0; i < num; i++) {
        fout << i*dx << " " << u[i] << "\n";
      }
      fout << "\n";
      fout.close();
    }
  }

  // Final displacement
  for (int i = 0; i<=num; i++) {
    std::cout << i*dx << " " << u[i] << "\n";
  }
  return 0;
}
