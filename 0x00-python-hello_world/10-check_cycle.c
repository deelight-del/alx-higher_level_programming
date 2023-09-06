#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Function to chexk if LL has a loop
 * @list: pointer to linked list (head pointer)
 *
 * Return: An integer to depict success or failure
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL
			|| list->next->next == NULL)
		return (0);

	slow = fast = list;
	slow = slow->next;
	fast = fast->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
