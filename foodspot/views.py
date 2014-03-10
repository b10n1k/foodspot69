from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, redirect, render,render_to_response
from foodspot.models import Food,Offer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def main(request):
    
    menu_beer = Food.objects.filter(category=4)
    menu_crepe = Food.objects.filter(category=2)
    menu_club = Food.objects.filter(category=1)
    menu_spaggetti = Food.objects.filter(category=8)
    menu_burgers = Food.objects.filter(category=11)
    menu_hotdog = Food.objects.filter(category=1)
    menu_salads = Food.objects.filter(category=7)
    menu_toast = Food.objects.filter(category=3)
    menu_dessert = Food.objects.filter(category=6)
    menu_coffee = Food.objects.filter(category=9)
    menu_soda = Food.objects.filter(category=5)
    menu_food = Food.objects.filter(category=1)
    
    menu_offer = Offer.objects.all()

    

    return render(request,'main.html',{'view_title':"Menu",
                                       'menu_crepe':menu_crepe,
                                       'menu_club':menu_club,
                                       'menu_spaghetti':menu_spaggetti,
                                       'menu_burgers':menu_burgers,
                                       'menu_hotdog':menu_hotdog,
                                       'menu_salads':menu_salads,
                                       'menu_toast':menu_toast,
                                       'menu_dessert':menu_dessert,
                                       'menu_coffee':menu_coffee,
                                       'menu_soda':menu_soda,
                                       'menu_beer':menu_beer,
                                       'menu_offer':menu_offer
                                   })
    
def profile(request):
    return render(request,'profile.html')

@csrf_exempt
def order(request):
    getobject=None
    if request==request.POST:
        sItem=int(request.POST.get('itemId'))
        #it=int(sItem['itemId'])
        getobject=Food.objects.get(id=sItem)
        
        #selectedItem=json.dumps(getobject)
    return render_to_response('main.html',{'objects':getobject})

