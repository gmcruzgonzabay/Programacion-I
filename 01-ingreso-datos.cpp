/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
   
   string nombre; // declaracion de variables
   int edad; // Es sensible a mayusculas y min, string es con min.
   
   string apellido;
   
   cout<< " Ingrese nombre:"; // muestro datos en pantall
   cin >> nombre; // capturo datos del teclado
   
   cout << "Ingrese su edad:";
   cin >> edad;
   
   cout << endl;
   
   cout << "Hola " << nombre << " tienes " << edad << " anios" << endl;
   
   
   

    return 0; // el programa terminó corectamente
}