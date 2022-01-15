import json
from django.shortcuts import redirect, render
from .forms import input_form
from .machine_learning import predict
from django.http import JsonResponse
# Create your views here.

def predict_price(request):
    
    """a view to get user input and predict price base on what is machine learned."""

    predicted_price = None
    rooms,space,y_of_cons = None,None,None
    if request.method == 'POST':
        form = input_form(request.POST)
        if form.is_valid():
            if request.is_ajax():
                cleaned_data = form.cleaned_data
                rooms,space,y_of_cons = cleaned_data['room'],cleaned_data['space'],cleaned_data['year_of_construction']
                predicted_price = int(predict([[rooms, space, y_of_cons]]))
                predicted_price = f'{predicted_price:,}'
                return JsonResponse({
                        'price':predicted_price,
                        'rooms':rooms,
                        'space':space,
                        'year_of_construction': y_of_cons,
                })
            # here our machine learning algorithm will predict the price,when forms passes validation.
            cleaned_data = form.cleaned_data
            rooms,space,y_of_cons = cleaned_data['room'],cleaned_data['space'],cleaned_data['year_of_construction']
            predicted_price = int(predict([[rooms, space, y_of_cons]]))
            predicted_price = f'{predicted_price:,}'
        else:
            return JsonResponse(form.errors, status=400)
    else:
        form = input_form()
    return render(request, 'ml/prediction.html', context= {'form':form,
    'price':predicted_price,
    'rooms':rooms,
    'space':space,
    'year_of_construction': y_of_cons,
    })
        
 
