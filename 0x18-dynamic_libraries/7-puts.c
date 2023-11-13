#include "main.h"

/**
 * _puts - Solve me
 * @str: character
 * Return: noting
 */
void _puts(char *str)
{
    int n = 0;
    while (str[n] != '\0')
    {
        _putchar(str[n]);
        n++;
    }
    _putchar('\n');
}