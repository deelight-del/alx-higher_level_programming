#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <stddef.h>

/**
 * print_python_list_info - Function to print information about python list
 * @p: Pointer to PyObject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i, size, mem_alloc;
	PyObject *element;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	mem_alloc = ((PyListObject *)(p))->allocated;
	printf("[*] Allocated = %d\n", mem_alloc);
	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
