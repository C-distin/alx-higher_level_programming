#include "lists.h"

/**
 * reverse_listint - reverses a singly-linked list
 * 
 * @head: head list
 * 
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		listint_t *next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

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
	listint_t *reverse = NULL;
	listint_t *temp = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	reverse = reverse_listint(head);
	temp = reverse;

	while (current != NULL)
	{
		if (current->n != temp->n)
			return (0);
		current = current->next;
		temp = temp->next;
	}
	return (1);
}
