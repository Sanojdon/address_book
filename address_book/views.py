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

def edit(request, list_id):
	if request.method == "POST":
		record = Address.objects.get(pk=list_id)
		form = AddressForm(request.POST or None, instance=record)
		if form.is_valid():
			form.save()
			messages.success(request, ("Address Contact has been Editted!!"))
			return redirect("home")
		else:
			messages.success(request, ("Some issue with the Data updated!!"))
			return render(request, "edit.html", {"get_address" : record})
	else:
		record = Address.objects.get(pk=list_id)
		return render(request, "edit.html", {"get_address" : record})

def delete(request, list_id):
	if request.method == "POST":
		record = Address.objects.get(pk=list_id)
		record.delete()
		messages.success(request, ("Address Contact has been Deleted!!"))
		return redirect("home")
	else:
		messages.success(request, ("Some issue with Deletion!!"))
		return redirect("home")