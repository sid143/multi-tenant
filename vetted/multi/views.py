from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from .forms import *




class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self):
        obj = super().get_context_data()
        obj['loginForm'] = LoginForm()
        return obj

    @method_decorator(login_required) # we can use multiple decorators here
    def dispatch(self, request):
        return super().dispatch(request)
 

def login_view(request):
    login_error = ""

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == "GET":
        loginForm = LoginForm()
    elif request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            # authenticate here
            user = authenticate(username = username, password = password)

            if user is not None:
                # user authenticated
                login(request, user)
                try:
                    next_page = request.GET['next']
                    return HttpResponseRedirect(next_page)
                except:
                    return HttpResponseRedirect('/')
            else:
                # wrong credentials
                login_error = "Username/Password incorrect"
    
    context = {
    'loginForm' : loginForm,
    'login_error' : login_error
    }
    
    return render(request, 'index.html', context)


class MainEmployeeView(TemplateView):
    template_name = 'mainemployee.html'

class NewhtmlView(TemplateView):
    template_name = 'newhtml.html'

class ProfessView(TemplateView):
    template_name = 'profess.html'




# Create your views here.
