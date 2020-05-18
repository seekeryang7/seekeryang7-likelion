from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    # text_input = form
    word_count = len(text.split(" ")); 
    strip_len = len(text.replace(" ",""))
    text_input =  text
    return render(request, 'result.html', {
        'total_len' : total_len,
        'word_count' : word_count,
        'strip_len' : strip_len,
        'text_input' : text_input,
    })