from django.urls import path

from .views import index, top_sellers,advertisement_post,CustomLoginView

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='adv_post'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
