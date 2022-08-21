from blog.forms import PostForm
from blog.models import Post, Category
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
# Create your views here.

class CreatePost(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = "blog/create_post.html"
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        if self.object.draft == True:
            messages.success(self.request, "Post Saved as Draft!")
        else:
            messages.success(self.request, "Post Published Successfully!")
        return super().get_success_url()

    def test_func(self):
        return self.request.user.is_doctor == True

class ListPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = dict()
        categories = Category.objects.all()
        context["items"] = dict()
        for category in categories:
            lst = category.category.filter(draft=False)
            if len(lst) != 0:
                context["items"][category] = lst
        return context

class MyList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_doctor == True
    model = Post
    template_name = "blog/doctor_post.html"

    def get_context_data(self, **kwargs):
        context = dict()
        context["post_list"] = Post.objects.filter(author=self.request.user)
        return context

class Publish(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request):
        id = int(request.POST.get("id"))
        post = Post.objects.get(id=id)
        if post.author != request.user:
            return redirect(reverse_lazy("accounts:index"))
        post.draft = False
        post.save()
        messages.success(request, "Post Published Successfully!")
        return redirect(reverse_lazy("blog:my-post"))

    def test_func(self):
        return self.request.user.is_doctor == True