#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - function that prints basic info about a python list
 * 
 * @p: python list
 * 
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i, j, k;
	PyObject *list;

	if (p == NULL)
	{
		printf("\n");
		return;
	}
	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size: %ld\n", PyList_Size(p));
		printf("[*] Allocated: %ld\n", ((PyListObject *)p)->allocated);
		printf("[*] Objects:\n");
		list = p;
		i = 0;
		while (i < PyList_Size(p))
		{
			printf("Element %d: ", i);
			j = 0;
			while (j < PyList_Size(p))
			{
				printf("[%d] ", j);
				k = 0;
				while (k < PyList_Size(p))
				{
					printf("%d", k);
					k++;
				}
				j++;
			}
			i++;
		}
	}
	else
	{
		printf("Not a list.\n");
	}
}
