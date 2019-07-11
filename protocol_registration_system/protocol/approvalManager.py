from .models import Protocol

def assignnum():
    ls = [x.number for x in Protocol.objects.all()]
    pro = Protocol.objects.latest('approval_date')
    return pro.id+1
#terra