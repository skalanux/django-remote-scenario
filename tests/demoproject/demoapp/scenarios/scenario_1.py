from django_dynamic_fixture import G

from demoapp.models import Question

def main(request):
    # setup your objects here
    G(Question)
    G(Question)
    G(Question)
    G(Question)
