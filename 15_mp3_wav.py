from pprint import pprint
from pymediainfo import MediaInfo
import time


def info_archivo(ruta_archivo):
  s = {
    "tipo":None,
    "formato": None,
    "video": {
      "formato":None,
      "resolucion":None,
      "fps":None,
      "bit_rate": None,
    },
    "audio":{
      "formato":None,
      "canales":None,
      "frame_rate": None,
      "sample_rate":None,
      "bit_rate":None,
    },
    "duracion":None, # En segundos
    "res":None,
  }
  
  try:
    info = MediaInfo.parse(ruta_archivo)
    if len(info.tracks) > 1:
      s["tipo"] = info.tracks[1].track_type.lower()
    for track in info.tracks:
      if track.track_type == "General":
        if track.duration:
          s["duracion"] = track.duration / 1000
        s["formato"] = track.format
      elif track.track_type == "Video":
        s["video"]["formato"] = track.format
        s["video"]["resolucion"] = f'{track.width}x{track.height}'
        s["video"]["fps"] = track.frame_rate
        s["video"]["bit_rate"] = track.bit_rate
        
      elif track.track_type == "Audio":
        s["audio"]["formato"] = track.format
        s["audio"]["canales"] = track.channel_s
        s["audio"]["frame_rate"] = track.samling_rate
        s["audio"]["bits"] = track.bit_depth
        s["audio"]["bit_rate"] = track.bit_rate
    
    s["res"] = "OK"
  except Exception as err:
    s["res"] = f'ERROR: {err}'
  return s
        
def convertir_a_wav(archivo_entrada,archivo_salida = None, frame_rate=48000, canales=1, bits=16):
  inicio = time.time()

if __name__ == '__main__':
  archivo = "C:\\Users\\PC\\Desktop\\Notas-Lenguajes\\Python\\automatizacion\\Prueba_cancion.mp3"
  
  res = info_archivo(archivo)
  pprint(res,sort_dicts=False)
  
  
  
# info = MediaInfo.parse("C:\\Users\\PC\\Desktop\\Notas-Lenguajes\\Python\\automatizacion\\Prueba_cancion.mp3")

# pprint(info.to_data(),sort_dicts=False) #Informacion del archivo