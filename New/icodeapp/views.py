from django.shortcuts import render,redirect,reverse
from .models import Post, Category,Comment
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .forms import RegisterForm


def index(request):
    post = Post.objects.order_by('-date')[:2]
    all_posts = Post.objects.all()
    category = Category.objects.all()
    popular = Post.objects.filter(popular__gte=10)
    return render(request, 'blog/base.html', {'post':post, 'all_posts':all_posts, 'category':category,"popular":popular})



def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
            Q(title__icontains=query) |Q(description__icontains=query)
        )
    return render(request, 'blog/search_results.html', {'search_obj':search_obj, 'query':query})
    

def post_detail(request, slug):
    post_detail = Post.objects.get(slug__iexact = slug)
    post_detail.popular += 1
    post_detail.save()
    return render(request, 'blog/post_detail.html', {'post':post_detail})




def category_detail(request,slug):
    category = Category.objects.get(slug__iexact=slug)
    posts = Post.objects.order_by('-date')
    return render(request, 'blog/category_detail.html',{'category':category, 'posts':posts})


def register(request):
    print(request)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form':form})



def leave_comment(request, slug):
    try:
        post = Post.objects.get(slug__iexact=slug)
    except:
        raise Http404("Статья не найдена")
    if request.user.is_authenticated:
        user = request.user.username
        post.comments.create(author_name=user,
                             comment_text=request.POST.get('comment_text'))
    else:
        post.comments.create(author_name=request.POST.get('name'), comment_text=request.POST.get('comment_text'))
        comment = Comment.objects.order_by('-date')[:2]
    return HttpResponseRedirect(reverse('post_detail_url', args=(post.slug,)))



