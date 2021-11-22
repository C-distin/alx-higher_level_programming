#include <Python.h>

/**
 * print_python_list_info - function that prints basic info about a python list
 * 
 * @p: python list
 * 
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyObject *item;
	int i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	printf("[*] Fill = %ld\n", ((PyListObject *)p)->fill);
	printf("[*] Items:\n");
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("[%ld]\t%s\n", i, Py_TYPE(item)->tp_name);
	}
}
