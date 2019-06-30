from django.shortcuts import render, get_object_or_404
# To return an HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from .models import bitly
from .form import bitlyform, editBitly 
from .util import create_shortcode
import json
from datetime import datetime
from django.urls import reverse
# to use it as the dynamic urls
from django.contrib.auth.decorators import login_required

def index(request):
    objects= bitly.objects.all()[: :-1]
    print(objects)

    context={'objs': objects}

    return render(request, "index.html", context)

def create(request):
    form = bitlyform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.shortcode = create_shortcode()
        instance.datewise = "{}"
        instance.save()

        return HttpResponseRedirect(reverse('index'))

    context={"urlform":form}
    return render(request,"create.html",context)

def goto(request,shortcode=None):
    qs =get_object_or_404(bitly,shortcode__iexact=shortcode)
    if qs:
        instance =json.loads(qs.datewise)
        if str(datetime.now().date()) in instance:
            instance[str(datetime.now().date())]+=1
        else:
            instance[str(datetime.now().date())]=1
        qs.datewise = json.dumps(instance)
        qs.save()

    return HttpResponseRedirect(qs.long_url)

def update(request,pk=None):
    if request.user.is_authenticated:
        qs=get_object_or_404(bitly,id=pk)
        form=editBitly(request.POST or None,instance=qs)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context={'urlform':form}
        return render(request,"create.html",context)
    return HttpResponseRedirect(reverse('index'))

def delete(request,pk=None):
    if request.user.is_authenticated:
        qs=get_object_or_404(bitly,id=pk)
        qs.delete()
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
