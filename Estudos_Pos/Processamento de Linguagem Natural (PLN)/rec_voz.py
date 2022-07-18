import speech_recognition as sr

def rec_voz():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        # Usa função para reduzir ruido
        mic.adjust_for_ambient_noise(source)
        print("Fale no microfone: ")
        audio = mic.listen(source)
    try:
        # Usa o reconhecimento de voz
        res = mic.recognize_google(audio, language='pt-BR')
        print("Resultado: " + res)
    except sr.UnknownValueError:
        print("Erro:"+sr.UnknownValueError)
    return res
rec_voz()