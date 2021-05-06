from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    #replace library class into books array

    # Tomar en cuenta que este array es un ejemplo de resultado del backend
    courses = [
        {'id':1,'name':'Arquitectura', 'img':'app/img/courses/default-01.jpg', 'date': '01-05-2018', 'score':1, 'price':28.00, 'students':1500},
        {'id':2,'name':'Arte',  'img':'app/img/courses/default-02.jpg', 'date': '01-05-2014', 'score':1, 'price':28.00, 'students':1500},
        {'id':3,'name':'Comunicación', 'img':'app/img/courses/default-03.jpg', 'date': '01-05-2017','score':4, 'price':28.00, 'students':1500},
        {'id':4,'name':'Biología',  'img':'app/img/courses/default-04.jpg', 'date': '01-05-2017', 'score':5, 'price':28.00, 'students':1500},
        {'id':5,'name':'Química', 'img':'app/img/courses/default-05.jpg', 'date': '01-05-2017', 'score':3, 'price':28.00, 'students':1500},
        {'id':6,'name':'Ciencias de la computación', 'img':'app/img/courses/default-06.jpg', 'date': '01-05-2018', 'score':2, 'price':28.00, 'students':1500},
        {'id':7,'name':'Diseño gráfico',  'img':'app/img/courses/default-07.jpg', 'date': '01-05-2014', 'score':1, 'price':28.00, 'students':1500},
        {'id':8,'name':'Economía', 'img':'app/img/courses/default-08.jpg', 'date': '01-05-2017', 'score':1, 'price':28.00, 'students':1500},
        {'id':9,'name':'Ciencia de datos',  'img':'app/img/courses/default-09.jpg', 'date': '01-05-2017', 'score':1, 'price':28.00, 'students':1500},
        {'id':10,'name':'Administración de empresas', 'img':'app/img/courses/default-10.jpg', 'date': '01-05-2017', 'score':2, 'price':28.00, 'students':1500},
        {'id':11,'name':'Educación', 'img':'app/img/courses/default-11.jpg', 'date': '01-05-2018', 'score':2, 'price':28.00, 'students':1500},
        {'id':12,'name':'Electrónica',  'img':'app/img/courses/default-12.jpg', 'date': '01-05-2014', 'score':1, 'price':28.00, 'students':1500},
        {'id':13,'name':'Ingeniería', 'img':'app/img/courses/default-13.jpg', 'date': '01-05-2017', 'score':1, 'price':28.00, 'students':1500},
        {'id':14,'name':'Medicina',  'img':'app/img/courses/default-14.jpg', 'date': '01-05-2017', 'score':2, 'price':28.00, 'students':1500},
        {'id':15,'name':'Literatura', 'img':'app/img/courses/default-15.jpg', 'date': '01-05-2017', 'score':1, 'price':28.00, 'students':1500},
        {'id':16,'name':'Matemáticas', 'img':'app/img/courses/default-06.jpg', 'date': '01-05-2018', 'score':4, 'price':28.00, 'students':1500},
        {'id':17,'name':'Salud',  'img':'app/img/courses/default-02.jpg', 'date': '01-05-2014', 'score':2, 'price':28.00, 'students':1500},
        {'id':18,'name':'Música', 'img':'app/img/courses/default-03.jpg', 'date': '01-05-2017', 'score':2, 'price':28.00, 'students':1500},
        {'id':19,'name':'Filosofía',  'img':'app/img/courses/default-04.jpg', 'date': '01-05-2017', 'score':5, 'price':28.00, 'students':1500},
        {'id':20,'name':'Derecho', 'img':'app/img/courses/default-05.jpg', 'date': '01-05-2017', 'score':5, 'price':28.00, 'students':1500},
        {'id':21,'name':'Física', 'img':'app/img/courses/default-06.jpg', 'date': '01-05-2018', 'score':5, 'price':28.00, 'students':1500},
        {'id':22,'name':'Ciencias sociales',  'img':'app/img/courses/default-07.jpg', 'date': '01-05-2014', 'score':5, 'price':28.00, 'students':1500},
        {'id':23,'name':'Humanidades', 'img':'app/img/courses/default-08.jpg', 'date': '01-05-2017', 'score':1, 'price':28.00, 'students':1500},
        {'id':24,'name':'Historia',  'img':'app/img/courses/default-09.jpg', 'date': '01-05-2017', 'score':1, 'price':28.00, 'students':1500},
        {'id':25,'name':'Nutrición', 'img':'app/img/courses/default-10.jpg', 'date': '01-05-2017', 'score':5, 'price':28.00, 'students':1500},
        {'id':26,'name':'Ética', 'img':'app/img/courses/default-11.jpg', 'date': '01-05-2018', 'score':2, 'price':28.00, 'students':1500},
        {'id':27,'name':'Medio Ambiente',  'img':'app/img/courses/default-12.jpg', 'date': '01-05-2014', 'score':4, 'price':28.00, 'students':1500},
        {'id':28,'name':'Energía', 'img':'app/img/courses/default-13.jpg', 'date': '01-05-2017', 'score':3, 'price':28.00, 'students':1500},
    ]

    categories = [
        {'id':1,'name':'La llorona', 'img':'app/img/library/01.jpg', 'date': '01-05-2018'},
        {'id':2,'name':'El Robo',  'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':3,'name':'El Mandril', 'img':'app/img/library/03.jpg', 'date': '01-05-2017'},
        {'id':4,'name':'Tecnicas laborales',  'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':5,'name':'Tecnicas intelectuales', 'img':'app/img/library/05.jpg', 'date': '01-05-2017'},
        {'id':6,'name':'La llorona', 'img':'app/img/library/06.jpg', 'date': '01-05-2018'},
        {'id':7,'name':'El Robo',  'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':8,'name':'El Mandril', 'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':9,'name':'Tecnicas laborales',  'img':'app/img/library/01.jpg', 'date': '01-05-2017'},
        {'id':10,'name':'Tecnicas intelectuales', 'img':'app/img/library/02.jpg', 'date': '01-05-2017'},
        {'id':11,'name':'La llorona', 'img':'app/img/library/01.jpg', 'date': '01-05-2018'},
        {'id':12,'name':'El Robo',  'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':13,'name':'El Mandril', 'img':'app/img/library/03.jpg', 'date': '01-05-2017'},
        {'id':14,'name':'Tecnicas laborales',  'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':15,'name':'Tecnicas intelectuales', 'img':'app/img/library/05.jpg', 'date': '01-05-2017'},
    ]

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

    collages = [
        {'id':1,'name':'La llorona', 'img':'app/img/library/01.jpg', 'date': '01-05-2018'},
        {'id':2,'name':'El Robo',  'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':3,'name':'El Mandril', 'img':'app/img/library/03.jpg', 'date': '01-05-2017'},
        {'id':4,'name':'Tecnicas laborales',  'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':5,'name':'Tecnicas intelectuales', 'img':'app/img/library/05.jpg', 'date': '01-05-2017'},
        {'id':6,'name':'La llorona', 'img':'app/img/library/06.jpg', 'date': '01-05-2018'},
        {'id':7,'name':'El Robo',  'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':8,'name':'El Mandril', 'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':9,'name':'Tecnicas laborales',  'img':'app/img/library/01.jpg', 'date': '01-05-2017'},
        {'id':10,'name':'Tecnicas intelectuales', 'img':'app/img/library/02.jpg', 'date': '01-05-2017'},
        {'id':11,'name':'La llorona', 'img':'app/img/library/01.jpg', 'date': '01-05-2018'},
        {'id':12,'name':'El Robo',  'img':'app/img/library/02.jpg', 'date': '01-05-2014'},
        {'id':13,'name':'El Mandril', 'img':'app/img/library/03.jpg', 'date': '01-05-2017'},
        {'id':14,'name':'Tecnicas laborales',  'img':'app/img/library/04.jpg', 'date': '01-05-2017'},
        {'id':15,'name':'Tecnicas intelectuales', 'img':'app/img/library/05.jpg', 'date': '01-05-2017'},
    ]

    clients = [
        {'id':1,'name':'Ipax', 'img':'app/img/our/Ipax.png', 'date': '01-05-2018'},
        {'id':2,'name':'Starlab',  'img':'app/img/our/Starlab.png', 'date': '01-05-2014'},
        {'id':3,'name':'Tigo', 'img':'app/img/our/tigo.png', 'date': '01-05-2017'},
        {'id':4,'name':'Unicef',  'img':'app/img/our/unicef.png', 'date': '01-05-2017'},
        {'id':5,'name':'Unesco', 'img':'app/img/our/unesco.png', 'date': '01-05-2017'},
        {'id':6,'name':'Save the Children', 'img':'app/img/our/Save the children.png', 'date': '01-05-2018'},
        {'id':7,'name':'Pica',  'img':'app/img/our/Pica.png', 'date': '01-05-2014'},
    ]


    return render(request, 'app/home.html', {"books": books, "collages":collages, "clients": clients, "categories": categories, "courses":courses})