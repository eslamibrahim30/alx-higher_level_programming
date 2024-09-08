#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
	PyObject *obj = NULL;
	unsigned char *byte = NULL;
	long int i = 0;
	long int size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	obj = PyBytes_FromObject(p);
	size = PyBytes_Size(obj);
	byte = (unsigned char *)obj + 32;
	printf("  size: %li\n", size);
	printf("  trying string: ");
	while (*byte != '\0')
	{
		printf("%c", *byte);
		byte++;
	}
	printf("\n");
	byte = (unsigned char *)obj + 32;
	i = (size + 1 > 10 ? 10 : size + 1);
	printf("  first %li bytes: ", i);
	printf("%02x", (int)*byte);
	i--;
	while (i != 0)
	{
		printf(" %02x", (int)*byte);
		byte++;
		i--;
	}
	printf("\n");
}

void print_python_list(PyObject *p)
{
	Py_ssize_t length = 0;
	Py_ssize_t allocated = 0;
	Py_ssize_t i = 0;
	PyObject *obj = NULL;
	const char *type = NULL;

	if (PyList_Check(p) == 0)
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	length = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", length);
	printf("[*] Allocated = %lu\n", allocated);
	for (i = 0; i < length; i++)
	{
		obj = PyList_GET_ITEM(p, i);
		type = (((PyObject *)(obj))->ob_type)->tp_name;
		printf("Element %li: %s\n", i, type);
		if (PyBytes_Check(obj) == 1)
			print_python_bytes(obj);
	}
}
