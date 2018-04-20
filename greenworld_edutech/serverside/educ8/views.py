from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from educ8.models import School,Student,ScholasticDetail 
import json
def index(request):
    results = [ob.as_json() for ob in ScholasticDetail.objects.all()]
    return HttpResponse(json.dumps(results), content_type="application/json")
    #schools_as_json = serializers.serialize('json', School.objects.all())
    #return HttpResponse(schools_as_json, content_type='json')
