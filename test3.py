from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Ruta al video original
video_path = "corto.mp4"

# Cargar el video original
video = VideoFileClip(video_path)

# Texto que deseas agregar
texto = "Texto que desesas agrega xxxxr"
texto2 = "Texto 2"

# Crear el clip de texto
clip_texto = TextClip(texto, fontsize=30, color='white', font='Arial-Bold')
clip_texto2 = TextClip(texto2, fontsize=30, color='white', font='Arial-Bold')


# Ajustar la duración del clip de texto
clip_texto = clip_texto.set_duration(3)
clip_texto = clip_texto.set_start(5)
clip_texto

clip_texto2 = clip_texto2.set_duration(3)
clip_texto2 = clip_texto2.set_start(8)

# Combinar el video original con el clip de texto
video_con_texto = CompositeVideoClip([video, clip_texto, clip_texto2])

# Ruta donde guardar el video con el texto agregado
output_path = "ss2.mp4"

# Exportar el video resultante
video_con_texto.write_videofile(output_path)