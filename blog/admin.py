from django.contrib import admin
from blog.models import Post,Comment,Upload
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # menampilkan list tabel pada django panel admin menu Blog
    list_display = ['id','title','content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','content']

class UploadAdmin(admin.ModelAdmin):
    list_display = ['title_pic','model_pic']

# untuk mendaftarkan dan menambahkan class ke panel django
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Upload, UploadAdmin)