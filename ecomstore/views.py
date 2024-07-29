from django.shortcuts import render
from django.template import RequestContext

def page_not_found_404(req, exception):
    page_title = 'page_not_found'
    
    req_ctx = RequestContext

    context = locals()

    return render(req, '404.html', context)