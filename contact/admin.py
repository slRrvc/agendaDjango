from django.contrib import admin

from contact.models import Category, Contact


@admin.register(Contact)
class ConyactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'email', 'category', 'created_date',
    ordering = '-id','first_name',
    list_filter = 'created_date', 'category',
    search_fields = 'first_name', 'last_name',
    list_per_page = 50
    list_max_show_all = 50
    # list_editable = 'first_name',
    list_display_links = 'first_name', 'last_name',
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id','name',
    # list_filter = 'created_date',
    search_fields = 'name',
    list_per_page = 10
    list_max_show_all = 50
    # list_editable = 'first_name',
    list_display_links = 'name', 