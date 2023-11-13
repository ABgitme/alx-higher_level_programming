#include "main.h"

/**
 * _abs - that prints signs
 * @n: value to be checked
 *
 * Return: 1 if n is greater than zero. 0 if n is zero.-1 n is less than zero
 */
int _abs(int n)
{
	if (n < 0)
	{
		return (-n);
	}
	else
	{
		return (n);
	}
}