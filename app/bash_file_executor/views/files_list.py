from django.shortcuts import render

from bash_file_executor.models import BashFile


def files_list(request):
    files = BashFile.objects.all()
    return render(request, 'bash_file_executor/files_list.html', {'files': files})
