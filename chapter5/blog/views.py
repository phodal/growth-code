from django.shortcuts import render_to_response, get_object_or_404

from blog.models import Blog


def blog_list(request):
    return render_to_response('blog/list.html', {
        'blogs': Blog.objects.all()
    })


def blog_detail(request, slug):
    return render_to_response('blog/detail.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })
