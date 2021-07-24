from django.shortcuts import redirect, render, HttpResponse
from .models import Company, Review

# Create your views here.
def index(request):
    company = Company.objects.all()
    print(company)

    params = {
        'company': company
    }
    return render(request, 'index.html', params)

def review(request, id):
    Comapany_review = Company.objects.filter(id=id)
    review = []
    catprods= Review.objects.values('company', 'id')
    cats = {item['company'] for item in catprods}
    for cat in cats:
        prod = Review.objects.filter(category=cat)
        review.append(prod)
    params = {
        'reviews':review
    }
    return render(request, 'review.html', {'comapany_review':Comapany_review,}, params)

def review_rate(request):
    if request.method== 'GET':
        prod_id = request.GET.get('prod_id')
        company = Company.objects.get(id = prod_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user = request.user
        Review(user=user,company = company,comment=comment,rate=rate).save()
        return redirect('review', id = prod_id)

def delete(request, id):
    rev = Review.objects.get(id=id)
    rev.delete()
    return redirect('/')