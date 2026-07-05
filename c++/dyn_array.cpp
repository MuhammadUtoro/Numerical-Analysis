#include <iostream>

int main() {

  // Practicing dynamic array
  int arrSize;
  std::cout << "Enter array length: " << std::endl; 
  std::cin >> arrSize;
  
  int stepSize;
  std::cout << "Enter step size: " << std::endl;
  std::cin >> stepSize;

  double* array1 = new double[arrSize];
  double* array2 = new double[arrSize];
  
  // Initialise Array
  for (int i=0; i<arrSize; i++) {
    array1[i] = i;
    array2[i] = 0;
  }

  // Check
  std::cout << "Array 1: ";
  for (int i=0; i<arrSize; i++) {
    std::cout << array1[i] << " ";
  }

  std::cout << "Array 2: ";
  for (int i=0; i<arrSize; i++) {
    std::cout << array2[i] << " ";
  }

  // Create pointers for swapping values
  double* tempArr1 = array1;
  double* tempArr2 = array2;

  // Time-stepping loop
  for(int t=0; t<stepSize; t++) {
    for(int i=1; i<arrSize-1; i++) {
      tempArr2[i] = (tempArr1[i-1] - 2*(tempArr1[i]) + tempArr1[i+1])/2;
      }

      std::cout << "\ntempArr1: "; 
      for(int i=0; i<arrSize; i++) {
        std::cout << tempArr1[i] << " ";
      }
      std::cout << "\ntempArr2: ";
      for(int i=0; i<arrSize; i++) {
        std::cout << tempArr2[i] << " ";
      }
    // Swap pointer
    double* tempVar = array1;
    tempArr1 = tempArr2;
    tempArr2 = tempVar;
  }

  // Free memory
  delete [] array1;
  delete [] array2;

  return 0;
}
