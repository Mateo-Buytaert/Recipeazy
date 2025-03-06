from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("recipe-list", views.recipe_list, name="recipe_list"),
    path("make-recipe", views.recipe_create,name="recipe-create"),
    path("recipe-list/<int:id>", views.recipe_detail,name="recipe-detail"),
    path("recipe-list/", views.search_recipe, name="search-recipe"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)