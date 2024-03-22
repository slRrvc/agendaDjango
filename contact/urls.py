
from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('searsh/', views.search, name = 'search'),
    
    #contact (CRUD)
    path('contact/<int:contact_id>/detalhe/', views.contact, name = 'contact'),
    path('contact/cadastro/', views.create, name = 'create'),
    path('contact/<int:contact_id>/alterar/', views.update, name = 'update'),
    path('contact/<int:contact_id>/deletar/', views.delete, name = 'delete'),
    
    #usuario (CRUD)
    path('user/cadastro/', views.register, name = 'register'),
    path('user/entrar/', views.login_view, name = 'login'),
    path('user/sair/', views.logout_view, name = 'logout'),
    path('user/alterar/', views.user_update, name = 'user_update'),
]
