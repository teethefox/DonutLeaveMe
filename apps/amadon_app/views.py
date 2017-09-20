from django.shortcuts import render, redirect
def index(request):
    return render(request,'index.html')
def process(request):
    try:
        request.session['orders']
        request.session['overall']
    except KeyError:
        request.session['orders'] = 0
        request.session['overall']=0
    

    request.session['quantity1'] = request.POST['quantity1']
    request.session['quantity2'] = request.POST['quantity2']
    request.session['quantity3'] = request.POST['quantity3']
    request.session['quantity4'] = request.POST['quantity4']
    request.session['quantity5'] = request.POST['quantity5']
    
    
    request.session['id1']=request.POST.get("dunid", "001")
    request.session['id2']=request.POST.get("dunid", "002")
    request.session['id3']=request.POST.get("dunid", "003")
    request.session['id4']=request.POST.get("dunid", "004")
    request.session['id5']=request.POST.get("dunid", "005")
    request.session['total']=int(request.session['quantity1'])*(1.00)+int(request.session['quantity2'])*(1.00) +int(request.session['quantity3'])*(1.00) +int(request.session['quantity4'])*(2.00) +int(request.session['quantity5'])*(2.00)
    request.session['orders'] += 1
    request.session['overall'] += request.session['total']
    
        
   
    return redirect('/confirm')
def confirm(request):
    return render(request,'confirm.html')

# Create your views here.
