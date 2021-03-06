from django.forms import ModelForm
from django import forms
from kehadiran.models import Izin

class IzinForm(ModelForm):
    class Meta:
        model = Izin
        fields = ['jenis_kehadiran','waktu_mulai','waktu_berhenti','alasan']
        labels = {
                    'jenis_kehadiran':'Jenis Izin',
                    'waktu_mulai':'Waktu Mulai Izin',
                    'waktu_berhenti':'Waktu Berhenti Izin',
                    'alasan':'Alasan Izin',
        }
        error_message = {
                            'jenis_kehadiran':{
                                'required':'Anda harus memilih izin'
                            },
                            'waktu_mulai':{
                                'required':'Anda harus menentukan tanggal izin mulai'
                            },
                            'waktu_berhenti':{
                                'required':'Anda harus menentukan tangga izin berakhir'
                            },
                            'alasan':{
                                'required':'Alasan harus diisi agar dapat disetujui oleh HRD'
                            }
        }
        widgets = {
            'jenis_kehadiran':forms.Select(attrs={'class':'form-control'}),
            'waktu_mulai':forms.DateInput(attrs={'class':'form-control'}),
            'waktu_berhenti':forms.DateInput(attrs={'class':'form-control'}),
            'alasan':forms.Textarea(attrs={'class':'form-control','cols':50,'rows':10}),
        }