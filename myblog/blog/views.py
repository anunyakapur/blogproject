from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth import logout
from .forms import PostForm, CommentForm
from django.http import JsonResponse, HttpResponseForbidden

def custom_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect('/login/')

    return render(request, 'registration/logout.html')

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            if not comment_form.cleaned_data['post_anon']:
                comment.author = request.user.username
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if not form.cleaned_data['post_anon']:
                post.author = request.user.username
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user.username:
        return redirect('post_list')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if not form.cleaned_data['post_anon']:
                post.author = request.user.username
            else:
                post.author = ''
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user.username:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/confirm_delete.html', {'post': post})