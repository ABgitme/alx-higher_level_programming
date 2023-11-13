#include "main.h"
/**
 * _memset - sets char
 * @s: char to set
 * @b: char
 * @n: number of bytes to print
 * Return: char - print
 */
char *_memset(char *s, char b, unsigned int n)
{
    char *set = s;
    while (n--)
    {
        *s = b;
        s++;
    }
    return (set);
}