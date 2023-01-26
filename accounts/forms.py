from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
