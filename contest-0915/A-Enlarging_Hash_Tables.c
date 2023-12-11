// I used chatgpt to translate my Python code to C because a python compilation error was occurring

#include <stdio.h>
#include <math.h>

// Check if a number is prime using the tips of the class
int is_prime_optimized(int number)
{
    if (number < 2)
        return 0;

    for (int i = 2; i <= (int)sqrt(number); i++)
    {
        if (number % i == 0)
            return 0;
    }

    return 1;
}

int main()
{
    int n;
    scanf("%d", &n);

    while (n != 0)
    {
        int aux_number = 2 * n + 1;

        if (aux_number % 2 == 0)
            aux_number += 1;

        // Search for the first prime number greater than 2*n
        while (!is_prime_optimized(aux_number))
        {
            aux_number += 2;
        }

        if (!is_prime_optimized(n))
            printf("%d (%d is not prime)\n", aux_number, n);
        else
            printf("%d\n", aux_number);

        scanf("%d", &n);
    }

    return 0;
}