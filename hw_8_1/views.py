from django.shortcuts import get_object_or_404, redirect, render

from hw_8_1.forms import AddPersonForm
from hw_8_1.models import Person


def person(request):
    if request.method == "POST":
        form = AddPersonForm(request.POST, instance=Person())
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = AddPersonForm()
    return render(request, 'person.html', {'form': form})


def person_pk(request, pk):
    if request.method == "POST":
        person_p = get_object_or_404(Person, pk=pk)
        form = AddPersonForm(request.POST, instance=person_p)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        person_p = get_object_or_404(Person, pk=pk)
        form = AddPersonForm(instance=person_p)
        return render(request, 'person.html', {'form': form})
