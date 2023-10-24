from config import *  # Importamos el token
import telebot  # Para manejar la API de Telegram
import time
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup
import pickle
import os
# Verifica si el directorio './busquedas/' existe, y si no, créalo.
if not os.path.exists('./busquedas/'):
    os.makedirs('./busquedas/')

# Constantes
N_RES_PAG = 5  # Número de resultados a mostrar en cada página
MAX_ANCHO_ROW = 8  # Máximo de botones por fila (el límite de Telegram es 8)
DIR = {"busquedas": "./busquedas/"}  # Directorio donde se guardan los archivos de las búsquedas

# Verificamos si los directorios existen y los creamos si no
for key in DIR:
    try:
        os.mkdir(DIR[key])
    except FileExistsError:
        pass

# Instanciamos el bot de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Para responder al comando /start
@bot.message_handler(commands=["help", "start", "ayuda"])
def enviar(message):
    bot.reply_to(message, "Hola, ¿Cómo estás?")
    print(message.chat.id)





# Responde al comando /botones
@bot.message_handler(commands=['botones'])
def cmd_botones(message):
    markup = InlineKeyboardMarkup(row_width=3)  # Número de botones en cada fila, 3 por defecto
    a1 = InlineKeyboardButton("DIRECTORIO", url="https://t.me/YaichiAnimeDirectorio")
    b0 = InlineKeyboardButton("#", url="https://t.me/YaichiAnimeDirectorio/67")
    b1 = InlineKeyboardButton("A", url="https://t.me/YaichiAnimeDirectorio/68")
    b2 = InlineKeyboardButton("B", url="https://t.me/YaichiAnimeDirectorio/69")
    b3 = InlineKeyboardButton("C", url="https://t.me/YaichiAnimeDirectorio/70")
    b4 = InlineKeyboardButton("D", url="https://t.me/YaichiAnimeDirectorio/71")
    b5 = InlineKeyboardButton("E", url="https://t.me/YaichiAnimeDirectorio/72")
    b6 = InlineKeyboardButton("F", url="https://t.me/YaichiAnimeDirectorio/73")
    b7 = InlineKeyboardButton("G", url="https://t.me/YaichiAnimeDirectorio/74")
    b8 = InlineKeyboardButton("H", url="https://t.me/YaichiAnimeDirectorio/75")
    b9 = InlineKeyboardButton("I", url="https://t.me/YaichiAnimeDirectorio/76")
    b10 = InlineKeyboardButton("J", url="https://t.me/YaichiAnimeDirectorio/77")
    b11 = InlineKeyboardButton("K", url="https://t.me/YaichiAnimeDirectorio/78")
    b12 = InlineKeyboardButton("L", url="https://t.me/YaichiAnimeDirectorio/79")
    b13 = InlineKeyboardButton("M", url="https://t.me/YaichiAnimeDirectorio/80")
    b14 = InlineKeyboardButton("N", url="https://t.me/YaichiAnimeDirectorio/81")
    b15 = InlineKeyboardButton("O", url="https://t.me/YaichiAnimeDirectorio/82")
    b16 = InlineKeyboardButton("P", url="https://t.me/YaichiAnimeDirectorio/83")
    b17 = InlineKeyboardButton("Q", url="https://t.me/YaichiAnimeDirectorio/84")
    b18 = InlineKeyboardButton("R", url="https://t.me/YaichiAnimeDirectorio/85")
    b19 = InlineKeyboardButton("S", url="https://t.me/YaichiAnimeDirectorio/86")
    b20 = InlineKeyboardButton("T", url="https://t.me/YaichiAnimeDirectorio/87")
    b21 = InlineKeyboardButton("U", url="https://t.me/YaichiAnimeDirectorio/88")
    b22 = InlineKeyboardButton("V", url="https://t.me/YaichiAnimeDirectorio/89")
    b23 = InlineKeyboardButton("W", url="https://t.me/YaichiAnimeDirectorio/90")
    b24 = InlineKeyboardButton("X", url="https://t.me/YaichiAnimeDirectorio/91")
    b25 = InlineKeyboardButton("Y", url="https://t.me/YaichiAnimeDirectorio/92")
    b26 = InlineKeyboardButton("Z", url="https://t.me/YaichiAnimeDirectorio/93")
    c1 = InlineKeyboardButton("Peliculas", url="https://t.me/YaichiAnimeDirectorio/95")
    markup.row(a1)
    markup.add(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26)
    markup.row(c1)
    bot.reply_to(message, "-----[BOTONERA YAICHI COMUNIDAD]-----\nLos animes están ordenados alfabeticamente segun su nombre en japones, estos son los animes que estan disponibles en nuestro catálogo", reply_markup=markup)
    #bot.send_message(CANAL_ID, "-----[BOTONERA YAICHI COMUNIDAD]-----\nLos animes están ordenados alfabeticamente segun su nombre en japones, estos son los animes que estan disponibles en nuestro catálogo", reply_markup=markup)
   
# Responde al comando /buscar
@bot.message_handler(commands=['buscar'])
def cmd_buscar(message):
    # Realiza una búsqueda en Google y devuelve una lista de resultados
    texto_buscar = " ".join(message.text.split()[1:])
    
    # Si no se han pasado parámetros
    if not texto_buscar:
        texto = 'Debes introducir una búsqueda.\n'
        texto += 'Ejemplo:\n'
        texto += f'<code>{message.text} Fate series</code>'
        bot.send_message(message.chat.id, texto, parse_mode="html")
        return

    # Si se ha indicado un texto de búsqueda
    else:
        time.sleep(1)
        print(f'Buscando en Google: "{texto_buscar}"')
        url = f'https://www.google.com/search?q={texto_buscar.replace(" ","+")}&num=50'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"
        headers = {"user-agent": user_agent}
        res = requests.get(url, headers=headers, timeout=10)
        
        if res.status_code != 200:
            print(f'Error al buscar: {res.status_code} {res.reason}')
            bot.send_message(message.chat.id, "Se ha producido un error. Inténtelo más tarde")
            return
        else:
            soup = BeautifulSoup(res.text, "html.parser")
            elementos = soup.find_all("div", class_="g")
            lista = []
            for elemento in elementos:
                try:
                    titulo = elemento.find("h3").text
                    url = elemento.find("a").attrs.get("href")
                    if not url.startswith("http"):
                        url = "https://google.com" + url
                    if [titulo, url] in lista:
                        continue
                    lista.append([titulo, url])
                except:
                    continue
        mostrar_pagina(lista, message.chat.id)
@bot.message_handler(func=lambda message: message.chat.type == 'group' or message.chat.type == 'supergroup')
def buscar_en_grupo(message):
    # Esta función se activa cuando se recibe el comando /buscar en un grupo
    # Puedes personalizar el comportamiento para grupos aquí

    bot.reply_to(message, "La búsqueda está disponible solo en chats personales.")

# Resto del código...
# ...

def mostrar_pagina(lista, cid, pag=0, mid=None):
    # Crea o edita un mensaje de la página
    # Creamos la botonera
    markup = InlineKeyboardMarkup()
    b_anterior = InlineKeyboardButton("◀⬅", callback_data="anterior")
    b_cerrar = InlineKeyboardButton("❌", callback_data="cerrar")
    b_siguiente = InlineKeyboardButton("➡▶", callback_data="siguiente")
    inicio = pag * N_RES_PAG  # Número resultados inicio de página en curso
    fin = pag * N_RES_PAG + N_RES_PAG  # Número resultado fin de página en curso
    markup.row(b_anterior, b_cerrar, b_siguiente)
    mensaje = f'<i>Resultados {inicio+1}-{fin} de {len(lista)}</i>\n\n'
    n = 1
    for item in lista[inicio:fin]:
        mensaje += f'[<b>{n}</b>] <a href="{item[1]}">{item[0]}</a>\n'
        n += 1
    if mid:
        bot.edit_message_text(mensaje, cid, mid, reply_markup=markup, parse_mode="html", disable_web_page_preview=True)
    else:
        res = bot.send_message(cid, mensaje, reply_markup=markup, parse_mode="html", disable_web_page_preview=True)
        mid = res.message_id
        datos = {"pag": 0, "lista": lista}
        pickle.dump(datos, open(f'{DIR["busquedas"]}{cid}_{mid}', 'wb'))



# Manejo de acciones de callback_data
@bot.callback_query_handler(func=lambda x: True)
def respuesta_botones_inline(call):
    cid = call.from_user.id
    mid = call.message.id

    if call.data == "cerrar":
        bot.delete_message(cid, mid)
        return
    datos = pickle.load(open(f'{DIR["busquedas"]}{cid}_{mid}', 'rb'))
    if call.data == "anterior":
        if datos["pag"] == 0:
            bot.answer_callback_query(call.id, "Ya estás en la primera página")
        else:
            datos["pag"] -= 1  # Retrocedemos una página
            pickle.dump(datos, open(f'{DIR["busquedas"]}{cid}_{mid}', 'wb'))
            mostrar_pagina(datos["lista"], cid, datos["pag"], mid)
        return
    elif call.data == "siguiente":
        if datos["pag"] * N_RES_PAG + N_RES_PAG >= len(datos["lista"]):
            bot.answer_callback_query(call.id, "Ya estás en la última página")
        else:
            datos["pag"] += 1  # Avanzamos una página
            pickle.dump(datos, open(f'{DIR["busquedas"]}{cid}_{mid}', 'wb'))
            mostrar_pagina(datos["lista"], cid, datos["pag"], mid)
        return

# Responde a mensajes que no son comandos
@bot.message_handler(content_types=["text"])
def message(message):
    # Gestiona los mensajes de texto recibidos
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        x = bot.send_message(message.chat.id, "<b>Holasss</b>", parse_mode="html")
        time.sleep(3)
        bot.edit_message_text("<u>Holisss</u>", message.chat.id, x.message_id, parse_mode="html")

# Configuramos los comandos disponibles del bot
bot.set_my_commands([
    telebot.types.BotCommand("/start", "Inicia el bot"),
    telebot.types.BotCommand("/botones", "Botones del directorio"),
    telebot.types.BotCommand("/buscar", "Búsqueda en la web"),
    telebot.types.BotCommand("/help", "Inicia el bot"),
    telebot.types.BotCommand("/ayuda", "Inicia también el bot"),
])
def recibir_mensajes():
    # Bucle infinito que comprueba si hay nuevos mensajes en el bot
    bot.infinity_polling()


# Iniciador del bot
if __name__ == '__main__':
    print('Estado: Iniciando el Bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot iniciado')

    sms = bot.send_message(CANAL_ID, "@YaichiAnimeBot ESTADO: Bot Iniciado!!!")
    sms2 = bot.send_message(MI_CHAT_ID, "@YaichiAnimeBot ESTADO: Bot Iniciado!!!")
    time.sleep(4)

    def contador(segundos):
        for i in range(segundos, 0, -1):
            print(f"[Quedan {i} seg]")
            bot.edit_message_text(f"@YaichiAnimeBot ESTADO: Bot Iniciado!!!\n¡Eliminando!... en {i} segundos", CANAL_ID, sms.message_id, parse_mode="html")
            bot.edit_message_text(f"@YaichiAnimeBot ESTADO: Bot Iniciado!!!\n¡Eliminando!... en {i} segundos", MI_CHAT_ID, sms2.message_id, parse_mode="html")
            time.sleep(1)
    print("¡Eliminando!")
    bot.edit_message_text("@YaichiAnimeBot ESTADO: Bot Iniciado!!!\n¡¡Eliminando...!!", CANAL_ID, sms.message_id, parse_mode="html")
    bot.edit_message_text("@YaichiAnimeBot ESTADO: Bot Iniciado!!!\n¡¡Eliminando...!!", MI_CHAT_ID, sms2.message_id, parse_mode="html")
    time.sleep(3)
    contador(5)
    bot.delete_message(MI_CHAT_ID, sms2.message_id)
    bot.delete_message(CANAL_ID, sms.message_id)
