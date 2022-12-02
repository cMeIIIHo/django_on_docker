import subprocess
from django.http import HttpResponse
from bash_file_executor.models import BashFile


def execute_file(request, file_id):
    file = BashFile.objects.get(pk=file_id)
    result = subprocess.run('{}'.format(file.file.path), stdout=subprocess.PIPE)
    file_path = file.file.path

    with open(file_path, 'r') as f:
        file_content = f.read()

    msg = """
file_path:\n{}\n\n
file_content:\n{}\n\n
file_execution_output:\n{}
    """.format(file_path, file_content, result.stdout.decode('utf-8'))

    return HttpResponse(msg, content_type="text/plain")
