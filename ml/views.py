from django.shortcuts import render
from .forms import input_form
# Create your views here.

def predict_price(request):
    """a view to get user input and predict price base on what is machine learned."""
    if request.method = 'POST':
        form = input_form(request.POST)

        if form.is_valid():
            # here our machine learning algorithm will predict the price,when forms passes validation.
            pass
    
    form = input_form()

    return render(request, 'ml/prediction.html', context= {'form':form})
        

