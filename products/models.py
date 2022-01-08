from django.db import models

# Create your models here.

class Menu(models.Model) :
    name = models.CharField(max_length=50)

    class Meta :
        db_table = 'menus'

class Category(models.Model) :
    name = models.CharField(max_length=20)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta :
        db_table = 'categories'

class Drink(models.Model) :
    korean_name = models.CharField(max_length=30)
    english_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Allergy_drink(models.Model) :
    allergy_id = models.CharField(max_length=30)
    drink_id = models.CharField(max_length=30)

    class Meta:
        db_table = 'Alergy_drink'

class Nutritions(models.Model) :
    one_serving_kca = models.CharField(max_length=30)
    sodium_mg= models.CharField(max_length=30)
    saturated_fat_g = models.CharField(max_length=30)
    sugars_g = models.CharField(max_length=30)
    protein_g = models.CharField(max_length=30)
    caffeine_mg = models.CharField(max_length=30)
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE)
    size = models.ForeignKey("Size", on_delete=models.CASCADE)

    class Meta:
        db_table = 'Nutritions'

class Image(models.Model) :
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Images'

class Allergy(models.Model) :
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'Allergy'

class Size(models.Model) :
    name = models.CharField(max_length=45)
    size_mi = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'Sizes'
