from django.shortcuts import redirect, render
from .models import Choice
# Create your views here.

def choice(request):
    if request.method == "GET":
        my_choices = Choice.objects.all()

        return render(request, "home.html", context= {"my_choices": my_choices})
    
    if request.method == "POST":
        id_to_change = request.POST.get("change")
        item_to_change = Choice.objects.get(id = id_to_change)
        item_to_change.result = not item_to_change.result
        item_to_change.save()
        
        return redirect("choice")