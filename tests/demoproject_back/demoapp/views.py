import json

from django.http import HttpResponse

from datetime import date
from demoapp.models import Question, Choice

from demoapp import utils


# Create your views here.
def index(request):
    questions = Question.objects.all()
    questions_data = [dict(id=q.id, text=q.question_text) for q in questions]
    return HttpResponse(json.dumps(questions_data), content_type='application/json')

def y2k(request):
    current_date = utils.get_current_date()

    if current_date == date(2000,1,1):
        response = "%s El mundo ha llegado a su fin" % current_date.strftime("%d/%m/%Y")
    else:
        response = "Hoy es %s" % current_date.strftime("%d/%m/%Y")

    return HttpResponse(response)

