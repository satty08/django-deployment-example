from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import FormName
# Create your views here.
def index(request):
    return render (request, 'Apptwo/help.html' )
def users(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ('Error: Form Invalid')
    return render(request,'AppTwo/satyam.html', {'form':form})


    # user_list = User.objects.order_by('fname')
    # user_dict = {'users': user_list}
    # return render(request, 'AppTwo/satyam.html', context = user_dict)






# def help(request):
#     dic={'help_insert': 'You are on the help page'}
#     return render(request, 'AppTwo/help.html', context= dic)
