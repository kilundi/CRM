from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

import random
from django.views import generic
from django.core.mail import send_mail

# from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizorAndLoginRequiredMixin
# Create your views here.

class AgentListView( OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter( organization = organization)

class AgentCreateView( OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agents_list")

    def form_valid(self, form):
        user =form.save(commit=False)
        user.is_agent = True
        user.is_organizor = False
        user.set_password(f"{random.randint(0, 100000000)}")
        user.save()

        Agent.objects.create(
            user = user,
            organization = self.request.user.userprofile
            )

        send_mail(
            subject = 'You are invited to be an agent',
            message = 'You were added as an agent on COSSIM LIMITED. Please login to your account',
            from_email = 'contact@cossim.com',
            recipient_list = [user.email],

        )

        return super(AgentCreateView,self).form_valid(form)


class AgentDetailView(OrganizorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_details.html'
    context_object_name = 'agent'


    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter( organization = organization)



class AgentUpdateView( OrganizorAndLoginRequiredMixin, generic.UpdateView ):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    success_url = '/agents_list/'


    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization = organization)





class AgentDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'
    success_url = '/agents_list/'


    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter( organization = organization)