from django.contrib.auth.forms import UserCreationForm
from . models import User


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2", "is_writer"]
        