from django.shortcuts import render,redirect
from .models import Car
from .forms import CarForm
from django.contrib.messages import constants as messages
from django.contrib import messages



MESSAGE_TAGS = {
    messages.SUCCESS: 'SUCCESS',
    50: 'critical',
}

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)



def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	#Complete Me
	form = CarForm()

	if request.method =="POST":
		form = CarForm(request.POST,  request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your car was created successfully!')
			return redirect('car-list')

	context = {
	"form": form,
	}
	return render(request, 'create.html', context)
	


def car_update(request, car_id):
	#Complete Me
	car=Car.objects.get(id=car_id)
	form = CarForm(instance=car)

	if request.method =="POST":
		form = CarForm(request.POST, request.FILES, instance=car)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your car was updated successfully!')
			return redirect('car-list')

	context = {
	"form": form,
	"car": car
	}
	return render(request, 'update.html', context)
	


def car_delete(request, car_id):
	#Complete Me

	Car.objects.get(id=car_id).delete()
	messages.success(request, 'Your car was deleted successfully!')
	return redirect('car-list')
	return render(request,'car-list')

	