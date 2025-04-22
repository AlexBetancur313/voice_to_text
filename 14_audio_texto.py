from pydub import AudioSegment
import speech_recognition as sr
import math
import os

# Cargar archivo de audio
audio_file = "C:\\Users\\PC\\Desktop\\Notas-Lenguajes\\Python\\automatizacion\\Cancion.wav"
sound = AudioSegment.from_wav(audio_file)

# Duración total del audio en milisegundos
duration_ms = len(sound)
segment_ms = 30000  # 30 segundos

# Crear recognizer
r = sr.Recognizer()
transcript = ""

print("Iniciando procesamiento por fragmentos...")

# Dividir y procesar
for i in range(0, duration_ms, segment_ms):
    segment = sound[i:i + segment_ms]
    segment_path = f"temp_segment_{i}.wav"
    segment.export(segment_path, format="wav")

    with sr.AudioFile(segment_path) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio, language='es-ES')
            transcript += text + " "
            print(f"Segmento {i//1000}-{(i+segment_ms)//1000} seg: OK")
        except Exception as e:
            print(f"Error en el segmento {i//1000}-{(i+segment_ms)//1000}: {e}")
    
    os.remove(segment_path)

print("\nTranscripción completa:")
print(transcript)
