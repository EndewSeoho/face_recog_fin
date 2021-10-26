from .task import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .models import *

@api_view(['POST'])
@permission_classes([AllowAny])
def enrollment_img(request):
    # try:

        id = request.POST["id"]
        company = request.POST["company"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        image = request.FILES["image"].read()

        result = enroll_img(id, company, image)

        # print(len(image))

        if age =='':
            age = None
        if gender == '':
            gender = None


        if len(image) < 307200 or len(image) > 502000:
            response_dict = {"result": "ZZZZZZZZZZZZ"}
        else:

            res = FaceRecogApi(id = id, gender = gender, age = age, company = company, image = result)

            res.save()

            response_dict = {"result": "Success"}

        return JsonResponse(response_dict)

    # except Exception as e:
    #     response_dict = {"result": "Fail"}
    #
    #     return JsonResponse(response_dict)


@api_view(['POST'])
@permission_classes([AllowAny])
def analy_img(request):

    try:
        id = request.POST["id"]
        company = request.POST["company"]
        image = request.FILES["image"].read()

        result = face_analy(id, company, image)

        response_dict = {"result" : result}

        return JsonResponse(response_dict)

    except Exception as e:
        response_dict = {"result": "Fail"}

        return JsonResponse(response_dict)
