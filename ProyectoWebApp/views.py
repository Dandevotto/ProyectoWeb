from django.shortcuts import render, HttpResponse

# Vista del home
def home(request):
    return render(request, "ProyectoWebApp/home.html")

# Vista de servicios
def services(request):
    return render(request, "ProyectoWebApp/servicios.html")

# Vista de tienda
def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

# Vista de blog
def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

# Vista de contacto
def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")