from django.shortcuts import render
from .models import Post, Comment


def post_list_view(request):
    ctx = {}
    ctx['post_list'] = Post.objects.all()

    return render(request, 'core/post_list.html', ctx)

def post_detail_view(request, slug):
    ctx = {}
    post = Post.objects.filter(slug=slug).first()
    comment = Comment.objects.all()
    if post:
        ctx['post'] = post
        ctx['comments'] = comment
    return render(request, 'core/post_detail.html', ctx)

# Переписать на функции >>
# class PostList(generic.ListView):
#     queryset = Post.objects.order_by('-created_on')
#     template = 'core/post_list'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name= 'post_detai;.html'

# def post_list(request):
#     return render(request, 'core/post_list.html', {})