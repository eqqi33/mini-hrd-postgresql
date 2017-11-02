# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from karyawan.models import Karyawan
from kehadiran.models import Kehadiran

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def daftar_hadir(request):
    daftar_hadir = None

    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        daftar_hadir = Kehadiran.objects.filter(waktu__year=tahun, waktu__month=bulan, karyawan__id=request.session['karyawan_id'])

    return render(request, 'daftar_hadir.html', {'daftar_hadir':daftar_hadir})
