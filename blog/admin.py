from django.contrib import admin
from .models import *

class category_admin(admin.ModelAdmin):
    list_display = ( 'image_tag','title' , 'description' , 'url' , 'add_date')
    search_fields = ('title' ,)

class Post_admin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat' , )

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)
    


admin.site.register(Category , category_admin)
admin.site.register(Post , Post_admin)