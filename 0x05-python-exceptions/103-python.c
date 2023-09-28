#include <Python.h>
#include <string.h>

/**
 * print_python_list - Function to print some information of a
 * python list object from C.
 * @p: A PyObject pointer
 *
 * Return: void.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *type;
	PyObject *item;

	printf("[*] Python List info\n");

	if (PyList_Check(p) != 1)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	alloc = ((PyListObject *)(p))->allocated;
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = (((PyListObject *)(p))->ob_item)[i];
		type = item->ob_type->tp_name;
		printf("Element %lu: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(type, "float") == 0)
			print_python_float(item);
	}

}

/**
 * print_python_bytes - Function to print information about 
 * Bytes object.
 * @p: A PyObject pointer
 *
 * Return: Void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, print_size, i;
	char *unicode_str;
	PyObject *unicode_obj;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) != 1)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %lu\n", size);
	unicode_obj = PyUnicode_FromEncodedObject(p, "utf-8", "strict");
	unicode_str = PyUnicode_AsUTF8(unicode_obj);
	printf("  trying string: %s\n", unicode_str);
	if (size + 1 >= 10)
		print_size = 10;
	else
		print_size = size + 1;
	printf("  first %lu bytes:", print_size);
	for (i = 0; i < print_size; i++)
	{
		printf(" %02x", unicode_str[i]);
		if (unicode_str[i] == '\0')
			break;
	}
	printf("\n");

}
