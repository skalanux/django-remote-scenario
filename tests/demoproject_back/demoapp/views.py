import json

from django.http import HttpResponse

from demoapp.models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    questions_data = [dict(id=q.id, text=q.question_text) for q in questions]
    return HttpResponse(json.dumps(questions_data), content_type='application/json')

