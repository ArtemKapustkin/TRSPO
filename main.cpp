#include<thread>
#include<iostream>
#include<chrono>

using namespace std;

void f1(int a, int b)
{
	int c = a + b;
	cout << "Function 1 result - " << c << endl;
}

void f2(int a, int b, int n)
{
	this_thread::sleep_for(chrono::seconds(n)); // затримка зроблена задля запобігання накладанню виведення функцій
	int c = a * b;
	cout << "Function 2 result - " << c << endl;
}

int main()
{
	thread thread1(f1, 100, 100);
	thread thread2(f2, 100, 100, 1);

	cout << "Now functions are executing parallel.." << endl;

	thread1.join();
	thread2.join();

	cout << "Both functions completed." << endl;

	return 0;
}