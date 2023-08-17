#include "lists.h"
/**
* dlistint_len - count all the elements of a dlistint_t list.
* @h: a struct pointer to the list
*
* Return: Number of element in a list
*/
size_t dlistint_len(const dlistint_t *h)
{

const dlistint_t *tempt = h;
size_t count = 0;
if (h == NULL)
{
return (0);
}
while (tempt != NULL)
{
tempt = tempt->next;
count++;
}
return (count);
}
