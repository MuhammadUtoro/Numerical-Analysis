// Practicing 1D wave equation - We use central scheme for both temporal and
// spatial meshes

#include <iostream>
#include <vector>
#include <fstream>

int main() {
  // Define parameters
  int num = 101; // number of spatial mesh
  double L = 1.0; // length of the string
  double c = 1.0; // speed of the wave
  double dx = L / (num-1); // distance between spatial mesh
  double dt = 0.00024; // temporal mesh
  
  double tmax = 2.0;
  int steps = static_cast<int>(tmax/dt); // time-step

  // Create dynamic array to store the solution
  std::vector<double> u_prev(num, 0.0);
  std::vector<double> u(num, 0.0);
  std::vector<double> u_new(num, 0.0);

  // Apply BCs. We need u(0,t) & u(L,t) = 0
  // Since wave equation is 2nd order in time, then we need two ICs. u(x,0) or
  // the initial displacement and u_t(x,0) or the initial velocity
  u_prev[0] = u_prev[num - 1] = 0.0;
  u[0] = u[num - 1] = 0.0;
  u_new[0] = u_new[num - 1] = 0.0;

}
