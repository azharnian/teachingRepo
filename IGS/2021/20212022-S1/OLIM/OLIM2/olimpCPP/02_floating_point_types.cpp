#include <cstdio>


int main(){
	// float, double, long double
	float a = 0.1f; //suffix f/F
	double b = 0.2;
	long double c = 0.3L;//suffix l/L

	double plancks_const = 6.62607004e-34;
	printf("Placnks : %e\n", plancks_const);
	printf("%f %f %Lf\n", a, b, c);
	printf("%e %e %Le\n", a, b, c);
	printf("%g %g %Lg\n", a, b, c);
}