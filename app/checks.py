import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
import django
django.setup()

from django.contrib.auth.models import User

users = User.objects.all()
print(list(users))