#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

/**
 * is_palindrome - a function that checks if a singly linked
 * list is a palindrome
 * 
 * @head: head list
 * 
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *back = NULL;
	listint_t *front = NULL;
	int count = 0;

	if (!head || !*head)
		return (1);

	while (current)
	{
		count++;
		current = current->next;
	}

	current = *head;
	while (count > 1)
	{
		front = current;
		current = current->next;
		count--;
	}

	while (current)
	{
		if (current->n != front->n)
			return (0);
		current = current->next;
		front = front->next;
	}

	return (1);
}
