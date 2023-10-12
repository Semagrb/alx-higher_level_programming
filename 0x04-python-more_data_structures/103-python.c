from ctypes import py_object, c_ssize_t, c_void_p, c_char_p
from sys import version_info
import struct
import ctypes
from types import ListType

def print_python_bytes(p) :
	if not isinstance(p, bytes) :
		print("[.] bytes object info")
		print("  [ERROR] Invalid Bytes Object")
		return

	print("[.] bytes object info")
size = len(p)
	print("  size: {}".format(size))
	print("  trying string: {}".format(p.decode("utf-8", "ignore").replace('\x00', '')))
limit = min(size, 10)
	print("  first {} bytes:".format(limit))

	for i in range(limit) :
		byte = struct.unpack('B', p[i : i + 1])[0]
		print(" {:02x}".format(byte), end = "")
		print()

	def print_python_list(p) :
		if type(p) is not ListType :
			return

	print("[*] Python list info")
size = len(p)
	print("[*] Size of the Python List = {}".format(size))
	allocated = getattr(p, 'allocated', 0)
	print("[*] Allocated = {}".format(allocated))

	for i, item in enumerate(p) :
		obj_type = item.__class__.__name__
		print("Element {}: {}".format(i, obj_type))
		if isinstance(item, bytes) :
			print_python_bytes(item)

# Example usage :
			my_bytes = b'Hello, World!'
			my_list = (b'Python', b'Programming', b'is', b'fun')
	print_python_bytes(my_bytes)
print_python_list(my_list)
