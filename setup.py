import sys
import os 
from cx_Freeze import setup,Executable

files=['Dry_cleaners_app_data.db','icon.ico']

target=Executable(
    script="Dry_cleaners_app.py", 
    base="Win32GUI",
    icon='icon.ico'
)
setup(
    name="Dry_cleaners_app",
    version="1.0",
    description="Dry_cleaners_app is a desktop software made to help the owner to get rid of the paper use",
    author="Diden Amine",
    author_email="d19amine@gmail.com",
    options={'build_exe' :{'include_files':files}},
    executables=[target]
)
