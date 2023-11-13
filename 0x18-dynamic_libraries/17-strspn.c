#include "main.h"

/**
 * _strspn - sets char
 * @s: char to set
 * @accept: char
 * Return: counter
 */
unsigned int _strspn(char *s, char *accept)
{
    int count = 0;
    int i, j;
    for (i = 0; s[i] != '\0'; i++)
    {
        bool match = false;
        for (j = 0; accept[j] != '\0'; j++)
        {
            if (s[i] == accept[j])
            {
                match = true;
                break;
            }
        }
        if (!match)
            break;
        else
            count++;
    }
    return (count);
}