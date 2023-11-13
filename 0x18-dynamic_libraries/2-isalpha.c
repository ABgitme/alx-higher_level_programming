#include "main.h"
/**
 * _isalpha - letter, lowercase or uppercase
 * @c: The char to be checked
 *
 * Return: 1 if the char is lowercase. 0 otherwise
 */
int _isalpha(int c)
{
if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
return (1);
else
return (0);
}