from django.shortcuts import render,redirect
from .models import Product,ProductSubcategory

# Create your views here.
def add_product(request):
    return render(request, 'add_product_list.html')

def add_product_subcategory(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        product_price = request.POST.get('product_price')
        product_image = request.FILES.get('product_image')
        product_model = request.POST.get('product_model')
        product_ram = request.POST.get('product_ram')

        product = Product.objects.get(pk=product_id)

        ProductSubcategory.objects.create(
            product=product,
            product_price=product_price,
            product_image=product_image,
            product_model=product_model,
            product_ram=product_ram,
        )  
        return redirect('product_subcategory_list')
    
    products = Product.objects.all()

    return render(request, 'add_product_list.html',{'products':products})

def update_product_subcategory(request,product_subcategory_id):
    if request.method == 'POST':
        existing_product = ProductSubcategory.objects.get(id=product_subcategory_id)
        existing_product.product = request.POST['product']
        existing_product.product_price = request.POST['product_price']
        existing_product.product_image =  request.FILES['product_image']
        existing_product.product_model = request.POST['product_model']
        existing_product.product_ram = request.POST['product_ram']

        existing_product.save()

        return redirect('product_subcategory_list')
    
    getproduct = ProductSubcategory.objects.get(id=product_subcategory_id)
    context = {
        'product':getproduct.product,
        'product_price':getproduct.product_price,
        'product_image': getproduct.product_image,
        'product_model':getproduct.product_model,
        'product_ram':getproduct.product_ram,
    }
    return render(request,'update_product.html',context)


def delete_product_subcategory(request, product_subcategory_id):
    delete_product_subcategory = ProductSubcategory.objects.get(id=product_subcategory_id)
    delete_product_subcategory.delete()
    return redirect('product_subcategory_list')



def product_subcategory_list(request):
    product_subcategories = ProductSubcategory.objects.all()
    return render(request,'product_subcategory_list.html',{'product_subcategories':product_subcategories})  