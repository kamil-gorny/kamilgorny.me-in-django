from django.shortcuts import render

posts_list = [
    {
        'author': 'Kamil', 
        'title' : 'Post 1',
        
    }, 
    {
        'author': 'Tomek', 
        'title' : 'Post 2',
    }, 
]

def home(request):
    context = {
        'posts' : posts_list
    }   
    return render(request, 'blog_app/home.html', context)

def about(request):
    return HttpResponse("about")

def posts(request):
    return HttpResponse("posts")

def contact(request):
    return HttpResponse("contact")