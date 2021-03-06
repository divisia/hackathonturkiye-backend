from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    protocol = 'https'
    
    def items(self):
        return Post.objects.filter(status='p')
    
    def location(self, instance):
        try:
            return f'/blog/{instance.slug}'
        except:
            return 'bir şeyler çok fena ters gitti'
    
    def lastmod(self, instance):
        try:
            return instance.edited_at
        except:
            return None
    