import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit



audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'eco' in comando:
                comando = comando.replace('eco', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()
    elif 'calcule' and 'mais' or 'soma' or 'adição' in comando:
        comand = comando
        a = 0
        b = 0
        if "três" or "tres" or "treis" or "3" in comando:
            a = 3
        elif "um" or "1" in comando:
            a = 1
        elif "dois" or "2" in comando:
            a = 2
        elif "quatro" or "cuatro" or "4" in comando:
            a = 4
        elif 'cinco' or "cincu" or "5" in comando:
            a = 5
        elif "seis" or "6" or "seix" in comando :
            a = 6
        elif "sete" or "set" or "7" in comando:
            a = 7
        elif "oito" or "oto" or "8" in comando:
            a = 8
        elif "nove" or "9" in comando:
            a = 9
        elif "dez" or "deiz" or "dés" or "10" in comando:
            a = 10
        if "três" or "tres" or "treis" or "3" in comando:
            b = 3
        elif "um" or "1" in comando:
            b = 1
        elif "dois" or "2" in comando:
            b = 2
        elif "quatro" or "cuatro" or "4" in comando:
            b = 4
        elif 'cinco' or "cincu" or "5" in comando:
            b = 5
        elif "seis" or "6" or "seix" in comando :
            b = 6
        elif "sete" or "set" or "7" in comando:
            b = 7
        elif "oito" or "oto" or "8" in comando:
            b = 8
        elif "nove" or "9" in comando:
            b = 9
        elif "dez" or "deiz" or "dés" or "10" in comando:
            b = 10


comando_voz_usuario()