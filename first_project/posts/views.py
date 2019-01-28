from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.

def post_create(request):
    
    return HttpResponse("<h1>Form is Posted</h1>")

def post_detail(request):#retrieve
    
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Submitted successfully")
    else:
        messages.error(request, "Not Submitted successfully")
    context = {
        "form" : form,
        }
    return render(request,"post_form.html",context)

def post_list(request):
    
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "create"
        }
    return render(request, "main.html", context)

def post_update(request):
    
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    
    return HttpResponse("<h1>Delete</h1>")