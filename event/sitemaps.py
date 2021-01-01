from django.contrib.sitemaps import Sitemap
from .models import Event


class EventSitemap(Sitemap):
    changefreq = 'never'
    priority = .5
    protocol = 'https'
    
    def items(self):
        return Event.objects.filter(published=True)
    
    def location(self, instance):
        try:
            return f'/etkinlik/{instance.slug}'
        except:
            return 'bir şeyler çok fena ters gitti'
    