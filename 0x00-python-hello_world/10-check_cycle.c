#include <stdlib.h>
#include <lists.h>

/**
 * check_cycle - checks if singly link has cycle or not
 * @list: list of singly linked
 *
 * Return: if there is cycle - 1,0 otherwise
 *
*/
int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    if (fast && fast->next)
        return (0);
    slow = list->next;
    fast = list->next->next;

    while (slow && fast && fast->next)
    {
        if (slow == fast)
            return (1);
        slow = slow->next;
        fast = fast->next->next;
    }
    return (0);
}