#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if singly link has cycle or not
 * @list: list of singly linked
 *
 * Return: if there is cycle - 1,0 otherwise
 *
*/
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	/*If the list is empty, then there is no cycle.*/
	if (list == NULL || list->next == NULL)
		return (0);
	/*Move the two pointers through the list.*/
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		/*If the two pointers ever meet, then there is a cycle.*/
		if (slow_ptr == fast_ptr)
			return (1);
	}
	/*If the fast pointer reaches the end of the list, then there is no cycle.*/
	if (fast_ptr == NULL)
		return (0);
	/*Otherwise, there must be a cycle in the list.*/
	return (1);
}
