#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: a pointer to the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr_slow = NULL;
	listint_t *ptr_fast = NULL;

	if (list == NULL)
		return (0);
	ptr_slow = list;
	ptr_fast = ptr_slow->next;
	while (ptr_slow != NULL && ptr_fast != NULL)
	{
		ptr_slow = ptr_slow->next;
		ptr_fast = ptr_fast->next;
		if (ptr_fast == NULL)
			return (0);
		ptr_fast = ptr_fast->next;
		if (ptr_slow == ptr_fast)
			return (1);
	}
	return (0);
}
