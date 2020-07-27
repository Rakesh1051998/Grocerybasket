from django.shortcuts import render
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required
from .models import MessageForm
from .models import FeedbackForm
from .models import cart




# Create your views here.
def home(req):
    return render(req,"index.html") 
 
def about(req):
    return render(req,"about.html") 


def contacts(req):
    if req.method == 'POST':
        Name= req.POST.get('Name')
        Contact_no= req.POST.get('Contact_no')
        Email_id= req.POST.get('Email_id')
        Message= req.POST.get('Message')
        
        m=MessageForm(Name=Name,Contact_no=Contact_no,Email_id=Email_id,Message=Message)
        m.save()
        return render(req,"contacts.html")
    
    else:
        return render(req,"contacts.html")

def offers(req):
    return render(req,"offers.html")  


def products(req):
    return render(req,"products.html") 

def terms(req):
    return render(req,"terms.html")  

def feedback(req):
    if req.method == 'POST':
        Name= req.POST.get('Name')
        Contact_no= req.POST.get('Contact_no')
        Email_id= req.POST.get('Email_id')
        Comment= req.POST.get('Comment')
        
        f=FeedbackForm(Name=Name,Contact_no=Contact_no,Email_id=Email_id,Comment=Comment)
        f.save()
        return render(req,"feedback.html")
    
    else:
        return render(req,"feedback.html") 
    

def explore(req): 
    if req.method == 'POST':
       product_name1= req.POST.get('product_name')
       type1= req.POST.get('product_type')      
       brand1= req.POST.get('brand') 
       price1= req.POST.get('price')
       quantity1= req.POST.get('quantity')
       units1= req.POST.get('units')
        
       g=cart(product_name=product_name1,type=type1,brand=brand1,price=price1,quantity=quantity1,units=units1)  
       g.save()  
       return render(req,"explore.html") 
    
    else:
         return render(req,"explore.html") 
 

def Grains(req):
    return render(req,"Grains.html") 

def Pulses(req):
    return render(req,"Pulses.html") 

def rice(req):
    return render(req,"rice.html")

def wheat(req):
    return render(req,"wheat.html") 

def cart(req):
    
    return render(req,"cart.html")  
 


 




