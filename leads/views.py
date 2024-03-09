from django.urls import reverse
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from .models import Lead, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganizorAndLoginRequiredMixin

from .forms import LeadModelForm,CustomUserCreationForm, LeadForm, AssignAgentForm, LeadCategoryUpdateForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView, FormView

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
            queryset = Lead.objects.filter(organization = user.userprofile, agent__isnull =False)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)
            #filter for the agent that is logged in
            queryset = queryset.filter(agent__user = user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user

        context = super(LeadListView, self).get_context_data(**kwargs)
        if user.is_organizor:
            queryset = Lead.objects.filter(
                organization = user.userprofile, agent__isnull = True
                )
            context.update({
                "unassigned_leads": queryset,
            })
        return context





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


    def form_valid(self, form):
        # form.instance.organization = self.request.user.userprofile
        lead = form.save( commit=False)
        lead.organization = self.request.user.userprofile
        lead.save()

        return super(LeadCreateView, self).form_valid(form)
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


class AssignAgentView(OrganizorAndLoginRequiredMixin, FormView):
    template_name = 'leads/assign_agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update( {
            "request": self.request
        })
        return kwargs
    success_url = '/lead_list/'

    def form_valid(self, form):
        agent= form.cleaned_data["agent"]
        lead = Lead.objects.get(id = self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)

class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "leads/category_list.html"
    context_object_name = 'category_lists'

    def get_context_data(self,**kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)

        user = self.request.user

        if user.is_organizor:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count(),
        })

        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)
        return queryset

class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/category_detail.html"
    context_object_name = 'category'


    # def get_context_data(self, **kwargs):
    #     context = super(CategoryDetailView, self).get_context_data(**kwargs)
    #     leads = self.get_object().leads.all()
    #     context.update({
    #         "leads": leads
    #     })

    #     return context


    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Category.objects.filter(organization = user.userprofile)
        else:
            queryset = Category.objects.filter(organization = user.agent.organization)
        return queryset

class LeadCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_category_update.html'
    form_class = LeadCategoryUpdateForm


    def get_success_url(self) -> str:
        return reverse("leads:lead_detail", kwargs={"pk": self.get_object().id})

    def get_queryset(self):
        user = self.request.user
        if user.is_organizor:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)
            #filter for the agent that is logged in
            queryset = queryset.filter(agent__user = user)
        return queryset


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