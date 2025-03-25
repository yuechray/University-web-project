from django.shortcuts import render
from datetime import datetime

from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import TaskForm, CommentForm
from .forms import UserRegisterForm, UserLoginForm, ReviewForm
from .models import Task, Comment, Review

def main(request):
    tasks = Task.objects.order_by('-id')[:3]
    user = request.user
    context = {
    'title': 'Главная страница сайта',
    'tasks': tasks,
    'user': user
    }

    return render(request, 'main.html', context)  

def about(request):
    context = {
    'user': request.user
    }
    return render(request, 'about.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'user': request.user
    }

    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
        'user': request.user
    }
    return render(request, 'login.html', context)

def links(request):
    context = {
    'user': request.user
    }

    return render(request, 'links.html', context)

def news(request):
    tasks = Task.objects.all()
    search = request.GET.get('search')

    if request.method == "POST":
        d = request.POST
        for key, value in d.items():
            if key == "reason":
                reason_ = value
                reasons = {
                    "upper": "-date_published",
                    "lower": "date_published"
                }

                tasks = tasks.order_by(reasons[reason_])

    if search:
        tasks = tasks.filter(title__icontains=search)
    paginator = Paginator(tasks, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user': request.user
    }

    return render(request, 'news.html', context)


def create(request):
    title = "Создать новость"
    action = "Создать"
    if not request.user.is_superuser:
        return redirect('https://youtu.be/3p6HiR8iKXQ?t=30')
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.date_published = datetime.now()
            new_form.save()
            return redirect('news')
    else:
        form = TaskForm()

    context = {
        'form': form,
        'user': request.user,
        'title': title,
        'action': action
    }

    return render(request, 'create.html', context)

def update_news(request, pk):
    action = "Обновить"
    task = Task.objects.get(pk=pk)
    title = f"Редактирование {task.title}"
    if not request.user.is_superuser:
        return redirect('https://www.youtube.com/watch?v=qn9FkoqYgI4')
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail_news', pk=pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'create.html',
                  {'form': form, 'title': title, 'action': action, 'is_delete': True, 'task': task})


def detail(request, pk):
    tasks = Task.objects.all()
    task = Task.objects.get(pk=pk)
    title = task.title

    first = tasks.first().id
    last = tasks.last().id
    count = str(request.GET.get("post"))

    if count == "prev":
        if task.id == first:
            return redirect('detail_news', pk=last)
        prev_task = tasks.filter(id__lt=task.id).last()
        return redirect('detail_news', pk=prev_task.id)

    if count == "next":
        if task.id == last:
            return redirect('detail_news', pk=first)
        next_task = tasks.filter(id__gt=task.id).first()
        return redirect('detail_news', pk=next_task.id)

    comments = Comment.objects.filter(task=pk).order_by("-date_published")
    context = {
        'task': task,
        'comments': comments,
        "title": title
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.date = datetime.now()
            new_comment.task = task
            new_comment.save()
            return redirect('detail_news', pk=pk)
    else:
        form = CommentForm()
    context["form"] = form
    return render(request, 'solo_new.html', context)

def delete_news(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()

    return redirect("news")


def logout_(request):
    logout(request)
    return redirect('login')

def admin(request):
    return redirect('admin')

def radio(request):
    if request.method == "POST":
        d = request.POST
        for key, value in d.items():
            if key == "reason":
                reason_ = value



def pool(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('-date_published')  
    
    return render(request, 'pool.html', {'form': form, 'reviews': reviews})