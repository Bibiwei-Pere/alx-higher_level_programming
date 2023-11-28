#include "lists.h"
/**
 * check_cycle - checks whether a list cycles or not
 * @list: singly linked list
 * Return: 0 No Cycling 1 Cycling
 */
int check_cycle(listint_t *list)
{
listint_t *curr = NULL, *tmp = NULL;
if (list == NULL)
return (0);
curr = list;
tmp = list->next;
while (tmp != NULL && tmp->next != NULL)
{
if (tmp == curr)
return (1);
curr = curr->next;
tmp = (tmp->next)->next;
}
return (0);
}
