#!/usr/bin/python3
import importlib.util
import os
if __name__ == "__main__":
    pyc_file_path = os.getcwd()
    spec = importlib.util.spec_from_file_location('hidden_4', pyc_file_path)
    pyc_file = importlib.util.module_from_spec(spec)
    name = dir(pyc_file)
    for nm in name:
        if nm[:2] != "__":
            print(nm)

