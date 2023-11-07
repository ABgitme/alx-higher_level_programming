
/**
 * is_palindrome - checks if the singly linked
 *              list pointed to by head is a palindrome
 * @head: pointer to a pointer to the
 *          head node of the singly linked list to be checked.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
	list_node_t *reversed_head = NULL, *original_node,
		    *reversed_node, *new_node, *current_node;
	/*If the list is empty, it is a palindrome.*/
	if (*head == NULL)
		return (1);
	/*Reverse the list*/
	current_node = *head;
	while (current_node != NULL)
	{
		new_node = malloc(sizeof(list_node_t));
		new_node->data = current_node->data;
		new_node->next = reversed_head;
		reversed_head = new_node;
		current_node = current_node->next;
	}
	/*Compare the original list to the reversed list.*/
	original_node = *head;
	reversed_node = reversed_head;
	while (original_node != NULL && reversed_node != NULL)
	{
		if (original_node->data != reversed_node->data)
		{
			/*The lists are not palindromes.*/
			return (0);
		}
		original_node = original_node->next;
		reversed_node = reversed_node->next;
	}
	/*The lists are palindromes.*/
	return (1);
}
