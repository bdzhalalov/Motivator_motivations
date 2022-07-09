from django.shortcuts import render, redirect
from .forms import MotivationForm
from .models import Motivation
from django.core.paginator import Paginator
from django.views.generic import CreateView


def list(request):
    motivations = Motivation.objects.all()
    paginator = Paginator(motivations, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main.html', {'page_obj': page_obj})


def random_motivation(request):
    random_motivation = Motivation.objects.all().order_by('?')[:1]
    return render(request, 'home.html', {'random_motivation': random_motivation})


class MotivationView(CreateView):
    template_name = 'post.html'

    def get(self, request):
        form = MotivationForm
        context = {
            'form': form    
        }
        return render(request, self.template_name, context)
        
    def post(self, request):
        form = MotivationForm(request.POST)
        
        if form.is_valid():
            motivation = form.save(commit=False)
            motivation.nickname = request.user
            motivation.save()
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
