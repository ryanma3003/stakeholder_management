from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse

from .models import *
from .forms import *
import json

# Create your views here.
import base64
import hashlib
from Cryptodome.Cipher import AES
# from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

__key__ = hashlib.sha256(settings.AES_KEY).digest()

def encrypt(raw):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

    raw = base64.b64encode(pad(raw).encode('utf-8'))
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key= __key__, mode= AES.MODE_CFB,iv= iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(enc):
    unpad = lambda s: s[:-ord(s[-1:])]
    # unpad = lambda s: s[:-ord(s[len(s)-1:])]

    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(__key__, AES.MODE_CFB, iv)
    return unpad(base64.b64decode(cipher.decrypt(enc[AES.block_size:])).decode('utf-8'))

def showPass(request):
    check = request.user.check_password(request.POST['password'])

    if request.method == 'POST' and check:
        return HttpResponse(json.dumps({'success': check}), content_type="application/json")
    else :
        return HttpResponse(json.dumps({'success': check}), content_type="application/json")

class PhrasalwordUpdateView(UpdateView):
    model = Phrasalword
    form_class = PhrasalwordForm
    template_name = 'user/create.html'
    extra_context = {
        'title' : 'User Profile',
        'breadcrumb': 'Update'
    }

    def get_queryset(self):
        user = self.request.user
        obj, created = self.model.objects.get_or_create(
            user_id = user.id,
        )
        return super(PhrasalwordUpdateView, self).get_queryset()

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self.extra_context)
        if self.object.passphrase:
            kwargs['passphrase'] = decrypt(self.object.passphrase)

        self.kwargs.update({'passphrase' : kwargs['passphrase']})

        kwargs = self.kwargs
        return super(PhrasalwordUpdateView, self).get_context_data(*args, **kwargs)

    def form_valid(self, form):
        if self.request.POST.get('passphrase'):
            enc = self.request.POST.get('passphrase')
            encrypted = encrypt(enc)
            form.instance.passphrase = encrypted

        return super().form_valid(form)
