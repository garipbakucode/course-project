from typing import Any, Dict
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Blog, Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import BlogForm


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blogs.html'
    queryset = Blog.objects.all().order_by('-published_at')
    context_object_name = 'blogs'
    paginate_by = 2


# def blog_list(request):
#     blogs = Blog.objects.all().order_by('-published_at')
#     context = {
#         'blogs': blogs,
#     }
#     return render(request, 'blog/blogs.html', context)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog-detail.html'

    def get_context_data(self, **kwargs: Any):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['last_blogs'] = Blog.objects.all().order_by('-published_at')[:4]
        context['categories'] = Category.objects.all()
        return context



# def blog_detail(request, slug):
#     blog = Blog.objects.get(slug=slug)
#     last_blogs = Blog.objects.all().order_by('-published_at')[:4]
#     categories = Category.objects.all()
#     context = {
#         'blog': blog,
#         'last_blogs': last_blogs,
#         'categories': categories,
#     }
#     return render(request, 'blog/blog-detail.html', context)


class CreateBlogView(LoginRequiredMixin, generic.CreateView):
    template_name = 'blog/create.html'
    model = Blog
    success_url = reverse_lazy('blogs')
    form_class = BlogForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class UpdateBlogView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'blog/create.html'
    model = Blog
    success_url = reverse_lazy('blogs')
    form_class = BlogForm


class DeleteBlogView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')


def delete_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    return redirect('blogs')

# def create_blog(request):
#     form = BlogForm()
#     if request.method == 'POST':
#         form = BlogForm(request.POST or None, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.author = request.user
#             obj.save()
#             return redirect('blogs')

#     context = {
#         'form': form,
#     }
#     return render(request, 'blog/create.html', context)