from django.shortcuts import render, redirect
from .models import user,transec
from django.contrib import messages
# Create your views here.

def home(request):
    context=user.objects.all()
    # print(context.username)
    return render(request,'index.html',{'context':context})

def viewProfile(requst,uid):
    user_got=user.objects.get(id=uid)
    return render(requst,'viewProfile.html',{'user_got':user_got})

def transection(request,uid):
    context=user.objects.all().exclude(id=uid)
    return render(request,'transection.html',{'context':context,'senderid':uid})

def transferBal(request,uid,senderid):
    sender=user.objects.get(id=senderid)
    receiver=user.objects.get(id=uid)
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))
        if sender.balance > amount:
            sender.balance = sender.balance-amount
            sender.save()
            receiver.balance = receiver.balance+amount
            receiver.save()
            transect = transec(senderName=sender.username, receiver=receiver.username, amount=amount)
            transect.save()
            messages.add_message(request, messages.INFO, 'Transection Done')
        else:
            # messages.error(request, 'Not enough balance')
            messages.add_message(request, messages.INFO, 'Not enough Balance')
    return render(request,'tranferBal.html',{'sender':sender,'receiver':receiver})

def all_transections(request):
    context=transec.objects.all()
    # print(context.username)
    return render(request,'all_transections.html',{'context':context})


def index(request):
    return redirect('home')