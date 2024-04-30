from django.contrib import admin
from .models import Thesis

class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')  # Removed 'slug'
    list_filter = ('status',)  # Removed 'status' from list_display
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Thesis, ThesisAdmin)
