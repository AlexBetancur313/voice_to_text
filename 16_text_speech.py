import time
from gtts import gTTS

def texto_a_voz(texto, ruta_salida ="C:\\Users\\PC\\Desktop\\Notas-Lenguajes\\Python\\automatizacion\\voz.mp3"):
  inicio = time.time()
  print("Generando locución con API de Google TTS")
  # lang="es" Idioma para locución
  # tld="es" Dominio de Google
  # lang_check=False Comprobrar si elñ idioma detectado en el texto esta disponible
  gTTS.GOOGLE_TTS_MAX_CHARS = 200
  tts = gTTS(texto,lang="es",tld="es",lang_check=False)
  
  tts.save(ruta_salida)
  print(f'Tiempo: {time.time()-inicio} segundos')
  



  # MAIN
if __name__ == '__main__':
   texto = "Puedes ajustar el texto y el idioma según tus necesidades y puedes personalizar el nombre y la ubicación del archivo. Este computador esta un poco ma, espero y pueda tener para este año dinero suficiente para comparar un computador nuevo"
   texto_a_voz(texto)