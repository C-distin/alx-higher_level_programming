#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 *
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int i;
	int size;

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %lu\n", (unsigned long)p->ob_item);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 *
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	int i;
	int size;

	size = PyBytes_Size(p);

	printf("[*] Size of the Python Byte String = %d\n", size);
	printf("[*] Allocated = %lu\n", (unsigned long)p->ob_item);
	
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %d\n", i, PyBytes_AS_STRING(p)[i]);
	}
}
