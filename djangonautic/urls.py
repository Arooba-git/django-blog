from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views, settings
from articles import views as article_views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about),
    path('', article_views.articles_list, name="home"),
    path('articles', include('articles.urls')),
    path('accounts', include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
