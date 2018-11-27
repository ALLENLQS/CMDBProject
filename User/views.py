from django.shortcuts import render
from django.http import JsonResponse
from XueGodCMDB.views import *
# Create your views here.
def register(request):
    # if request.method == "POST":
    #     return JsonResponse({"method":"POST"})
    # else:
    #     return JsonResponse({"method":"GET"})
    result_dict = {'submit':'success'}
    if request.method == 'POST' and request.POST and request.FILES:
        register_data = CMDBUserForm(data=request.POST,files=request.FILES)
        if register_data.is_valid():
            register_post_data = register_data.cleaned_data

            username = register_post_data.get('username')
            password = register_post_data.get('password')
            nickname = register_post_data.get('nickname')
            phone = register_post_data.get('phone')
            email = register_post_data.get('email')

            photo = register_post_data.get('photo').name

            CMDBUser.objects.create(
                username = username,
                password = password,
                nickname = nickname,
                phone = phone,
                email = email,
                photo = photo,
            )
            photoFile = request.FILES.get('photo')
            photoSavePath = os.path.join(BASE_DIR,'static\\images\\%s'%photoFile.name)
            with open(photoSavePath,'wb') as pf:
                for chunk in photoFile.chunks():
                    pf.write(chunk)
                return JsonResponse(result_dict)
        else:
            print(register_data.errors)
            result_dict['submit'] = 'error'
            return JsonResponse(result_dict)
    else:
        return JsonResponse({'method':'GET'})
