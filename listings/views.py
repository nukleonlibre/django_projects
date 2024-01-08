from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})
def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})  


def listings_list(request):
    listings = Listing.objects.all()
    return render(request, 
                  'listings/listing_list.html',
                  {'listings': listings})
def listings_detail(request, id):
    listings = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listings': listings})




def about(request):
    return render(request, 
                  'listings/about.html')

def contact(request):
    return render(request, 
                  'listings/contact.html')

