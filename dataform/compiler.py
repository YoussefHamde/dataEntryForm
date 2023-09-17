import os
import sys
import auto_py_to_exe


# Get the path to the directory containing the Python interpreter.
python_dir = os.path.dirname(sys.executable)

# Construct the path to the auto-py-to-exe executable.
auto_py_to_exe_path = os.path.join(python_dir, "Scripts", "auto-py-to-exe.exe")

# Print the path to the auto-py-to-exe executable.
print(auto_py_to_exe_path)