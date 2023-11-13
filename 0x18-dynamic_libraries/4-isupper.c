#include "main.h"
#include <ctype.h>
/**
 * _isupper- check the code.
 * @c: value check
 * Return: 1 if c is uppercase
 */
int _isupper(int c)
{
    char uppercase = 'A';
    int isupper = 0;
    for (; uppercase <= 'Z'; uppercase++)
    {
        if (c == uppercase)
        {
            isupper = 1;
            break;
        }
    }
    return (isupper);
}