


import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file closed")


with file_open("test.txt") as f:
    print(f)



















