import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\tcl\tk8.6"

executables = [cx_Freeze.Executable("ghoulsPygame.py")]

cx_Freeze.setup(
    name="Somhm xx Ghouls",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables)