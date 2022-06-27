import sys
import os 
from cx_Freeze import setup,Executable

files=['Pressing_base_donne.db','icon.ico']

target=Executable(
    script="Pressing_code.py",
    base="Win32GUI",
    icon='icon.ico'
)
setup(
    name="Pressing",
    version="1.0",
    description="Crreator : Diden Amine",
    author="Diden amine",
    options={'build_exe' :{'include_files':files}},
    executables=[target]
)
