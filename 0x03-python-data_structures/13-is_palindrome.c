#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * len_of_ll - Function that calculates the length of a ll
 * @head: The head pointer of the listint
 *
 * Return: An integer, the length of the ll
 */

int len_of_ll(listint_t *head)
{
	int i;
	listint_t *track;

	if (head == NULL)
		return (0);
	track = head;
	for (i = 1; track->next != NULL; i++)
		track = track->next;
	return (i);
}

/**
 * create_array - Fucntion to create array from ll
 * @head: head pointer of the ll
 *
 * Return: An int pointer (a.k.a array of ints)
 */

int *create_array(listint_t *head)
{
	int i, len, *array;
	listint_t *track = head;

	len = len_of_ll(head);
	if (len == 0)
		return (NULL);
	array = malloc(sizeof(int) * len);
	if (array == NULL)
		return (NULL);
	for (i = 0; i < len; i++)
	{
		array[i] = track->n;
		track = track->next;
	}
	return (array);
}

/**
 * is_palindrome - Function to check if a given LL is palindrome or not
 * @head: head pointer to ll
 *
 * Return: an integer; 1 is a palindrom, 0 is not palindrome
 */

int is_palindrome(listint_t **head)
{
	int *array;
	int i = 0, j, k, len, half;

	if (head == NULL || (*head) == NULL)
		return (1);
	array = create_array((*head));
	len = len_of_ll((*head));
	if (len % 2)
		half = len / 2;
	else
		half = (len / 2) + 1;
	j = len - 1;
	for (k = 0; k <= half - 1; k++)
	{
		if (array[i] != array[j])
			return (0);
		i++;
		j--;
	}
	return (1);
}
