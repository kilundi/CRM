from django.shortcuts import render,redirect
from .models import Lead
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizorAndLoginRequiredMixin

from .forms import LeadModelForm,CustomUserCreationForm, LeadForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'leads/home.html'


# def home(request):
#     return render(request, 'leads/home.html')

class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/leads.html'
    context_object_name = 'lead_list'

    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)
            #filter for the agent that is logged in
            queryset = queryset.filter(agent__user = user)
        return queryset





# def lead_list(request):
#     leads = Lead.objects.all()

#     context = {
#         "lead_list": leads,
#     }
#     return render(request, 'leads/leads.html' , context )


class LeadDetailView( LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)
            #filter for the agent that is logged in
            queryset = queryset.filter(agent__user = user)
        return queryset

# def lead_detail(request,pk):
#     lead = Lead.objects.get(pk=pk)
#     context = {
#         "lead": lead,
#     }
#     return render(request, 'leads/lead_detail.html', context )


class LeadCreateView(OrganizorAndLoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    success_url = '/lead_list/'
# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/lead_list/')

#     context = {
#         "form": form,
#         'bg_image': 'images/bg1.svg'
#     }

#     return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(OrganizorAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    success_url = '/lead_list/'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organization
        return Lead.objects.filter(organization = user.userprofile)

# def lead_update(request,pk ):
#     lead = Lead.objects.get(pk=pk)
#     form = LeadModelForm(instance=lead)

#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/lead_list/')

#     context = {
#         "form": form,
#         'lead': lead
#     }

#     return render(request, 'leads/lead_update.html', context)

class LeadDeleteView(OrganizorAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'
    context_object_name = 'lead'
    success_url = '/lead_list/'

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organization
        return Lead.objects.filter(organization = user.userprofile)


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = '/login'


class LogoutPageView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/logout.html'



# def logout(request):
#     return render(request, 'registration/logout.html')


# def lead_delete(request, pk):
#     lead = Lead.objects.get(pk=pk)
#     lead.delete()
#     return redirect('/lead_list/')

# def lead_update(request, pk):
#     lead = Lead.objects.get(pk=pk)

#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():

#           first_name = form.cleaned_data["first_name"]
#           last_name = form.cleaned_data["last_name"]
#           age = form.cleaned_data["age"]


#           lead.first_name = first_name
#           lead.last_name = last_name
#           lead.age = age
#           lead.save()


#           return redirect('/lead_list/')



    # context = {
    #     "form": form,
    #     'lead': lead
    # }

    # return render(request, 'leads/lead_update.html', context)

# def lead_create1(request):
    # form = LeadForm()
    # if request.method == 'POST':
    #     form = LeadForm(request.POST)
    #     if form.is_valid():

    #       first_name = form.cleaned_data["first_name"]
    #       last_name = form.cleaned_data["last_name"]
    #       age = form.cleaned_data["age"]
    #       agent = Agent.objects.first()

    #       Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent
    #         )
    #       return redirect('lead/')



    # context = {
    #     "form": form
    # }

#     return render(request, 'leads/lead_create.html', context)