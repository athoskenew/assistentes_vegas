# programa que exibe transcrição do audio no vegas
# esse arquivo precisa estar no mesmo path de audios /feito
import pyautogui
import keyboard
import clipboard
import speech_recognition as sr
from os import path
import os
import time

def show():
    
    # verifica se a tecla 't' foi pressionada
    if keyboard.read_key() == "t":
        print('opa executou')

        # salva a posicao que o mouse estava inicialmente
        atual = pyautogui.position()

        # clica no valor da track atual
        pyautogui.click(875,136)

        # aguarda ate o mouse se movimentar para o local
        time.sleep(0.3)

        # copia o valor que indica a track atual
        pyautogui.hotkey('ctrl', 'c')

        # move o mouse de volta pra posicao inicial
        pyautogui.moveTo(atual)

        # mostra no console o nome da faixa
        print(clipboard.paste())
        
        arquivo_selecionado = clipboard.paste().replace("\r\n", "")
        AUDIO_FILE = path.join(arquivo_selecionado+".wav") #procura o arquivo de audio
        r = sr.Recognizer() #chama a funcao de reconhecimento como 'r'

        with sr.AudioFile(AUDIO_FILE) as source: #abre o arquivo de audio
            audio = r.record(source)  # lê todo o arquivo de audio

        try:
            texto_reconhecido = r.recognize_google(audio,language="pt-BR")
            print("audio: " + texto_reconhecido ) #usa reconhecimento do google para fazer a transcrição
        #lança excessões no caso de erros
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
        except sr.RequestError as e:
            print("Não foi possível solicitar do google a transcrição {0}".format(e))

        # reseta o show()
    if keyboard != "":
        time.sleep(0.1) # aguarda um tempo para o reset
        show() # faz a execucao novamente (recursividade)


#inicia a execucao do programa
show()
