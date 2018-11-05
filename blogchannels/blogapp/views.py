from django.shortcuts import render
from blogapp.models import Post, Comment
from blogapp.forms import CommentForm



def base_view(request):
	posts = Post.objects.all()
	return render(request, 'base.html', {'posts': posts})


def post_detail(request, slug):
	post = Post.objects.get(slug=slug)
	form = CommentForm(request.POST or None)
	comments = Comment.objects.filter(post=post)
	return render(request, 'post_detail.html', {
		'post': post,
		'form': form,
		'comments': comments
	})
