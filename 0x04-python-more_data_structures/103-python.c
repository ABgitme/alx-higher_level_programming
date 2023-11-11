#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <Python.h>

int __dummy;
/*
 * Print the information of a Python list object.
 */
void print_python_list(PyObject *p) {
  if (!PyList_Check(p)) {
    printf("[ERROR] Invalid List Object\n");
    return;
  }

  Py_ssize_t size = PyList_Size(p);
  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", PyList_GET_ALLOC(p));

  for (Py_ssize_t i = 0; i < size; i++) {
    PyObject *element = PyList_GetItem(p, i);

    if (PyBytes_Check(element)) {
      printf("Element %ld: bytes\n", i);
      print_python_bytes(element);
    } else {
      printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
  }
}

/*
 * Print the information of a Python bytes object.
 */
void print_python_bytes(PyObject *p) {
  if (!PyBytes_Check(p)) {
    printf("[ERROR] Invalid Bytes Object\n");
    return;
  }

  Py_ssize_t size = PyBytes_GET_SIZE(p);
  printf("[.] bytes object info\n");
  printf("  size: %ld\n", size);

  // Try to decode the bytes object as a string.
  char *string = PyBytes_AsString(p);
  if (string != NULL) {
    printf("  trying string: %s\n", string);
  }

  // Print the first 10 bytes of the bytes object.
  printf("  first 10 bytes: ");
  for (Py_ssize_t i = 0; i < size && i < 10; i++) {
    printf("%02x ", PyBytes_AS_STRING(p)[i]);
  }
  printf("\n");
}