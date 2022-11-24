from django.db import models

# модель маршрут перевозки
class Itinerary(models.Model):
    title = models.CharField(max_length=200)  # поле название маршрута

    def __str__(self):
        return self.title

# модель контактное лицо
class Person(models.Model):
    contact_person = models.CharField(max_length=200) # поле контактное лицо

    def __str__(self):
        return self.contact_person

# модель груз
class Cargo(models.Model):
    cargo = models.CharField(max_length=200) # поле наименование груза

    def __str__(self):
        return self.cargo

# модель вес
class Weight(models.Model):
    weight = models.FloatField() # поле вес

    def __str__(self):
        return str(self.weight)

# модель обьем
class Volume(models.Model):
    volume = models.IntegerField() # поле обьем

    def __str__(self):
        return str(self.volume)

# модель налог
class Tax(models.Model):
    tax = models.CharField(max_length=50) # поле налог НДС

    def __str__(self):
        return self.tax

# Модель тип загрузки
class Typeofloading(models.Model):
    typeofloading = models.CharField(max_length=100) # поле тип загрузки
    def __str__(self):
        return self.typeofloading

# Модель тип выгрузки
class Typeofunloading(models.Model):
    typeofunloading = models.CharField(max_length=100) # поле тип выгрузки
    def __str__(self):
        return self.typeofunloading

# Модель валюта
class Currency(models.Model):
    currency = models.CharField(max_length=20) # поле валюта
    def __str__(self):
        return self.currency


# Основная модель актуальный груз
class Actual(models.Model):
    title2 = models.CharField(max_length=200)  # маршрут перевозкиd
    date_of_transportation = models.DateField()  # поле дата загрузки
    itinerary = models.ForeignKey('Itinerary', on_delete=models.CASCADE)  # поле маршрут перевозки
    customers_contact_person = models.ForeignKey('Person', on_delete=models.CASCADE)  # поле контактное лицо заказчика
    cargos = models.ForeignKey('Cargo', on_delete=models.CASCADE) # поле груз
    price = models.CharField(max_length=20) # поле цена
    currency= models.ForeignKey('Currency', on_delete=models.CASCADE) # поле валюта
    taxes = models.ForeignKey('Tax', on_delete=models.CASCADE) # поле налог
    weight = models.ForeignKey('Weight', on_delete=models.CASCADE) # поле вес
    volume = models.ForeignKey('Volume', on_delete=models.CASCADE) # поле обьем
    typesofloading = models.ForeignKey('Typeofloading', on_delete=models.CASCADE) # поле тип загрузки
    typesofunloading = models.ForeignKey('Typeofunloading', on_delete=models.CASCADE) # поле тип выгрузки
    note = models.TextField()  # поле примечание по отгрузке

    def __str__(self):
        return self.title2
