from django.shortcuts import render
from annoying.decorators import render_to

# Create your views here.


@render_to('galerieApp/index.html')
def main(request):
    if request.method == "GET":
        ctx = {}
        return ctx