from django.contrib.auth.models import User
from order.models import Order
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from user.models import Comment,Address, CreditCard,Wishlist,Response,RewardPoints
from product.models import Product
from order.models import *

# Create your views here.


class OrderPurchase(View):
    def get(seft, request):
        if request.user.is_authenticated:
            context={}
            detail =[]
            order =Order.objects.filter(user=request.user).order_by('-create_at').all()
            context['order'] = order
            for o in order:
                if OrderDetail.objects.filter(order=o,is_rating=False).count()==0:
                    o.is_rating = True
            # return HttpResponse(detail)
            return render(request,"user/purchase.html",context)

class AddressView(View):
    def get(seft,request):
      
        context={}
        addresses = Address.objects.filter(user=request.user)
        for add in addresses:
            add.address = add.ToString()
        context['address'] =addresses
      
        # return HttpResponse(addresses)
        return render(request,"user/address.html",context)
    def post(seft,request):
        address_id = request.POST.get('address_id')
        Address.objects.filter(user=request.user,default=True).update(default=False)
        Address.objects.filter(pk=address_id).update(default=True)
       
        return HttpResponse(1 ,"user:address")
class Add_Address(View):
    def post(seft,request):
        street =request.POST.get('street')
        apartment =request.POST.get('apartment')
        district =request.POST.get('district')
        city =request.POST.get('city')
        Address.objects.create(user= request.user, street= street,apartment_number= apartment,district=district,city=city)
        return HttpResponse(1)
class Edit_Address(View):
    def post(seft,request):
        id= request.POST.get('id')
        street =request.POST.get('street')
        apartment =request.POST.get('apartment')
        district =request.POST.get('district')
        city =request.POST.get('city')
        add =Address.objects.get(pk=id)
        add.street =street
        add.apartment_number=apartment
        add.district =district
        add.city=city
        add.save()
        return HttpResponse(1)
class Delete_Address(View):
    def post(seft,request):
        id= request.POST.get('id')
        add =Address.objects.get(pk=id)
        add.delete()
        return redirect("user:address")
        

        
class CommentProduct(View):
    def post(seft,request):
        if request.user.is_authenticated:
            product_id =request.POST.get('id_pro')
            order_id =request.POST.get('id_order')
            score =request.POST.get('score')
            comment =request.POST.get('comment')
            pro = Product.objects.get(id= product_id)

            Comment.objects.create(user = request.user, product=pro,comment=comment,rating=int(score),order_id=int(order_id))
            OrderDetail.objects.filter(order =Order.objects.get(pk=order_id),product=pro).update(is_rating=True)
            RewardPoints.objects.create(user=request.user,point=200,product_name = pro.title,product_thumbnail=pro.thumbnail)
            return HttpResponse(pro)
        # return HttpResponse(1)
class Profile(View):
    def get(self,request):
        return render(request,"user/profile.html")
    def post(self,request):
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        x = CustomerUser.objects.get(id=request.user.id)
        x.first_name= fn
        x.last_name=ln
        x.email= email
        x.phone_number=phone
        x.save()
        # .update(first_name=fn,last_name=ln,email=email,phone_number=phone)
    
        return redirect('user:profile')
class WishList(View):
    def get(self,request):
        wishlist = Wishlist.objects.filter(user=request.user)
        context={}
        context['wishlist'] = wishlist
        return render(request,'user/wishlist.html',context)
    def post(self,request):
        pro = request.POST.get('id_pro')
        item= request.POST.get('item_id')
      
        if item is not None:
            x=Wishlist.objects.filter(pk=item).delete()
            return HttpResponse(1)
        if pro is not None:
            pro1=Wishlist.objects.filter(user =request.user,product =Product.objects.get(pk=pro))
            if pro1.count() > 0:
                pro1.delete()
                return HttpResponse("delete_success")
            elif pro1.count()==0:
                Wishlist.objects.create(user=request.user,product=Product.objects.get(id=pro))
                return HttpResponse('true')

class Credits(View):
    def get(seft,request):
        context={}
        credits = CreditCard.objects.filter(user=request.user)
        if request.is_ajax():
            credits =list(CreditCard.objects.filter(user=request.user).values())
            return JsonResponse({"credit":credits},safe=False)
           
        context['credits'] =credits
        for cre in credits:
            cre.credit_card_number = cre.formatNumber()
        
        return render(request,'user/creditcard.html',context)
    def post(seft,request):
        is_default= request.POST.get('is_default')
        if is_default =='true':
             creditcard_id = request.POST.get('creditcard_id')
             CreditCard.objects.filter(user=request.user,default=True).update(default=False)
             CreditCard.objects.filter(pk=creditcard_id).update(default=True)
             return HttpResponse(1)
        else:
            name= request.POST.get('name')
            credit_number= request.POST.get('credit_number')
            expriration_date= request.POST.get('expriration_date')
            cvv= request.POST.get('cvv')
            credits = CreditCard.objects.create(user=request.user,credit_card_number=credit_number,expiration_date=expriration_date,cvv=cvv)
        return redirect('user:creditcard')
class Delete_CreditCard(View):
    def post(seft,request):
        id= request.POST.get('id')
        cred =CreditCard.objects.get(pk=id)
        cred.delete()
        return redirect("user:creditcard")
class Comments(View):
    def get(self,request):
        comments = Comment.objects.all()
        context={}
        context['comments']=comments
        return render(request,'user/manageRating.html',context)
    def post(seft,request):
        id_comment= request.POST.get('id_comment')
        response =request.POST.get('response')
        Response.objects.create(employee=request.user,comment=Comment.objects.get(pk=id_comment),response=response)
       
        return redirect('user:comments')

class RewardPointsView(View):
    def get(self, request):
        context={}
        listPoint =RewardPoints.objects.all().order_by("-id")
        context['listPoint'] = listPoint
        total=0
        for p in listPoint:
            total +=int(p.point)
        context['total']= total
        return render(request,"user/rewardpoints.html",context)
    