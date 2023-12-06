#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list object.
 */

void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *type;

	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}

}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: PyObject byte object.
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, size;

	PyBytesObject *bytes = NULL;
	PyVarObject *var = (PyVarObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;

	printf("  size: %ld\n", var->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (var->ob_size > 10)
		size = 10;
	else
		size = var->ob_size + 1;

	printf("  first %d bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", *(bytes->ob_sval + i));
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
