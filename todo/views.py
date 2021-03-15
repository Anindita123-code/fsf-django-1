from django.shortcuts import render, redirect
from .models import items


# Create your views here.


def get_todo_list(request):
    # return HttpResponse('<h1>Hello</h1><p>This is a paragraph</p>')
    items1 = items.objects.all()
    context = {
        'items': items1
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        items.objects.create(name=name, done=done)
        return redirect('get_todo_list')

    return render(request, 'todo/add_item.html')
