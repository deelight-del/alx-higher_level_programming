#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_dlistint - Function to print the values and return count of
 * a doubly linked list
 * @h: head pointer to the node
 *
 * Return: The size of the nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *temp;
	size_t count;

	if (h == NULL)
		return (0);

	count = 1;
	for (temp = h; temp->next != NULL; temp = temp->next)
	{
		count++;
		printf("%d\n", temp->n);
	}
	printf("%d\n", temp->n);
	return (count);
}
