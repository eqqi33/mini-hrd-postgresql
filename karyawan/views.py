from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from karyawan.models import Karyawan


@login_required(login_url=settings.LOGIN_URL)
def profil(request):
    if 'username' in request.session:
        karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
        return render(request, 'new/profil.html', {"karyawan": karyawan})
    else:
        return render(request, 'login.html', {})

@login_required(login_url=settings.LOGIN_URL)
def ganti_foto(request):
    karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
    karyawan.foto = request.FILES['files']
    karyawan.save()

    return redirect('/')