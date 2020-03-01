"""ksiegarnia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from account.views import(
  
    customer_profile_view,
    logout_view,
    login_view,
)
from cart.views import(
    add_to_cart,
    add_oder_view,
    cart_summary_view,
    )
from books.views import(
    show_books_view,
    add_book_view,
    show_oders_view,
    book_view,
    search_book_view,
    show_books_view_category,
    )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_books_view,name="home"),
    path('register/', customer_profile_view,name="register"),
    path('logout/', logout_view,name="logout"),
    path('login/', login_view,name="login"),
    url(r'^add-to-cart/(?P<bookid>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    path('addorder/', add_oder_view,name="addorder"),
    path('addbook/', add_book_view,name="addbook"),
    path('orders/', show_oders_view,name="orders"),
    url(r'^book/(?P<bookid>[-\w]+)/$', book_view, name="book"),
    path('search/', search_book_view,name="search"),
    url(r'^category/(?P<category>[-\w]+)/$', show_books_view_category, name="category"),
    path('summary/', cart_summary_view,name="summary"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
