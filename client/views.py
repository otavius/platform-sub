from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from writer.models import Article
from . models import Subscription

# Create your views here.
@login_required(login_url="my-login")
def client_dashboard(request):
    try:
        sub_details = Subscription.objects.get(user=request.user)
        subscription_plan = sub_details.subscription_plan
        context = {"sub_plan": subscription_plan}
        return render(request, "client/client-dashboard.html", context)
    except:
        subscription_plan = "None"
        context = {"sub_plan": subscription_plan}
        return render(request, "client/client-dashboard.html", context)

@login_required(login_url="my-login")
def browse_articles(request):
    try:
        sub_details = Subscription.objects.get(user=request.user, is_active=True)
    except:
        return render(request, "client/subscription-locked.html")
    
    current_subscription_plan = sub_details.subscription_plan
    if current_subscription_plan == "Standard":
        articles = Article.objects.all().filter(is_premium=False)
    elif current_subscription_plan == "Premium":
        articles = Article.objects.all()

    context = {"AllClientArticles":articles}
    return render(request, "client/browse-article.html", context)

@login_required(login_url="my-login")
def subscription_locked(request):

    return render(request, "client/subscription-locked.html")


    