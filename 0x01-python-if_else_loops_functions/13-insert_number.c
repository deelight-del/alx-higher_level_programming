#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Function to insert a node in a sorted linked list
 * @head: pointer to the head pointer to the first node
 * @number: number to add to new node
 *
 * Return: address of new node or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *next, *track;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if ((*head) == NULL || head == NULL)
	{
		(*head) = new_node;
		return (new_node);
	}
	if (number < (*head)->n)
	{
		new_node->next = *head;
		(*head) = new_node;
		return (new_node);
	}
	track = (*head);
	while (track->next != NULL)
	{
		if (number > track->n && number < track->next->n)
		{
			printf("add end");
			break;
			next = track->next;
			track->next = new_node;
			new_node->next = next;
			return (new_node);
		}
		track = track->next;
	}

	next = track->next;
	track->next = new_node;
	new_node->next = next;
	return (new_node);
}
