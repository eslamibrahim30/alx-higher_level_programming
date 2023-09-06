#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t length = 0;
	Py_ssize_t allocated = 0;
	Py_ssize_t i = 0;
	PyObject *item = NULL;
	PyTypeObject *type = NULL;
	
	if (PyList_Check(p) == 0)
		return;
	length = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %lu\n", length);
	printf("[*] Allocated = %lu\n", allocated);
	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item);
		printf("Element %lu: %s\n", i, type->tp_name);
	}
}
