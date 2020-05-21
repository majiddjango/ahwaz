from django.shortcuts import render,redirect
from .models import About,Problem
from .forms import ProblemForm
# Create your views here.

from django.contrib import messages

def about_us(request):
    about = About.objects.first()
    context = {
        'about':about,
        'title': 'درباره ما',
    }

    return render(request,'home/about.html',context)



def report_to_us(request):
    form = ProblemForm(request.POST or None)
    title = 'ثبت نظر یا شکایت'

    if request.POST:
        if form.is_valid():
            p = form.save(commit=False)
            user = request.user
            if user.is_authenticated:
                p.owner = user
            form.save(commit=True)
            messages.success(request,'نظر شما با موفقیت ثبت شد.')
            return redirect('home')
        else:
            messages.error(request,'لطفا مجددا تلاش نمایید.')
            return render(request,'home/report.html',locals())

    else:
        return render(request,'home/report.html',locals())
