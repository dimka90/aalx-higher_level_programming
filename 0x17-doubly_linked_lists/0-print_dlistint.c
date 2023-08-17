#include "lists.h"
/**
* print_dlistint - prints all the elements of a dlistint_t list.
* @h: a struct pointer to the list
*
* Return: Number of element in a list
*/
size_t print_dlistint(const dlistint_t *h)
{

const dlistint_t *tempt = h;
size_t count = 0;
if (h == NULL)
{
return (NULL);
}
while (tempt != NULL)
{
printf("%d\n", tempt->n);
tempt = tempt->next;
count++;
}
return (count);
}
