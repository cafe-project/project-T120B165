from bottle import unicode
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from meals.services.meal_service import MealService

from meals.services.product_service import ProductService

from meals.helper import parse_json_from_request

from meals.services.pdf_service import PdfService


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)



@csrf_exempt
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
def product_list(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    products = ProductService().product_list(parameters)
    return JsonResponse(products, safe=False)


@csrf_exempt
def create_product(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    ProductService().create_product(parameters)
    return HttpResponse()


@csrf_exempt
def delete_product(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    ProductService().delete_product(parameters)
    return HttpResponse()


@csrf_exempt
def update_product(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    ProductService().update_product(parameters)
    return HttpResponse()


@csrf_exempt
def get_product(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    product = ProductService().get_product(parameters)
    return JsonResponse(product, safe=False)

@csrf_exempt
def meal_list(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    meals = MealService().meal_list(parameters)
    return JsonResponse(meals, safe=False)


@csrf_exempt
def create_meal(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    MealService().create_meal(parameters, request.user)
    return HttpResponse()


@csrf_exempt
def delete_meal(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    MealService().delete_meal(parameters)
    return HttpResponse()


@csrf_exempt
def update_meal(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    MealService().update_meal(parameters)
    return HttpResponse()


@csrf_exempt
def get_meal(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    meal = MealService().get_meal(parameters)
    return JsonResponse(meal)
    return HttpResponse()


@csrf_exempt
def category_list(request: WSGIRequest, name: str):
    parameters = parse_json_from_request(request)

    return HttpResponse()

@csrf_exempt
def create_category(request: WSGIRequest, name: str):
    parameters = parse_json_from_request(request)
    return HttpResponse()


@csrf_exempt
def delete_category(request: WSGIRequest, name: str):
    parameters = parse_json_from_request(request)
    return HttpResponse()


@csrf_exempt
def get_category(request: WSGIRequest, name: str):
    parameters = parse_json_from_request(request)
    return HttpResponse()


@csrf_exempt
def generate_pdf(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    meal_parameters = {
        'category': 1,
        'name': 'name'
    }
    meal = MealService().create_meal(meal_parameters)
    PdfService().generate_pdf(meal)
    return HttpResponse()