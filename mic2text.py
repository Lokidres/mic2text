import speech_recognition as sr
import threading

def transcribe_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("[+] Ortam dinleniyor, konuşabilirsiniz. (Enter'a basınca duracak)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("[>] Algılanan metin:", text)
    except sr.UnknownValueError:
        print("[!] Ses anlaşılamadı.")
    except sr.RequestError as e:
        print("[!] API isteği başarısız:", e)

def wait_for_enter():
    input()
    print("[*] Dinleme sonlandırıldı.")
    # Bu noktada mikrofon zaten kapanmış olacak.

def main():
    input("Başlamak için Enter'a basın...")
    
    listen_thread = threading.Thread(target=transcribe_speech)
    enter_thread = threading.Thread(target=wait_for_enter)

    listen_thread.start()
    enter_thread.start()

    listen_thread.join()
    enter_thread.join()

if __name__ == "__main__":
    main()
