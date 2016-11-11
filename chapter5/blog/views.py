from django.shortcuts import render_to_response

from blog.models import Blog


def blog_list(request):
    return render_to_response('blog/list.html', {
        'blogs': Blog.objects.all()[:5]
    })
