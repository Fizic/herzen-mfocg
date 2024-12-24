import PyInstaller.__main__
import shutil

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--noconsole',
], )

shutil.copytree('sounds/', '/sounds')
shutil.copytree('sprites/', '/sprites')
