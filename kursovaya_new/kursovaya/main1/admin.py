# Регистрация моделей
from django.contrib import admin
from .models import* # импорт всех созданных моделей
admin.site.register(Itinerary)
admin.site.register(Person)
admin.site.register(Cargo)
admin.site.register(Actual)
admin.site.register(Tax)
admin.site.register(Typeofloading)
admin.site.register(Typeofunloading)
admin.site.register(Currency)
admin.site.register(Weight)
admin.site.register(Volume)

