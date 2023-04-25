from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls.base import reverse_lazy
from .models import Feedback
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index_success(request):
    return render(request, "feedback/index_success.html")

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Feedback
    fields = ['topic', 'rating', 'good', 'bad', 'ideas']
    template_name = "feedback/index.html"
    success_url = reverse_lazy('feedback:index_success')
