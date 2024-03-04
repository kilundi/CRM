from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Lead,Agent


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'bg-slate-500 text-black border-0 rounded-xl p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
                'last_name': forms.TextInput(attrs={'class': 'bg-slate-500 text-black border-0 rounded-md p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
                'age': forms.NumberInput(attrs={'class': 'bg-slate-500 text-black border-0 rounded-md p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
                'agent': forms.Select(attrs={'class': 'bg-slate-500 text-black border-0 rounded-md p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
            }



class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=18)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


        widgets = {
            'username': forms.TextInput(attrs={'class': 'bg-slate-500 text-black border-0 rounded-xl p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
            'email': forms.EmailInput(attrs={'class': 'bg-slate-500 text-black border-0 rounded-xl p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
            'password1': forms.PasswordInput(attrs={'class': 'bg-slate-500 text-black border-0 rounded-xl p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
            'password2': forms.PasswordInput(attrs={'class': 'bg-slate-500 text-black border-0 rounded-xl p-2 w-full focus:bg-gray-600 focus:outline-none focus:ring-1 focus:ring-blue-500 transition ease-in-out duration-150'}),
        }


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')

        agents = Agent.objects.filter(organization = request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents
