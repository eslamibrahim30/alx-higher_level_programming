#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = NULL;
	char *byte = NULL;
	int size = 0;
	int printable = 0;
	int i = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	byte = bytes->ob_sval;
	size = ((PyVarObject *)p)->ob_size;
	printable = (size + 1 < 10 ? size + 1 : 10);
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %d bytes:", printable);
	for (i = 0; i < printable; i++)
		printf(" %02x", (byte[i] & 0xFF));
	printf("\n");
}

void print_python_float(PyObject *p)
{
	double num = 0;
	char *repr = NULL;

	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	num = ((PyFloatObject *)p)->ob_fval;
	repr = PyOS_double_to_string(num, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", repr);
}

void print_python_list(PyObject *p)
{
	PyListObject *list = NULL;
	PyObject *cur = NULL;
	int size = 0;
	int allocated = 0;
	int i = 0;

	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		cur = PyList_GET_ITEM(p, i);
		if (PyBytes_Check(cur))
		{
			printf("Element %d: bytes\n", i);
			print_python_bytes(cur);
		}
		else if (PyFloat_Check(cur))
		{
			printf("Element %d: float\n", i);
			print_python_float(cur);
		}
		else
		{
			printf("Element %d: %s\n", i, _PyType_Name(cur->ob_type));
		}
	}
}
