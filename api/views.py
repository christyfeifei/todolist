from django.shortcuts import render
from todo.models import Todo
from django.http import HttpResponse
import json
# Create your views here.

#  取得所有的代辦事項
    # title=models.CharField(max_length=100)
    # text=models.TextField(blank=True)
    # created=models.DateTimeField(auto_now_add=True)
    # date_completed=models.DateTimeField(null=True,blank=True)
    # important=models.BooleanField(default=False)
    # completed=models.BooleanField(default=False)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)

def todos_api(request):
    todo_list=[]

    try:
        todos=Todo.objects.all()
    
        for todo in todos:
            todo_data={
                'id':todo.id,
                'text':todo.text,
                'important':todo.important,
                'completed':todo.completed,
                'created':todo.created.strftime('%Y-%m-%d %H:%M:%S'),
                'date_completed':todo.date_completed.strftime('%Y-%m-%d %H:%M:%S')\
                    if todo.completed else None,
                'user':todo.user.username
            }
            todo_list.append(todo_data)
        print(todo_list)
    except Exception as e:
        print(e)

    todo_list = json.dumps(todo_list,ensure_ascii=False)

    return HttpResponse(todo_list,content_type='application/json')