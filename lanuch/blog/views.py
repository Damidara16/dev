from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Post, Comments, waste
from .forms import CreatePost, CommentCreate

def Post_all(request):
    '''
    post = Post.objects.all()
    posts = []
    for i in post:
        if i.private == True:
            posts.append(i)
    for x in posts:
        return x.id
    Posts = Post.objects.exclude(id=x)[:25]
    context = {'Posts':Posts}
    '''
    posts = Post.objects.all()[:25]
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def CreateComment(request, post_pk):
    if request.user.is_authenticated():
    #FIRST MAKE SURE THE USER MAKING THE COMMENT IS AN AUTHENTICATED USER, GET THE POST ID TO KNOW WHICH POST THE BELONGS TO,
    #THEN CHECK IF IT EXIST, AFTER IT DOES SAVE THE COMMENT WITH ITS DATA AND MAKE SURE ITS LINKED TO THE RIGHT POST
        try:
            post = Post.objects.get(pk=post_pk)
            if request.method == 'POST':
                form = CommentCreate(request.Post)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.user = request.user
                    comment.context = form.cleaned_data['context']
                    comment.post = post
                    comment.save()
            else:
                form = CommentCreate()
                btnName = 'Post'
                return render(request, 'blog/create.html', {'form':form, 'btnName':btnName})
        except Post.DoesNotExist:
            raise Http404('Post does not exist')
        #return render(request, 'blog/detail.html', {'post':post})
    else:
        return redirect('/home/')


def DeleteComment(request, post_pk):
    #Post.comment_set.all()
    if request.user.is_authenticated():
        try:
            post = Post.objects.get(pk=post_pk)
            #itrated through the post comments then through user and then author to get the id of the comment owner
            if post.comment_set.user.author.id == request.user.id:
                post.delete()
        except Post.DoesNotExist:
            raise Http404('Post does not exist')
        return render(request, 'blog/detail.html', {'post':post})
    else:
        return redirect('/home/')

#should add a view everytime a post is detailed
def Post_detail(request, post_pk):
    try:
        post = Post.objects.get(pk=post_pk)
        post.views += 1
        post.save()
        #IN THE FUTURE ADD A FUNC THAT WONT ADD A NEW VIEW WHEN REFRESHED, COULD USE A TIMER TO INDICATE IF IT WAS
        #OR CHECK IF DANGO HAS A THING THAT CHECK FOR REFRESH
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(request, 'blog/detail.html', {'post':post})


def Post_create(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = CreatePost(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                title = form.cleaned_data['title']
                author = request.user
                content = form.cleaned_data['content']
                post.save()
    
                return redirect('/')
            return redirect('/')
        else:
            form = CreatePost()
            title = 'Create A Post'
            btnName = 'Create Post'
            context = {'form':form, 'title':title, 'btnName':btnName}
            return render(request, 'blog/create.html', context)
    return redirect('/accounts/login')


def Post_delete(request, post_pk):
    if request.user.is_authenticated():
        try:
            post = Post.objects.get(pk=post_pk)
            if post.author.id == request.user.id:
                post.delete()
                return redirect('/home/deleted')
        except Post.DoesNotExist:
            raise Http404('Post does not exist')
        return render(request, 'blog/detail.html', {'post':post})
    else:
        return redirect('/home/')
