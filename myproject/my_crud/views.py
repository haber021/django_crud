from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm

# Create
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)  # Add request.FILES to handle image upload
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'mycrud/item_form.html', {'form': form})

# Read
def item_list(request):
    items = Item.objects.all()
    return render(request, 'mycrud/item_list.html', {'items': items})

# Update
# Update Item
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    # Handle the form and ensure it can accept file uploads
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)  # Add request.FILES to handle image
        if form.is_valid():
            form.save()  # Save the form and update the item (including the image)
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'mycrud/item_form.html', {'form': form})

# Delete
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'mycrud/item_confirm_delete.html', {'item': item})
