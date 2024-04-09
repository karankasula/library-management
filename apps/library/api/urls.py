from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.library.api.views import BookViewSet, LibraryViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'libraries', LibraryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('books/search/', BookViewSet.as_view({'get': 'search'}), name='search_book'),
]
