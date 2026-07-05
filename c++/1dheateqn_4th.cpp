// We practice to solve the 1D heat equation using 4th order accuracy central
// scheme

#include <iostream>
#include <fstream>
#include <vector>

int main() {
  // We define the constants, ICs and Bcs
  int num_mesh; // number of spatial mesh
  double tend; // maximum time
  double dt; // time-step or interval
  double dx; // distance between two spatial mesh
  double alpha; // thermal diffusivity
  double c; // (alpha*dt)*(dx)^2
  double L; // length of the bar

  // We set the value
  alpha = 0.3;
  num_mesh = 101;
  L = 1.0;
  dx = L/(num_mesh - 1);
  dt = 0.000024;
  c = (alpha*dt)/(12*dx*dx);
  tend = 2.0;
  int steps = static_cast<int>(tend/dt);

  // Create arrays for saving the value
  std::vector<double> u(num_mesh, 0.0);
  std::vector<double> u_new(num_mesh, 0.0);

  // Create pointers to swap value
  std::vector<double>* curr = &u;
  std::vector<double>* next = &u_new;

  // Apply BCs
  (*curr)[0] = 0.0;
  (*curr)[1] = 0.0;
  (*curr)[num_mesh-1] = 100.0;
  (*curr)[num_mesh-2] = 100.0;

  int save_every = steps/7;
  
  std::ofstream fout("1d_heateqn_4th.dat"); // Overwrite
  fout.close();

  // Loop
  for (int n=0; n<steps; n++) {
    for (int i=2; i<num_mesh-2; i++){
      (*next)[i] = (*curr)[i] + c * (
          - (*curr)[i+2] + 16*(*curr)[i+1] - 30*(*curr)[i] + 16*(*curr)[i-1] - (*curr)[i-2]
          );
    }

    // reapply BCs
    (*next)[0] = 0.0;
    (*next)[1] = 0.0;
    (*next)[num_mesh-1] = 100.0;
    (*next)[num_mesh-2] = 100.0;

    // swap pointers
    std::swap(curr, next);

    // saving snapshots
    if (n % save_every == 0 || n == steps-1) {
      std::ofstream fout("1d_heateqn_4th.dat", std::ios::app);
      fout << "# t = " << n*dt << "\n";
      for (int i=0; i<num_mesh; i++) {
        fout << i*dx << " " << (*curr)[i] << "\n";
      }
      fout << "\n";
      fout.close();
    }
  }
  std::cout << "Simulation done!" << std::endl; 
}
