from django.http import HttpResponse

from demoapp.models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return HttpResponse(questions)

