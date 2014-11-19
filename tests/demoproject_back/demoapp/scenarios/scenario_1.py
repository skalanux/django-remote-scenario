from django_dynamic_fixture import G

from demoapp.models import Question
import random
qs = ['flat or nested?', 'sparse or dense?', 'complex or complicated?', 'explicit or implicit?', 'now or never?']

def main(request):
    # setup your objects here
    for i in range(0,5):
        choice = random.choice(qs)
        G(Question, question_text=choice)
