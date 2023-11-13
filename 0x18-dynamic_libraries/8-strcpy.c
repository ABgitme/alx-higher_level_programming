#include "main.h"
/**
 * _strcpy - a function that copies the string pointed to by src,
 * including the terminating null byte (\0),
 * to the buffer pointed to by dest.
 *
 * @dest: A pointer to destination of string
 * @src: A pointer to source string to copy from
 *
 * Return: pointer to dest
 */
char *_strcpy(char *dest, char *src)
{
    int j;
    for (j = 0; src[j] != '\0'; j++)
    {
        dest[j] = src[j];
    }
    dest[j++] = '\0';
    return (dest);
}