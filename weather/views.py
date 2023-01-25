from django.shortcuts import render
import json
import urllib.request,os
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        print('does it work------------------------------------')
        print(type(city))
        secret_key = os.environ['SECRET_KEY']

        request_url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+secret_key).read()
        #print(request_url.read())
        json_data=json.loads(request_url)
        conv=json_data['main']['feels_like']
        conv=(int)(conv-273)
        data={
            'country_code':json_data['sys']['country'],
            'temp':conv,
            'pressure':json_data['main']['pressure'],
            'humidity':json_data['main']['humidity']
        }
    else:
        city='enter some name'
        data={}

    return render(request, 'index.html',{'city':city,'data':data})

#'data':data