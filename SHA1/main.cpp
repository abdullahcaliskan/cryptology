#include <iostream>
#include "sha1.hpp"
#include <string>
using namespace std;
 
int main(int argc, char *argv[])
{
	string plainText = "GNU";
	if (argc > 1)
		plainText = string(argv[1]);

    cout << "sha1('"<< plainText <<"'):" << sha1(plainText) << endl;
    return 0;
}