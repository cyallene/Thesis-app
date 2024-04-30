from django.shortcuts import render, get_object_or_404
from .models import Thesis

def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request, 'thesis/thesis_list.html', {'theses': theses})

def thesis_detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, pk=thesis_id)
    return render(request, 'thesis/thesis_detail.html', {'thesis': thesis})

def thesis_form(request):
    if request.method == 'POST':
        # Process form data here
        pass
    else:
        # Render the form template here
        pass  # Ensure this 'pass' is at the same indentation level as the 'if' statement above
