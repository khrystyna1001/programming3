from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def user_page(request):
    return render(request, "profile.html")

def blogs_page(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", context={"blogs": blogs})

def blog_page(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, "blog.html", context={"blog": blog})