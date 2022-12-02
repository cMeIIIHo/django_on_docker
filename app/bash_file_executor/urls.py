import os
from django.urls import path
from .views.execute_file import execute_file
from .views.files_list import files_list

app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))  # название прило из пути

urlpatterns = [
    path('', files_list, name='files_list'),
    path('execute_file/<int:file_id>', execute_file, name='execute_file')
]
