#include "lists.h"
#include <stdlib.h>


/**
 * list_len - Calculates the length of a given non-looping singly linked list.
 * @head: a pointer to the head of the linked list.
 *
 * Return: the length of a given singly linked list.
 */
int list_len(listint_t *head)
{
	int len = 0;
	listint_t *ptr = head;

	while (ptr != NULL)
	{
		ptr = ptr->next;
		len++;
	}
	return (len);
}

/**
 * get_middle - Returns a pointer to the middle node of a given
 * non-looping singly linked list.
 * @head: a pointer to the head of the linked list.
 * @len: the length of the linked list.
 *
 * Return: a pointer to the middle node of the list.
 */
listint_t *get_middle(listint_t *head, int len)
{
	int mid_idx = 0;
	int i = 0;
	listint_t *ptr = head;

	mid_idx = (len / 2) + (len % 2) - 1;
	for (i = 0; i <= mid_idx; i++)
		ptr = ptr->next;
	return (ptr);
}

/**
 * reverse_list - Reverses a singly linked list.
 * @head: a pointer to the head of the linked list.
 *
 * Return: a pointer to the head of the list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *ptr = NULL;
	listint_t *ptr_next = NULL;
	listint_t *temp = NULL;

	if (head == NULL)
		return (NULL);
	ptr = head;
	ptr_next = ptr->next;
	while (ptr_next != NULL)
	{
		temp = ptr_next->next;
		ptr_next->next = ptr;
		ptr = ptr_next;
		ptr_next = temp;
	}
	head->next = NULL;
	return (ptr);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: a pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int is_palindrome_list = 1;
	listint_t *ptr_1 = NULL;
	listint_t *ptr_2 = NULL;
	listint_t *middle = NULL;
	listint_t *reversed_second_half = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	len = list_len(*head);
	middle = get_middle(*head, len);
	reversed_second_half = reverse_list(middle->next);
	middle->next = NULL;
	ptr_1 = *head;
	ptr_2 = reversed_second_half;
	while (ptr_1 != NULL && ptr_2 != NULL)
	{
		if (ptr_1->n != ptr_2->n)
		{
			is_palindrome_list = 0;
			break;
		}
		ptr_1 = ptr_1->next;
		ptr_2 = ptr_2->next;
	}
	middle->next = reverse_list(reversed_second_half);
	return (is_palindrome_list);
}
