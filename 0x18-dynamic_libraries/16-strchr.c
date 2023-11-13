#include "main.h"
#include <stddef.h>
/**
 * _strchr - sets char
 * @s: char to set
 * @c: char
 * Return: char destination
 */
char *_strchr(char *s, char c)
{
    while (*s != '\0')
    {
        if (*s == c)
        {
            return (s);
        }
        s++;
    }
    if (*s == c)
    {
        return (s);
    }
    return (NULL);
}