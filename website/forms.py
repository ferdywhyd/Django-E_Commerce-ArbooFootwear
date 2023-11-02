from django import forms
from django.forms import ModelForm
from .models import Karyawan

class AddKaryawanForm(ModelForm):
    class Meta:
        model = Karyawan
        fields = ('__all__')
        label = ""
        widgets = {
            'nama' : forms.TextInput(attrs={'class':'min-h-[auto] bg-transparent px-3 py-[0.32rem] leading-[1.6] rounded border mb-3 ml-10'}),
            'pekerjaan' : forms.Select(attrs={'class':'rounded border mb-3 ml-10'}),
            'alamat' : forms.TextInput(attrs={'class':'min-h-[auto] bg-transparent px-3 py-[0.32rem] rounded border mb-3 ml-8'}),
            'no_hp' : forms.TextInput(attrs={'class':'min-h-[auto] bg-transparent px-3 py-[0.32rem] rounded border mb-3 ml-10'})
        }

# class AddFormGajian(ModelForm):
#     class Meta:
#         model = Gajian
#         fields = ('__all__')