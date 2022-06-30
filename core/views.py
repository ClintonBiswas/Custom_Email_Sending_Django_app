from django.shortcuts import render, HttpResponse
from .forms import PersonForm
from .models import Person
from django.core.mail import send_mail
# Create your views here.
def Home(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        # print(name)
        if form.is_valid():
            send_mail(
            f"Hi, {name}",
            'Thanks For Subscription',
            'hdclintonb@gmail.com',
            [f'{email}'],
            fail_silently=False,
            )
            form.save()
            return HttpResponse('Thanks for subscription')
    dict = {'form': form}
    return render(request, 'home.html', context=dict)