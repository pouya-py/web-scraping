$(document).ready(function(){
    var $form = $('.ajax-form')
    $form.submit(function(event){
        event.preventDefault()
        var $form_data = $form.serialize()
        var $url = $form.attr('data-url') || window.location.href
        // console.log($form_data)
        // console.log($url)
        $.ajax({
            method: 'POST',
            url : $url,
            data : $form_data,
            success : handleformsuccess,
            error : handelformerror
        })


    })
    function handleformsuccess(data,textstatus,jqXHR){
        // append the fetched data from the server
        if (textstatus == 'success'){
            $('.info').append(':حدودقیمت بر اساس داده‌های زیر')
            $('.data .rooms').append(
                 data['rooms'] + ':خواب' 
            );
            $('.data .space').append(
                 data['space'] + ':متراژ' 
            );
            $('.data .year_of_build').append(
                 data['year_of_construction'] + ':سال ساخت' 
            );
            $('.price').append(data['price'] +' :قیمت پیش‌بینی شده');
    
        }
        // reset the form data, notice we should get javascript object first.
        $form[0].reset();
    }
    function handelformerror(errorThrown, textStatus, jqXHR){
        var error = errorThrown.responseJSON
        console.log(error)
        if (error !== null){
            if (error['space']){
                $('<li class="text-danger" dir="rtl">'+'<span>'+error['space']+'<span>'+'</li>').insertAfter($('div > p:first'))
            }
            if (error['year_of_construction']){
                // alert(error['year_of_construction'])
                $('<li class="text-danger" dir="rtl">'+'<span>'+error['year_of_construction']+'<span>'+'</li>').insertAfter($('div > p:first'))
            }

            
        }
    }
   

})

