from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from sadat.models import Topic, Webpage, AccessRecords
# from sadat.forms import FormName
from . import forms
from sadat.forms import NewUserForm,UserForm,UserProfileInfoForm

def home(request,*args,**kwargs):
    #return HttpResponse("Welcome to sadats home")    
    #return render,('index.html') #### this will also work========
    webpage_list = AccessRecords.objects.order_by('date')
    # top_name = Webpage.objects.all()
    date_dict = { 'access_records' : webpage_list}
    return render(request, "index.html", context = date_dict)

def about(request):
    return render(request, "about.html",{})

def tutorial(request):
    return render(request, "tutorial.html",{})

# this part is related to form
def form_page(request):    
    form_value = forms.FormName
    # if form_value.is_valid
      
    return render(request, "form_page.html",{'form_key' : form_value})

def user_signup_form(request):    
    signup_form_value = forms.NewUserForm

    if request.method == "POST":
        signup_form_value = forms.NewUserForm(request.POST)

        if signup_form_value.is_valid:
            signup_form_value.save(commit=True)
            return home(request)
        else:
            print("Error in the page")

    # if form_value.is_valid
      
    return render(request, "user_signup_form.html",{'signup_form_key' : signup_form_value})


def user_registration_form(request):
    registered = False

    registration_form_value = forms.UserForm
    frofile_form_value = forms.UserProfileInfoForm

    if request.method == "POST":
        registration_form_value = UserForm(data=request.POST)
        frofile_form_value = UserProfileInfoForm(data=request.POST)

        if registration_form_value.is_valid() and frofile_form_value.is_valid():

            user = registration_form_value.save()
            user.set_password(user.password)
            user.save

            profile = frofile_form_value.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            # return home(request)

        else:
            # print(registration_form.error, profile_info_form.error)
            print("Error in the page")
            
    else:
        registration_form_value = UserForm
        profile_form_value = UserProfileInfoForm    
          
    return render(request, "registration.html",
                {'registration_form_key' : registration_form_value,
                'profile_form_key' : frofile_form_value,
                'registered': registered})








# def user_registration_form(request):
#     registered = False

#     registration_form_value = forms.UserForm

#     if request.method == "POST":
#         # registration_form_value = forms.UserForm(request.POST)
#         registration_form_value = UserForm(data=request.POST)

#         if registration_form_value.is_valid:
#             registration_form_value.save(commit=True)
#             return home(request)
#         else:
#             print("Error in the page")

#     # if form_value.is_valid
      
#     return render(request, "registration.html",{'registration_form_key' : registration_form_value})
