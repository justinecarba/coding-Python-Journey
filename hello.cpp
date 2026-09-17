
// hello.cpp - basic C++ example
#include <iostream>
#include <string>

// simple function that returns greeting
std::string make_greeting(const std::string &justine)
{
    return "Hello, " + name + "!";
}

int main()
{
    // variables
    std::string name;
    int repeat = 1;

    // prompt user
    std::cout << "Enter your name: ";
    if (!std::getline(std::cin, name) || name.empty())
    {
        name = "World"; // default
    }

    std::cout << "How many times to repeat (1-5): ";
    if (!(std::cin >> repeat) || repeat < 1)
        repeat = 1;
    if (repeat > 5)
        repeat = 5;

    // output using loop
    for (int i = 0; i < repeat; ++i)
    {
        std::cout << make_greeting(name) << "\n";
    }

    return 0;
}
