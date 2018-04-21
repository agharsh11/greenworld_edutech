from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from educ8.models import School,Student,ScholasticDetail
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    results = [ob.as_json() for ob in ScholasticDetail.objects.all()]
    return HttpResponse(json.dumps(results), content_type="application/json")
    #schools_as_json = serializers.serialize('json', School.objects.all())
    #return HttpResponse(schools_as_json, content_type='json')

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        first_name = body['first_name']
        middle_name = body['middle_name']
        last_name = body['last_name']
        image_url = body['image_url']
        registration_date = body['registration_date']
        year_of_birth = body['year_of_birth']
        birth_date = body['birth_date']
        gender = body['gender']
        aadhar = body['aadhar']
        new_student = Student(first_name=first_name, middle_name=middle_name, last_name=last_name, student_img=image_url, registration_date=registration_date, year_of_birth=year_of_birth, birth_date=birth_date, gender=gender, aadhar=aadhar)
        try:
            new_student.save()
        except IntegrityError:
            return HttpResponse(status_code=500)

        res = {
            'id' : new_student.id
        }
        return JsonResponse(res, status=200)



