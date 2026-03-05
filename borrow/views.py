from django.shortcuts import render, redirect, get_object_or_404
from .models import BorrowRecord
from .forms import BorrowForm

# Borrow List (Read)
def borrow_list(request):
    records = BorrowRecord.objects.all()
    return render(request, 'borrow/borrow_list.html', {'records': records})

# Create Borrow Record (Create)
def borrow_create(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
    else:
        form = BorrowForm()
    return render(request, 'borrow/borrow_form.html', {'form': form})

# Update Borrow Record (Update)
def borrow_update(request, pk):
    record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == 'POST':
        form = BorrowForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
    else:
        form = BorrowForm(instance=record)
    return render(request, 'borrow/borrow_form.html', {'form': form})

# Delete Borrow Record (Delete)
def borrow_delete(request, pk):
    record = get_object_or_404(BorrowRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('borrow_list')
    return render(request, 'borrow/borrow_confirm_delete.html', {'record': record})

    