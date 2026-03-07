def read_file_function():
    with open("doc/my_python_file.py") as f:
        return f.read()
    
def read_file_function_dynamic(path: str):
    with open(f"doc/{path}") as f:
        return f.read()
    

