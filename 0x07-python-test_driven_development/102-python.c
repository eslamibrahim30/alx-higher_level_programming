#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_string(PyObject *p)
{
	const char *string = NULL;
	Py_ssize_t size = 0;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p) == 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	size = PyUnicode_GET_LENGTH(p);
	string = PyUnicode_AsUTF8(p);
	if (PyUnicode_IS_COMPACT_ASCII(p) == 1)
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", size);
	printf("  value: %s\n", string);
}
