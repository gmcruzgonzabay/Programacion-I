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
   
   
   cout << "===============================" << endl;
   cout << "        Mi Primer Programa     " << endl;
   cout << "===============================" << endl;

   
   
   cout<< " Ingrese nombre:"; // muestro datos en pantall
   cin >> nombre; // capturo datos del teclado
   
   cout << "Ingrese su edad:";
   cin >> edad;
   
   
   int anioNacimiento= 2026-edad;
   
   
   cout << endl;

   
   cout << "Hola " << nombre << endl;
   cout <<  "Tienes " << edad << " anios "<< endl;
   cout << "Naciste aproximadamente en " << anioNacimiento << endl;
   
   
   
   

    return 0; // el programa terminó corectamente
}