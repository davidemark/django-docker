from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from my_app.models import Todo

class TodoView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'

    def post(self, request):
        data = request.data
        todo = Todo.objects.create(task=data['task'], completed=data['completed'])
        return Response(status=200, template_name=self.template_name)

    def get(self, request):
        todos = Todo.objects.all()
        context = {'todos': [(x.task, x.completed) for x in todos]}
        return Response(context, template_name=self.template_name)
