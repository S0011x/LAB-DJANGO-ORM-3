from django.shortcuts import render, redirect
from .models import Post,Comment,User
from .forms import PostForm
from django.http import HttpRequest, HttpResponse




def posts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def all_posts(request: HttpRequest):


    if "top" in request.GET:
        post = Post.objects.all().order_by("-rating")
    elif "search" in request.GET:
        post = Post.objects.filter(title__contains=request.GET["search"])
    else:
        post = Post.objects.all()

    return render(request, "blog/all_posts.html", context = {"post" : post})

def add_post(request: HttpRequest):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')  # Redirect to the posts page after successful submission
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def post_detail(request: HttpRequest, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == "POST" and request.user.is_authenticated:
        new_comment = Comment(post=post, user=request.user, content=request.POST["content"], rating=request.POST["rating"])
        new_comment.save()
    comments = Comment.objects.filter(post=post)

    return render(request, "blog/post_detail.html", {"post" : post, "comments" : comments})


def post_update(request, post_id):

    try:
        post = Post.objects.get(id=post_id)

        if request.method == "POST":
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.category = request.POST["category"]
            post.publish_date = request.POST["publish_date"]
            if "photo" in request.FILES:
                post.photo = request.FILES["photo"]
            post.save()

            
            return redirect('blog:posts')
    except:
        return render(request,'blog/notFound.html')
    
    post.publish_date = post.publish_date.strftime("%Y-%m-%d")
    return render(request, 'blog/post_update.html', {'post': post})


def post_delete(request:HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:posts')

def search(request: HttpRequest):
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = []
    return render(request, 'blog/posts.html', {'posts': posts})

