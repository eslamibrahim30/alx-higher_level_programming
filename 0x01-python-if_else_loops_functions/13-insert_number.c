#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: a pointer to the head of the list
 * @number: the given number to be added within the new added node.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *ptr_cur;
	listint_t *ptr_next;

	if (head == NULL)
		return (NULL);
	node = (listint_t *)malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}
	ptr_cur = *head;
	if (node->n < ptr_cur->n)
	{
		*head = node;
		node->next = ptr_cur;
		return (node);
	}
	ptr_next = ptr_cur->next;
	while (ptr_next != NULL)
	{
		if (ptr_cur->n <= node->n && ptr_next->n >= node->n)
		{
			ptr_cur->next = node;
			node->next = ptr_next;
			return (node);
		}
		ptr_cur = ptr_cur->next;
		ptr_next = ptr_next->next;
	}
	ptr_cur->next = node;
	node->next = NULL;
	return (node);
}
