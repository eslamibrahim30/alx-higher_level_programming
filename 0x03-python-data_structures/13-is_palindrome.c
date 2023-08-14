#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: a pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr_f = NULL;
	listint_t *ptr_l = NULL;
	int len = 0;
	int idx = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	ptr_f = *head;
	ptr_l = *head;
	while (ptr_l->next != NULL)
	{
		ptr_l = ptr_l->next;
		len++;
	}
	while (ptr_f != ptr_l)
	{
		if (ptr_f->n != ptr_l->n)
			return (0);
		if (ptr_f->next == ptr_l)
			break;
		ptr_f = ptr_f->next;
		len--;
		idx = 0;
		ptr_l = *head;
		while (idx != len)
		{
			ptr_l = ptr_l->next;
			idx++;
		}
	}
	return (1);
}
