from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['url']:
			post = Post()
			post.title = request.POST['title']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				post.url = request.POST['url']
			else:
				post.url = 'http://' + request.POST['url']
			post.author = request.user
			post.pub_date = timezone.datetime.now()
			post.save()
			return redirect('home')
		else:
			return render(request, 'posts/create.html', {'msg':'please enter all the required fields'})
	else:
		return render(request, 'posts/create.html')

def home(request):
	posts = Post.objects.order_by('vote_count').reverse()
	return render(request, 'posts/home.html', {'posts':posts})

@login_required
def upvote(request, pk):
	post = Post.objects.get(pk=pk)
	post.vote_count += 1
	post.save()
	return redirect('home')

@login_required
def downvote(request, pk):
	post = Post.objects.get(pk=pk)
	post.vote_count -= 1
	post.save()
	return redirect('home')