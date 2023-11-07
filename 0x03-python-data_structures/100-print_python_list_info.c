/**
* print_python_list_info - prints some basic information
*          about the Python object pointed to
* @p: A pointer to a Python object
*
* Return: nothing
*/

void print_python_list_info(PyObject *p)
{
	int i, length, allocated;
	PyObject *item;

	length = PyList_Size(p);
	allocated = PyListObject_allocated(p);
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
