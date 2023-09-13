#include <Python.h>
#include <string.h>

/**
 * print_python_list - Function that prints information about python lists
 * @p: PyObject pointer
 *
 * Return: void
 */

void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;
	const char *type;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", size);
	alloc = ((PyListObject *)(p))->allocated;
	printf("[*] Allocated = %lu\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = (((PyListObject *)(p))->ob_item)[i];
		type = item->ob_type->tp_name;
		printf("Element %lu: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}

}

/**
 * print_python_bytes - Function to print information about the PytypeObject
 * @p: An PyObject
 *
 * Return: Void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *buffer;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		size = PyBytes_Size(p);
		printf("  size: %lu\n", size);
		buffer = PyBytes_AsString(p);
		printf("  trying string: %s\n", buffer);
	}
}
