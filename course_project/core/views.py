from django.shortcuts import render

from blog.models import Blog
from .models import HomePage, BelowBanner, About, ClientFeedback


def index(request):
    banner = HomePage.objects.first()
    below_banners = BelowBanner.objects.all()
    about = About.objects.first()
    client_feedbacks = ClientFeedback.objects.all()
    blogs = Blog.objects.all().order_by('-published_at')[:3]
    context = {
        'banner': banner,
        'below_banners': below_banners,
        'about': about,
        'blogs': blogs,
        'client_feedbacks': client_feedbacks,
    }
    return render(request, 'home/index.html', context)


def about(request):
    about = About.objects.first()
    context = {
        'about': about,
    }
    return render(request, 'about/index.html', context)