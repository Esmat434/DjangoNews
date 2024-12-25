from django.utils.deprecation import MiddlewareMixin
from .models import PageView

class PageViewMiddleware(MiddlewareMixin):
    def process_view(self,request,view_fun,view_args,view_kwargs):
        page_name = request.path
        ip = request.META.get('REMOTE_ADDR')
        if not page_name.startswith('/admin'):
            page,created = PageView.objects.get_or_create(ip=ip,page_name=page_name)
            page.view_count = 1
            page.save()
        return None