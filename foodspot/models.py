from django.db import models
import datetime


class Profile(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    phone_home=models.CharField(max_length=30)
    phone_mobile=models.CharField(max_length=30)
    email=models.EmailField()
   # favorites=models.ManyToMany(Favorites)
   # order=models.ForeignField(Order)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name,self.last_name)

    class Meta:
        verbose_name_plural='Profiles'

class Favorites(models.Model):
    #profile=mode
    pass

class Category(models.Model):
    CATEG_LIST={
        ('Crepe','Crepe'),
        ('Club Sandwich','Club Sandwich'),
        ('Spaghetti','Spaghetti'),
        ('Sandwich','Sandwich'),
        ('Burger','Burger'),
        ('Salad','Salad'),
        ('Toast','Toast'),
        ('IceCream','IceCream'),
        ('Coffee','Coffee'),
        ('Dessert','Dessert'),
        ('Drinks','Drinks'),
        ('Soft Drinks','Soft Drinks'),
        ('Beer','Beer'),
        ('Wine','Wine')
        
    }

    category_title=models.CharField(max_length=35,choices=CATEG_LIST,default='Crepe',unique=True)

    def __unicode__(self):
        return self.category_title

    class Meta:
        verbose_name_plural='Categories'
        ordering=['category_title']

class SubCategory(models.Model):
    category=models.ForeignKey(Category)
    sub_title=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.sub_title

    class Meta:
        ordering=['sub_title']
        verbose_name_plural='Sub Categories'

class Food(models.Model):
    title=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    category=models.ForeignKey(Category)
    description=models.TextField(blank=True)
    
    def __unicode__(self):
        return "%d - %s " % (self.price,self.title)
        
    class Meta:
        ordering=['category']


class Topping(models.Model):
    topping_name=models.CharField(max_length=30)
    topping_description=models.TextField()
    topping_price=models.DecimalField(max_digits=4,decimal_places=2)
    
    def __unicode__(self):
        return "%s" % self.topping_name
   
class Offer(models.Model):
    foodspot_offer=models.CharField(max_length=200)
    foodspot_offer_price=models.DecimalField(max_digits=4,decimal_places=2)
    foodspot_offer_description=models.CharField(max_length=100, null=True, blank=True)

    def get_offer(self):
        return (foodspot_offer, foodspot_offer_price)
        
    def __unicode__(self):
        return self.foodspot_offer

    class Meta:
        verbose_name_plural='Offers'

class Photo(models.Model):
    #caption=models.CharField(max_length=200)
    #image=models.ImageField(upload_to='images')
    pass

class Menu(models.Model):
    pass


class Choise(models.Model):
    choise=models.ForeignKey(Menu)


class Order(models.Model):
    order_profile=models.ForeignKey(Profile)
    order_choises=models.ForeignKey(Choise)
    order_date=models.DateTimeField(auto_now_add=True)
    order_status=models.BooleanField(default=False)
    
    class Meta:
        ordering=['order_date']

    def __unicode__(self):
        pass
