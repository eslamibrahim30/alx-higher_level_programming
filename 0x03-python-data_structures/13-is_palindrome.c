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
	listint_t *ptr = NULL;
	int *list_arr = NULL;
	int len = 0;
	int half_len = 0;
	int i = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		len++;
	}
	list_arr = (int *)malloc(len * sizeof(int));
	if (list_arr == NULL)
		return (0);
	ptr = *head;
	i = 0;
	while (ptr != NULL)
	{
		list_arr[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	half_len = len / 2;
	for (i = 0; i <= half_len; i++)
	{
		if (list_arr[i] != list_arr[len - i - 1])
		{
			free(list_arr);
			return (0);
		}
	}
	free(list_arr);
	return (1);
}
