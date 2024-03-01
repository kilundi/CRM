from django.shortcuts import render,redirect
from .models import Lead,Agent
from .forms import LeadModelForm, LeadForm


# Create your views here.
def home(request):
    return render(request, 'leads/home.html')

def lead_list(request):
    leads = Lead.objects.all()

    context = {
        "lead_list": leads,
    }
    return render(request, 'leads/leads.html' , context )


def lead_detail(request,pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        "lead": lead,
    }
    return render(request, 'leads/lead_detail.html', context )

def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lead_list/')

    context = {
        "form": form,
        'bg_image': 'images/bg1.svg'
    }

    return render(request, 'leads/lead_create.html', context)

def lead_update(request,pk ):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)

    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/lead_list/')

    context = {
        "form": form,
        'lead': lead
    }

    return render(request, 'leads/lead_update.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('/lead_list/')

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