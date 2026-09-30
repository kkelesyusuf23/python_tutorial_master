"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include # SEBEP: Diğer dosyaları (departmanları) içeri aktarmak için include fonksiyonunu ekledik.

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # SEBEP: Ana resepsiyona (config/urls.py) gelen ve tarayıcıda "api/" ile başlayan tüm istekleri
    # "todo" departmanının kendi resepsiyonuna (todo/urls.py) yönlendiriyoruz.
    path('api/', include('todo.urls')),
]
