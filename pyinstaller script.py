import sys
from PyInstaller.__main__ import run

# Specify the source file
source_file = 'clicker-game.py'

# Additional files or data files
additional_files = ['Montserrat-Medium.ttf']

# PyInstaller options
options = [
    '--onefile',            # Create a single executable file
    #'--windowed',           # Create a windowed application (no console)
    f'--add-data={",".join(additional_files)};.',  # Include additional files
]

# Run PyInstaller
run([source_file] + options)
