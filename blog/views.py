from django.shortcuts import render
from django.utils import timezone
from .models import	Post
#from .forms	import PostForm

def	post_list(request):
    posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return	render(request,	'blog/post_list.html',	{})
def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post,	pk=pk)
    return render(request,	'blog/post_detail.html', {'post': post})
def	post_new(request):
    form = PostForm.clear()
    return	render(request,	'blog/post_edit.html',	{'form':form})
