from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.froms import RegisterForm
from contact.models import Contact


def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('contact:login')
    
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')
        
    paginator = Paginator(contacts, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
       'page_obj': page_obj,
       'pageTitle': 'Contatos - ' 
    }    
    
    return render(
        request,
        'contact/index.html',
        context, 
        
    )

def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')
        
    contacts = Contact.objects\
        .filter(show=True).\
        filter(
            Q(first_name__icontains = search_value) |
            Q(last_name__icontains = search_value)
        )\
        .order_by('-id')
        
    paginator = Paginator(contacts, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
                    
    context = {
       'page_obj': page_obj,
       'pageTitle': 'Search - ',
    #    'search_value': search_value,
    }    
    
    return render(
        request,
        'contact/index.html',
        context, 
        
    )
    
def contact(request, contact_id):
    # if not request.user.is_authenticated:
    #     return redirect('contact:login')
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True,
    )
    
    pageTitle = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
       'contact': single_contact,
       'pageTitle': pageTitle 
    }    
    
    return render(
        request,
        'contact/contact.html',
        context, 
    )
