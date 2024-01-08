from django.shortcuts import render,redirect
from .registrationPage import registrationForm

# Create your views here.
def registration_form(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            return redirect('otp_page')
    else:
        form = registrationForm()
    return render(request,'memberRegistration/registrationForm.html',{'form'}:form)

def otp_page(request):
    return render(request, 'otpPage.html')