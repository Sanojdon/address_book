from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages


def home(request):
	all_addresses = Address.objects.all
	return render(request, "home.html", {"all_addresses": all_addresses})

def add_address(request):
	if request.method == "POST":
		form = AddressForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Address Contact has been Added!!"))
			return redirect("home")
		else:
			messages.success(request, ("Some issue with the Data entered!!"))
			return render(request, "add_address.html")
	else:
		return render(request, "add_address.html", {})