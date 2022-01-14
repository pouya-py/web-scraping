from django.shortcuts import redirect, render
from .forms import input_form
from .machine_learning import predict
# Create your views here.

def predict_price(request):
    
    """a view to get user input and predict price base on what is machine learned."""

    predicted_price = None
    rooms,space,y_of_cons = None,None,None
    form = input_form(request.GET)
    if form.is_valid():
        # here our machine learning algorithm will predict the price,when forms passes validation.
        cleaned_data = form.cleaned_data
        rooms,space,y_of_cons = cleaned_data['room'],cleaned_data['space'],cleaned_data['year_of_construction']
        predicted_price = int(predict([[rooms, space, y_of_cons]]))
        predicted_price = f'{predicted_price:,}'
    form = input_form()
    return render(request, 'ml/prediction.html', context= {'form':form,
    'price':predicted_price,
    'rooms':rooms,
    'space':space,
    'year_of_construction': y_of_cons,
    })
        
 
