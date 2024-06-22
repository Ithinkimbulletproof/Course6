from django.shortcuts import render, get_object_or_404, redirect
from .models import Newsletter
from .forms import NewsletterForm

def create_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter_list')
    else:
        form = NewsletterForm()
    return render(request, 'create_newsletter.html', {'form': form})

def newsletter_list(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'newsletter_list.html', {'newsletters': newsletters})

def update_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, instance=newsletter)
        if form.is_valid():
            form.save()
            return redirect('newsletter_list')
    else:
        form = NewsletterForm(instance=newsletter)
    return render(request, 'update_newsletter.html', {'form': form})

def delete_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        newsletter.delete()
        return redirect('newsletter_list')
    return render(request, 'delete_newsletter.html', {'newsletter': newsletter})
