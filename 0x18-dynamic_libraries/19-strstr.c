#include "main.h"

/**
 * _strstr - sets char
 * @haystack: char to set
 * @needle: char
 * Return: char
 */
char *_strstr(char *haystack, char *needle)
{
    int n = strlen(needle);
    while (*haystack)
    {
        if (!memcmp(haystack, needle, n))
        {
            return (haystack);
        }
        haystack++;
    }
    return (NULL);
}