from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db import transaction
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import Product, Profile



@login_required()
def home(request):
    context = {
        'yo' : "hello world",
    }
    return render(request, 'core/home.html', context)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return redirect('/')


@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    print(user)
    temp = 'core/profile.html'
    return render(request, temp, {'user_p': user})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print(profile_form)
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('core:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'core/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })






def insta(request):
    
    context = {
        'data': 'somedata from insta'
    }
    return render(request, 'core/insta.html', context)





def products_list():
    product_qs = Product.objects.all()

    products = []

    for product in product_qs:
        products.append({
            'id': product.id,
            'title': product.title,
            'category': product.category.name
        })

    return products

def charts(request):
    return render(request, 'core/charts.html')