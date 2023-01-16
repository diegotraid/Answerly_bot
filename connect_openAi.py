import requests


api_key = "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"

# autorizacion de la api key
headers = {
    'Authorization': f'Bearer {api_key}'}


# me conecto a los parametros que yo quiero de openAI
url = "https://api.openai.com/v1/engines/text-davinci-002/completions"


def generar_respuesta(pregunta):

    # aca se genera el prompt, le doy valores para que la respuesta sea la que yo quiero.
    data = {
        "prompt": pregunta,
        "max_tokens": 1000,
        "stop": "",
        "temperature": 0.7
    }

    # hago la peticion
    response = requests.post(url, json=data, headers=headers)

    # agarro la respuesta
    respuesta = response.json()

    # devuelvo la misma
    return respuesta['choices'][0]['text']


if __name__ == '__main__':
    print(generar_respuesta())
