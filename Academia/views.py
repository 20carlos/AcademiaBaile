from django.shortcuts import render
from django.contrib.auth.models import User
from Academia.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index_view(request, template_name = 'Academia/index.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    '''try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login/')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    count_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()'''
    return render(request, template_name, locals(),)


def login_view(request, template_name = 'Academia/login.html'):
    #Modulo que permite a los usuarios ingresar sus datos de usuario y contraseña para acceder a las distintas funciones del sistema
    #Declaramos las variables iniciales para el manejo de la informacion del formulario
    state = ""
    username = ""
    password = ""
    next = ""
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de alerta
    if request.GET:
        next = request.GET['next']
    #Si el formulario es mandado por metodo post
    if request.POST:
        #Obtenemso los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        try:
            if '@' in username:
                check = User.objects.get(email=username)
            else:
                check = User.objects.get(username=username)
            username = check.username
            #Col dos datos del formulario validamos que estos pertenezcan a algun usuario den la base de datos
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if next == "":
                        request.session.set_expiry(14400)#4 horas para que caduque la session
                        #check.last_login = datetime.now()
                        #check.save()
                        return HttpResponseRedirect('/home/')
                    else:
                        return HttpResponseRedirect(next)
                else:
                    #Mandamos la excepcion en caso de que un usuario aun sin activar trate de ingresar
                    estado = 1
                    mensaje = "¡Lo sentimos! Este usuario debe activarse."
                    #messages.warning(request, mensaje)
                    return render(request, template_name, locals(),)
            valid = check.check_password(password)
            if not valid:
                #Si la contraseña no es valida
                estado = 1
                mensaje = "¡Hay un problema! La contraseña es incorrecta."
                #messages.warning(request, mensaje)
                return render(request, template_name, locals(),)
        except ObjectDoesNotExist:
            if '@' in username:
                #Si el usuario no esta registrado en la base de datos
                estado = 1
                mensaje = "¡Lo sentimos! El email no existe, registrese por favor."
                #messages.info(request, mensaje)
                return render(request, template_name, locals(),)
            else:
                estado = 1
                mensaje = "¡Upps! El nombre de usuario no existe, registrese por favor."
                ##messages.warning(request, mensaje)
                return render(request, template_name, locals(),)

    return render(request, template_name, {'mensaje':mensaje, 'username': username, 'next': next,},)


def home_view(request, template_name = 'Academia/home.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    return render(request, template_name, locals(),)


def login_out(request):
    #Pagina a la que se accede despues de un logout del usuario
    logout(request)
    return HttpResponseRedirect('/')


def lista_alumnos(request, template_name = 'Academia/lista_alumnos.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    alumnos = Alumno.objects.all()
    return render(request, template_name, locals(),)


def lista_clases(request, template_name = 'Academia/lista_clases.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    clases = Clase.objects.all()
    return render(request, template_name, locals(),)


def agregar_alumno(request, template_name = 'Academia/agregar_alumno.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    clases = Clase.objects.all()
    if request.method == "POST":
        nombre = request.POST['nombre']
        a_paterno = request.POST['a_paterno']
        a_materno = request.POST['a_materno']
        edad = request.POST['edad']
        clase = request.POST['clase']
        if Alumno.objects.all().filter(nombre=nombre, a_paterno=a_paterno, a_materno=a_materno, edad=edad).exists():
            estado = 1
            mensaje = 'Ya existe el alumno!'
            return render(request, template_name, locals(),)
        else:
            clase_obj = Clase.objects.get(pk=clase)
            new_alumno = Alumno(nombre=nombre, a_paterno=a_paterno, a_materno=a_materno, edad=edad, clase=clase_obj)
            new_alumno.save()
            estado = 1
            mensaje = 'Alumno agregado con exito!'
            return render(request, template_name, locals(),)
        #print(nombre, a_paterno, a_materno, edad, clase)

    return render(request, template_name, locals(),)


def agregar_clase(request, template_name = 'Academia/agregar_clase.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    #clases = Clase.objects.all()
    if request.method == "POST":
        nombre = request.POST['nombre']
        horario = request.POST['horario']
        if Clase.objects.all().filter(nombre=nombre, horario=horario).exists():
            estado = 1
            mensaje = 'Ya existe la clase con el mismo horario!'
            return render(request, template_name, locals(),)
        else:
            new_clase = Clase(nombre=nombre, horario=horario)
            new_clase.save()
            estado = 1
            mensaje = 'Clase agregada con exito!'
            return render(request, template_name, locals(),)
        #print(nombre, a_paterno, a_materno, edad, clase)

    return render(request, template_name, locals(),)


def eliminar_alumno(request, id_alumno):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    #clases = Clase.objects.all()
    alumno = Alumno.objects.get(id=id_alumno)
    alumno.delete()
    return HttpResponseRedirect('/lista_alumnos')
    '''if request.method == "POST":
        nombre = request.POST['nombre']
        horario = request.POST['horario']
        if Clase.objects.all().filter(nombre=nombre, horario=horario).exists():
            estado = 1
            mensaje = 'Ya existe la clase con el mismo horario!'
            return render(request, template_name, locals(),)
        else:
            new_clase = Clase(nombre=nombre, horario=horario)
            new_clase.save()
            estado = 1
            mensaje = 'Clase agregada con exito!'
            return render(request, template_name, locals(),)
        #print(nombre, a_paterno, a_materno, edad, clase)

    return render(request, template_name, locals(),)'''

def eliminar_clase(request, id_clase):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    #clases = Clase.objects.all()
    clase = Clase.objects.get(id=id_clase)
    clase.delete()
    return HttpResponseRedirect('/lista_clases')


def modificar_alumno(request, id_alumno, template_name = 'Academia/modificar_alumno.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    alumno_obj = Alumno.objects.get(id=id_alumno)
    alumno = {
        "nombre" : alumno_obj.nombre,
        "a_paterno" : alumno_obj.a_paterno,
        "a_materno" : alumno_obj.a_materno,
        "edad" : alumno_obj.edad,
        "clase" : alumno_obj.clase.nombre + " : " + alumno_obj.clase.horario,
        "clase_id" : alumno_obj.clase.id
    }

    clases = Clase.objects.all()
    if request.method == "POST":
        nombre = request.POST['nombre']
        a_paterno = request.POST['a_paterno']
        a_materno = request.POST['a_materno']
        edad = request.POST['edad']
        clase = request.POST['clase']
        if Alumno.objects.all().filter(nombre=nombre, a_paterno=a_paterno, a_materno=a_materno, edad=edad).exclude(id = id_alumno).exists():
            estado = 1
            mensaje = 'Ya existe un alumno con estos datos!'
            return render(request, template_name, locals(),)
        else:
            clase_obj = Clase.objects.get(pk=clase)
            alumno_obj.nombre = nombre
            alumno_obj.a_paterno = a_paterno
            alumno_obj.a_materno = a_materno
            alumno_obj.edad = edad
            alumno_obj.clase = clase_obj
            alumno_obj.save()
            estado = 1
            mensaje = 'Alumno modificado con exito!'
            alumno = {
                "nombre" : alumno_obj.nombre,
                "a_paterno" : alumno_obj.a_paterno,
                "a_materno" : alumno_obj.a_materno,
                "edad" : alumno_obj.edad,
                "clase" : alumno_obj.clase.nombre + " : " + alumno_obj.clase.horario,
                "clase_id" : alumno_obj.clase.id
            }
            return render(request, template_name, locals(),)
        #print(nombre, a_paterno, a_materno, edad, clase)

    return render(request, template_name, locals(),)


def modificar_clase(request, id_clase, template_name = 'Academia/modificar_clase.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    #count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    #xcount_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()
    clase_obj = Clase.objects.get(id=id_clase)
    clase = {
        "nombre" : clase_obj.nombre,
        "horario" : clase_obj.horario
    }

    if request.method == "POST":
        nombre = request.POST['nombre']
        horario = request.POST['horario']
        if Clase.objects.all().filter(nombre=nombre, horario=horario).exclude(id = id_clase).exists():
            estado = 1
            mensaje = 'Ya existe una clase con estos datos!'
            return render(request, template_name, locals(),)
        else:
            clase_obj.nombre = nombre
            clase_obj.horario = horario
            clase_obj.save()
            estado = 1
            mensaje = 'Clase modificada con exito!'
            clase = {
                "nombre" : clase_obj.nombre,
                "horario" : clase_obj.horario
            }
            return render(request, template_name, locals(),)
        #print(nombre, a_paterno, a_materno, edad, clase)

    return render(request, template_name, locals(),)


def eventos(request, template_name = 'Academia/eventos.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    '''try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login/')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    count_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()'''
    return render(request, template_name, locals(),)


def maestros(request, template_name = 'Academia/maestros.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    '''try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login/')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    count_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()'''
    return render(request, template_name, locals(),)


def contacto(request, template_name = 'Academia/contacto.html'):
    '''
    Función home

    Es la primera vista despues de que el usuario se logueo

    Parametros:
        -request            --[peticion]--      nos permite obtener el usuario logueado 
        -template_name      --[string]--        proporciona la url vinculada a la función
    Excepciones:
        -sin excepciones    --
    Return:
        -locals()           --[encapsulado]--   retorna todas las variables declaradas en el views
    '''
    '''try:
        usuario = request.user
        user =  User.objects.get(username = usuario)
        usuarioExt = Usuario.objects.get(user = user)
        isAdministrador = user.groups.filter(name = 'Administrador').exists()
    except:
        return HttpResponseRedirect('/login/')
    estado = 0#Bandera de alertas
    mensaje = ""#Mensaje de la alerta
    count_instrumentos = Instrumento.objects.filter(usuario=usuarioExt).count()
    count_grupos = Cat_grupo.objects.filter(usuario=usuarioExt).count()'''
    return render(request, template_name, locals(),)