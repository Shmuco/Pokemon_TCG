from django.shortcuts import render
from .models import *
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import *
from django.http import HttpResponseRedirect



# Create your views here.

def all (request):
    posts = Post.objects.all()
    print(posts)

    return render(request, 'forum_homepage.html', {'posts':posts})



class NewPost(generic.CreateView):
    template_name = 'new_post.html'
    model = Post
    fields = ('title', 'content')
    success_url = reverse_lazy('all')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



def single_post(request, post_id):

    post = Post.objects.get(id = post_id)
    comments = Comment.objects.filter(post = post.id)
    form = CommentForm
    if request.method == "POST":
    
            form = CommentForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.creator = request.user
                f.post = post
                f.save()
                return HttpResponseRedirect(request.path_info)

    return render(request,'single_post.html', {'post': post, 'comments':comments, 'form':form})


class DeletePost(generic.DeleteView):
    model = Post
    print('working')
    success_url = reverse_lazy('all')


class DeleteComment(generic.DeleteView):
    model = Comment
    print('working')
    success_url = reverse_lazy('single_post')
    
    def get_success_url(self):
        return reverse('single_post', kwargs={'int': int(self.object.post.id)})
    