print("Bienvenido a TRYPY, si estas en las nubes te ayudamos a aterrizar.")
dias = input("¿Cuántos días tienes planeado escaparte?: ")

print("¿En qué época del año quieres viajar?")
print("primavera")
print("verano")
print("invierno")
print("otoño")
estacion = input("Escribe el clima elegido: ")

print("¿Qué zona de España te gustaría visitar en", estacion,"?")
print("Norte")
print("Centro")
print("Sur")
region = input("Escribe la región elegida: ")


print("¿Te gustaría viajar a una ciudad del", region,"de España grande o a una más pequeña?")
print("Ciudad grande")
print("Ciudad mediana")
tamanyo = input("Escribe el tipo de ciudad: ")

def actividades():
    print("¿Qué actividades prefieres hacer durante el viaje?")
    print("Ir a visitar museos")
    print("Excursiones")
    print("Disfrutar de la gastronomia")
    print("Salir de noche")
    actividad = input("Escribe tu actividad favorita: ")
    return actividad

if (region == "Norte") & (tamanyo == "Ciudad grande"):
    diferencia1 = input("¿Te gustaría tomarte un txakoli con unos pintxos? (y/n): ")
    if diferencia1 == "y":
        print("Tu destino ideal es Bilbao, Euskadi.")
        actividad = actividades()
        if actividad == "Ir a visitar museos":
            print("Puedes ir a visitar el museo Guggengheim")
        elif actividad == "Excursiones":
            print("Puedes ir a ver San Juan de Gaztelugatxe")
        elif actividad == "Disfrutar de la gastronomia":
            print("Puedes ir a el Glovo y a la Plaza Nueva")
        elif actividad == "Salir de noche":
            print("Puedes ir a dar una vuelta por pozas")
        else:
            print("Esa opción no está disponible")
    else: 
        print("Tu destino ideal es Santander, Cantabria.")
        actividad = actividades()
        if actividad == "Ir a visitar museos":
            print("Puedes ir a visitar el museo maritimo")
        elif actividad == "Excursiones":
            print("Puedes ir al Palacio de la Magdalena")
        elif actividad == "Disfrutar de la gastronomia":
            print("Puedes a comer tortilla al Café Santander")
        elif actividad == "Salir de noche":
            print("Puedes ir a la discoteca Cambalache")
        else:
            print("Esa opción no está disponible")       
elif (region == "Norte") & (tamanyo == "Ciudad mediana"):
    print("Tu destino ideal es Santiago de Compostela, Galicia.")
    actividad = actividades()
    if actividad == "Ir a visitar museos":
        print("Puedes ir a visitar el museo del peregrino")
    elif actividad == "Excursiones":
        print("Puedes hacer el camino de santiago desde Roncesvalles")
    elif actividad == "Disfrutar de la gastronomia":
        print("Puedes ir a comer pulpo al bar Roi")
    elif actividad == "Salir de noche":
        print("Puedes salir por la Plaza del Obradoiro")
    else:
        print("Esa opción no está disponible")

elif (region == "Centro") & (tamanyo == "Ciudad grande"):
    diferencia2 = input("¿Eres más de Messi o de Cristiano?: ")
    if diferencia2 == "Messi":
        print("Tu destino ideal es Barcelona, Cataluña.")
        actividad = actividades()
        if actividad == "Ir a visitar museos":
            print("Puedes visitar el Museo Europeo de arte Moderno")
        elif actividad == "Excursiones":
            print("Puedes dar un paseo por el Park Güell")
        elif actividad == "Disfrutar de la gastronomia":
            print("Puedes comerte unos buenos calçots")
        elif actividad == "Salir de noche":
            print("Puedes pegarte un fiestote en Razzmataz")
        else:
            print("Esa opción no está disponible")

    else:
        print("Tu destino ideal es Madrid, Comunidad de Madrid.")
        actividad = actividades()
        if actividad == "Ir a visitar museos":
            print("Puedes ir a visitar el museo del Prado")
        elif actividad == "Excursiones":
            print("Puedes hacer una ruta por la Sierra de Guadarrama")
        elif actividad == "Disfrutar de la gastronomia":
            print("Puedes pillarte unas bravas en el restaurante Las Bravas")
        elif actividad == "Salir de noche":
            print("Puedes salir de fiesta por el barrio de Chueca")
        else:
            print("Esa opción no está disponible")
          
elif (region == "Centro") & (tamanyo == "Ciudad mediana"):
    print("Tu destino ideal es Valencia, Comunidad Valenciana.")
    actividad = actividades()
    if actividad == "Ir a visitar museos":
        print("Puedes ir a visitar el museo de las Artes y las Ciencias")
    elif actividad == "Excursiones":
        print("Puedes hacer la ruta del Bakalao")
    elif actividad == "Disfrutar de la gastronomia":
        print("Puedes ir a almorzar al Pastoret")
    elif actividad == "Salir de noche":
        print("Puedes irte de teknazo a Spook")
    else:
        print("Esa opción no está disponible")

elif (region == "Sur") & (tamanyo == "Ciudad grande"):
    diferencia3 = input("¿Eres más de mezquita o de catedral?: ")
    if diferencia3 == "catedral":
        print("Tu destino ideal es Sevilla, Andalucia.")
        actividad = actividades()
        if actividad == "Ir a visitar museos":
            print("Puedes ir a visitar el museo de Bellas Artes")
        elif actividad == "Excursiones":
            print("Puedes ir a ver la Doñana")
        elif actividad == "Disfrutar de la gastronomia":
            print("Puedes ir a comer salmorejo y pescaito frito al bar Ricardo")
        elif actividad == "Salir de noche":
            print("Puedes ir a dar una vuelta por el Barrio de Santa Cruz ")
        else:
            print("Esa opción no está disponible")
    else:
        print("Tu destino ideal es Córdoba, Andalucia.")
        actividad = actividades()
        if actividad == "Ir a visitar museos":
            print("Puedes ir a visitar la mezquita de Cordoba")
        elif actividad == "Excursiones":
            print("Puedes ir a Alcazar de los Reyes Cristianos")
        elif actividad == "Disfrutar de la gastronomia":
            print("Puedes ir comer rabo de toro, flamenquín y salmorejo al bar Ricardo")
        elif actividad == "Salir de noche":
            print("Puedes ir a dar una vuelta por la Calleja de las Flores")
        else:
            print("Esa opción no está disponible")

elif (region == "Sur") & (tamanyo == "Ciudad mediana"):
    print("Tu destino ideal es Granada, Andalucia.")
    actividad = actividades()
    if actividad == "Ir a visitar museos":
        print("Puedes ir a visitar el museo de la Alhambra")
    elif actividad == "Excursiones":
        print("Puedes ir a la Sierra Nevada")
    elif actividad == "Disfrutar de la gastronomia":
        print("Puedes ir comer remojon granadino al bar Carlos")
    elif actividad == "Salir de noche":
        print("Puedes ir a dar una vuelta por la Calle Elvira")
    else:
        print("Esa opción no está disponible")
else:
     print("Esa zona no está disponible")
    
print("Muchas gracias por confiar en TRYPY, pégate un buen viaje!")
print("Puedes reservar todo a través de www.trypytrypy.com")


