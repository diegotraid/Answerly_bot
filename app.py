import connect_openAi


# inicio el programa
def iniciar_programa():

    # realizo pregunta
    pregunta = input('Que es lo que deseas saber?')

    # llamo a al modulo que realiza la peticion
    respuesta = connect_openAi.generar_respuesta(pregunta)

    # muestro respuesta
    print(respuesta)


iniciar_programa()
