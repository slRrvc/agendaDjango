from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.froms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
        
            messages.success(request, 'Usuário registrado com sussesso!')
            return redirect('contact:register')
        
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )


@login_required(login_url='contact:login')    
def user_update(request):    
    form = RegisterUpdateForm(instance = request.user)
    operation = 'update'
    context = {
        'form': form,
        'operation': operation,
    }
    
    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            context, 
        )
    
    form = RegisterUpdateForm(data = request.POST, instance = request.user)
    context = {
        'form': form,
        'operation': operation,
    }

    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            context, 
        )
        
    form.save()
    return redirect('contact:user_update')
    
        
def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            
            # messages.success(request, 'Acesso autorizado!')
            return redirect('contact:index')   
         
        # messages.success(request, 'Acesso desautorizado, usuario ou senha incorreto.')
        
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )
 
@login_required(login_url='contact:login')       
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')