#include "main.h"
/**
 * _strncat - a function that copies the string pointed to by src,
 * @dest: the string to concatenate
 * @src: the string from concatenate
 * @n: the number of bytes to copy
 * Return: pointer to dest
 */
char *_strncat(char *dest, char *src, int n)
{
    int i;
    int j;
    for (i = 0; dest[i] != '\0'; i++)
    {
    }
    for (j = 0; src[j] != src[n]; j++, i++)
    {
        dest[i] = src[j];
    }
    dest[i] = '\0';
    return (dest);
}