#include "main.h"
/**
 * _memcpy - sets char
 * @dest: char to set
 * @src: char
 * @n: number of bytes to print
 * Return: char destination
 */
char *_memcpy(char *dest, char *src, unsigned int n)
{
    unsigned int i;
    char *ch_dest = (char *)dest;
    char *ch_src = (char *)src;
    for (i = 0; i < n; i++)
    {
        ch_dest[i] = ch_src[i];
    }
    return (dest);
}