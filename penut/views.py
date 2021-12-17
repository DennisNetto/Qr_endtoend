from django.shortcuts import render
from django.http import HttpResponse
from .models import HumanStorage, TokenStorage
from .forms import CreateNewEntry, CreateNewQR

import os
import base64
from .ebcryt import cryupt
from .qr import qrpic
import hashlib
import shutil


# Create your views here.


def removedir(a):
    shutil.rmtree(a)


def removefile(a):
    os.remove(a)


def index(response):
    return HttpResponse('hello')


def qrpi(request):
    return HttpResponse("test")


def createqr(request):
    try:
        qry = TokenStorage.objects.get(id_number=27461501745267184763129481)
        print(qry)
        return HttpResponse("test")

    except TokenStorage.DoesNotExist:
        return HttpResponse("test")


def create(response):
    if response.method == "POST":
        form = CreateNewEntry(response.POST)

        if form.is_valid():
            n = form.cleaned_data["id_number"]
            a = form.cleaned_data["First_name"]
            m = form.cleaned_data["Last_name"]
            e = form.cleaned_data["DOB"]
            t = HumanStorage(id_number=n, First_name=a, Last_name=m, DOB=e)
            t.save()

    else:
        form = CreateNewEntry()
    return render(response, "penut/create.html", {"form": form})


def create1(response):
    if response.method == "POST":
        form = CreateNewQR(response.POST)

        if form.is_valid():
            num = form.cleaned_data["id_number"]
            fname = form.cleaned_data["First_name"]
            lname = form.cleaned_data["Last_name"]
            edob = form.cleaned_data["DOB"]
            a = "./tmp" + num
            qry = HumanStorage.objects.get(id_number=num)
            qfn = qry.First_name
            qln = qry.Last_name
            qdb = qry.DOB
            qdb = str(qdb)
            if fname == qfn and lname == qln and edob == qdb:
                try:
                    TokenStorage.objects.get(id_number=num)
                    qrpic(num)
                    with open(r'C:\Users\Maker\Desktop\djangoProject\27461501745267184763129482.jpeg', "rb") as f:
                        return HttpResponse(f.read(), content_type="image/png")
                except TokenStorage.DoesNotExist:
                    hash = hashlib.sha256()
                    num1 = bytes(num, 'utf-8')
                    hash.update(num1)
                    hash1 = (hash.hexdigest())
                    h = str(hash1)
                    cryupt(num, fname, lname, edob)
                    with open(r"C:\Users\Maker\Desktop\djangoProject\tmp27461501745267184763129482\2746150174526"
                              r"7184763129482private.pem", "rb") as File:
                        pkey = File.read()

                        file = open(r"C:\Users\Maker\Desktop\djangoProject\tmp27461501745267184763129482\2746150174526"
                                    r"7184763129482qr.png", 'rb').read()
                        qrcode = base64.b64encode(file)

                    if fname == qfn and lname == qln and edob == qdb:
                        t = TokenStorage(id_number=num, hash=h, privatekey=pkey, QR=qrcode, Qr_Issued='True')
                        t.save()
                        removedir(a)
                        qrpic(num)
                        with open(r'C:\Users\Maker\Desktop\djangoProject\27461501745267184763129482.jpeg', "rb") as f:
                            return HttpResponse(f.read(), content_type="image/png")
    else:
        form = CreateNewQR()
    return render(response, "penut/create1.html", {"form": form})




