#include "main.h"
/**
 * _islower - Check if a char is lowercase
 * @c: The char to be checked
 *
 * Return: 1 if the char is lowercase. 0 otherwise
 */
int _islower(int c)
{
if (c >= 97 && c <= 122)
{
return (1);
}
else
return (0);
}