from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    #replace library class into books array
    books = [
        {'id':1,'title':'La llorona', 'autor': 'Alvaro Rodriguez Peña', 'img':'app/img/library/01.jpg', 'date': '01-05-2018'},
        {'id':2,'title':'El Robo', 'autor': 'Manuel Peña Loza', 'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':3,'title':'El Mandril', 'autor': 'Jose Peña Loza', 'img':'app/img/library/03.jpg', 'date': '01-05-2017'},
        {'id':4,'title':'Tecnicas laborales', 'autor': 'Jhon Espinoza Ramos', 'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':5,'title':'Tecnicas intelectuales', 'autor': 'Dan Alvarez', 'img':'app/img/library/05.jpg', 'date': '01-05-2017'},
        {'id':6,'title':'La llorona', 'autor': 'Alvaro Rodriguez Peña', 'img':'app/img/library/06.jpg', 'date': '01-05-2018'},
        {'id':7,'title':'El Robo', 'autor': 'Manuel Peña Loza', 'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':8,'title':'El Mandril', 'autor': 'Jose Peña Loza', 'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':9,'title':'Tecnicas laborales', 'autor': 'Jhon Espinoza Ramos', 'img':'app/img/library/01.jpg', 'date': '01-05-2017'},
        {'id':10,'title':'Tecnicas intelectuales', 'autor': 'Dan Alvarez', 'img':'app/img/library/02.jpg', 'date': '01-05-2017'},
        {'id':11,'title':'La llorona', 'autor': 'Alvaro Rodriguez Peña', 'img':'app/img/library/01.jpg', 'date': '01-05-2018'},
        {'id':12,'title':'El Robo', 'autor': 'Manuel Peña Loza', 'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':13,'title':'El Mandril', 'autor': 'Jose Peña Loza', 'img':'app/img/library/03.jpg', 'date': '01-05-2017'},
        {'id':14,'title':'Tecnicas laborales', 'autor': 'Jhon Espinoza Ramos', 'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':15,'title':'Tecnicas intelectuales', 'autor': 'Dan Alvarez', 'img':'app/img/library/05.jpg', 'date': '01-05-2017'},
    ]
    return render(request, 'app/home.html', {"books": books})