
#include <iostream>
#include <fstream>
#include <functional>
#include <random>
using namespace std;

default_random_engine re{12345};
normal_distribution<double> norm(100, 15);
auto rnorm = bind(norm, re);

int main() {
    ofstream fout("norm_data.txt");
    for (int i=0; i<100; i++) {
        fout << rnorm() << "\n";
    }
}
