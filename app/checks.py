import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
import django
django.setup()

import subprocess

from django.contrib.auth.models import User
from bash_file_executor.models import BashFile

# -----------------------------------------------------

# files = BashFile.objects.all()
# for f in files:
#     print(f.file.path)

# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------

# users = User.objects.all()
# print(list(users))

# -----------------------------------------------------
# path_for_files_folder = 'bash_scripts_files'
# print(list(os.walk(path_for_files_folder)))
# _, _, files_names = list(os.walk(path_for_files_folder))[0]
# print(files_names)
# file_paths = []
# for file_name in files_names:
#     file_paths.append(os.path.join(path_for_files_folder, file_name))
# print(file_paths)
#
# for file_path in file_paths:
#     with open(file_path, 'r') as f:
#         print(f.read())
#
#     print('start')
#     subprocess.call(file_path, shell=True)
#     print('end')

# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------

# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
#     break