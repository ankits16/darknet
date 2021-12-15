import sys
import subprocess
import os

from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools import setup, find_packages

class Build(build_ext):
 """Customized setuptools build command - builds protos on build."""
 def run(self):
     protoc_command = ["make"]
     # os.chdir('./darknet_src/ai_darknet')
     if subprocess.call(protoc_command) != 0:
         sys.exit(-1)
     build_ext.run(self)


setup(
 name='ai_darknet_local',
 version='1.0',
 description='Python Distribution Utilities',
 packages=find_packages(where='.'),
 py_modules=['darknet.py'],
 package_data= {'': ['darknet']},
 # py_modules=['darknet.py'],
 # data_files=['darknet'],
 has_ext_modules=lambda: True,
 cmdclass={
     'build_ext': Build,
 }
)