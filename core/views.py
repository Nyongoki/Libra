from django.contrib import messages
from django.shortcuts import redirect, render

from core.forms import BookForm


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book registered successfully.')
            return redirect('book_create')
    else:
        form = BookForm()

    return render(request, 'core/book_form.html', {'form': form})
