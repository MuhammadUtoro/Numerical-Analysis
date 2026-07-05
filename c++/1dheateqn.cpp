#include <iostream>
#include <vector>
#include <fstream>

// Practicing 1D Heat Equation - Using pointer to update value

int main() {

  // Define the parameters
  int num = 101; // Number of mesh
  double L = 1.0; // Length of the bar
  double alpha = 0.2; // Thermal diffusivity
  double dx = L / (num-1);
  double dt = 0.00024;
  double c = (alpha*dt)/(dx*dx);

  double tmax = 2.0;
  int steps = static_cast<int>(tmax/dt);

  // Create arrays for saving the solution
  std::vector<double> u(num, 0.0);
  std::vector<double> u_new(num, 0.0);

  // Create pointers to swap value
  std::vector<double>* curr = &u;
  std::vector<double>* next = &u_new;

  // Apply BCs
  (*curr)[0] = 0.0;
  (*curr)[num-1] = 100.0;

  int save_every = steps/7;

  std::ofstream fout("1dheateqn.dat"); // Overwrite
  fout.close();

  // Comes the main loop
  for (int n=0; n < steps; n++) {
    for (int i=1; i < num-1; i++) {
        (*next)[i] = (*curr)[i] + c * ((*curr)[i+1] - 2*(*curr)[i] + (*curr)[i-1]);
    }

    // Reapply BCs
    (*next)[0] = 0.0;
    (*next)[num-1] = 100.0;

    // Swap pointers
    std::swap(curr, next);

    // Saving snapshots
    if (n % save_every == 0 || n == steps-1) {
      std::ofstream fout("1dheateqn.dat");
      fout << "# t = " << n*dt << "\n";
      for (int i=0; i < num; i++) {
        fout << i*dx << " " << (*curr)[i] << "\n";
      }
      fout << "\n";
      fout.close();
    }
  }

  std::cout << "Simulation Done!" << std::endl;

  return 0;
}
