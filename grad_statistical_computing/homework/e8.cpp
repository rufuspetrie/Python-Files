
#include <iostream>
#include <fstream>
#include <armadillo>
using std::cout;
using std::ofstream;

int main(){
    // Armadillo library
    using namespace arma;
    
    // Generate vectors
    vec x = linspace<vec>(10.0, 15.0, 10);
    vec e = 10*randn<vec>(10);
    vec y = 3*5%x - 7*x + 2 + e;
    
    // Print x/y vectors
    cout << "Here are the x values: \n" << x << "\n";
    cout << "Here are the y values: \n" << y << "\n";
    
    // Lengths and Euclidean Distance
    cout << "Length of x: " << norm(x) << "\n";
    cout << "Length of y: " << norm(y) << "\n";
    cout << "Distance between x and y: " << norm(x -y) << "\n";

    // Correlation
    cout << "Correlation of x and y: " << cor(x,y) << "\n";
    
    // Solve linear system for quadratic fit
    mat A = join_rows(ones<vec(10), x);
    A = join_rows(A, x%x);
    cout << "Here is the data matrix: " << A << "\n";
    vec b = solve(A, y);
    cout << "Here is the beta value: " << b << "\n";
}
