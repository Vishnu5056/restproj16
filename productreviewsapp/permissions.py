from rest_framework.permissions import BasePermission,SAFE_METHODS
from django.contrib.auth.models import User
from .models import Review
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        u1=User.objects.get(username=request.user)
        print(u1.username)
        r1=Review.objects.filter(created_by=u1)
        x=[]
        for p in r1:
            x.append(p.id)
        print(x)
        rid=int(request.path[-2])
        print(rid)
        if rid in x:
            return True
        #request.GET["username"]==request.user
