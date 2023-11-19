#include "lists.h"


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;
	int i = 0;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current_node = *head;
	while (current_node->next != NULL)
	{
		if (i == 4)
		{
			new_node->next = current_node->next;
            current_node->next = new_node;
            break;
        }
		i++;
		current_node = current_node->next;
	}

	return (new_node);
}
