from django.contrib.sitemaps import Sitemap
from wagtail.models import Page





class WagtailSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Page.objects.live().public()

    def lastmod(self, obj):
        return obj.latest_revision_created_at

    def location(self, obj):
        # Trả về URL đầy đủ với domain là maihoadichquan.vn
        return "https://maihoadichquan.vn" + obj.url


