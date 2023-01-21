from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):

    teamMeamber = TeamMember.objects.all()
    ourroom = OurRoom.objects.all()
    

    if request.method == 'POST':
        form = Contacts(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Contacts()

    context = {
        'teamMeamber':teamMeamber,
        'ourroom':ourroom,
        'form':form

    }
    return render(request, 'index.html', context)

def room(request):
    a_room = OurRoom.objects.all()
    return render(request, 'room.html',{'a_room':a_room})

def order(request,id):
    obj  = get_object_or_404(OurRoom, pk=id) 
    return render(request, 'room_details.html',{'obj':obj})


def order_registration(request):
    if request.method == 'POST':
        forms = OrderRoom(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = OrderRoom()
    return render(request, 'order_registration.html', {'forms':forms})

    

