from django.contrib import admin
from .models import Post

# Register your models here. - this will make it visibile on the admin page
admin.site.register(Post)