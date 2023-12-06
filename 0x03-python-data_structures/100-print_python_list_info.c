#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * print_python_list_info -  The function that prints some basic
 * info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int Ray;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (Ray = 0; Ray < Py_SIZE(p); Ray++)
		printf("Element %d: %s\n", Ray, Py_TYPE(PyList_GetItem(p, Ray))->tp_name);
}
