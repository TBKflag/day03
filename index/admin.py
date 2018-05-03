from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','age','email')
    list_display_links = ('name', 'email')
    list_editable=('age',)
    search_fields=['name','email']
    list_filter=['name','age','email']
    # fields=['name','email']
    fieldsets=(
        ('基本信息',{
            'fields':['name','age'],
            'classes':['collapse'],
            }),
        ('高级信息', {
            'fields': ['email', 'isactive'],
            'classes':('collapse',),
        }),
    )

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publicate_date'

class publisherAdmin(admin.ModelAdmin):
    list_display=['name','address','city']
    list_editable=['address','city']
    list_filter=['address','city']
    fieldsets=(
        ('基本选项',{
            'fields':['name','address','city'],
        }),
        ('可选选项',{
            'fields':['country','website'],
            'classes':['collapse'],
        })
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher, publisherAdmin)
admin.site.register(wife)