from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import os

def detectar_picos_audio(caminho_audio, min_duracao=500, limiar_silencio=-30):
    """
        Detecta os trechos não silenciosos no áudio.
        - caminho_audio: Caminho do arquivo MP3.
        - min_duracao: Duração mínima de um trecho não silencioso (em ms).
        - limiar_silencio: Volume mínimo considerado como "som" (em dBFS).

        Retorna: Lista de intervalos [(inicio, fim), ...] em milissegundos.
    """
    audio = AudioSegment.from_mp3(caminho_audio)
    picos = detect_nonsilent(audio, min_silence_len=min_duracao, silence_thresh=limiar_silencio)
    return picos

def cortar_trechos_video(video_path, momentos, output_folder='shorts'):
    """
        Corta trechos do vídeo em que há momentos relevantes.
        - video_path: Caminho do vídeo original.
        - momentos: Lista de intervalos [(inicio, fim), ...] em milissegundos.
        - output_folder: Pasta onde os trechos serão salvos.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, (inicio, fim) in enumerate(momentos):
        inicio_seg = inicio / 1000
        fim_seg = fim / 1000
        output_file = os.path.join(output_folder, f"short_{i + 1}.mp4")

        os.system(f'ffmpeg -i "{video_path}" -ss {inicio_seg} -to {fim_seg} -c copy "{output_file}"')
        print(f"Trecho {i + 1} salvo em {output_file}")


caminho_audio = "audios/E se o YURI ALBERTO fosse para o REAL MADRID？ GANHARIA TUDO？.mp3"
momentos_relevantes = detectar_picos_audio(caminho_audio)

video_path = "videos/E se o YURI ALBERTO fosse para o REAL MADRID？ GANHARIA TUDO？.mp4"
cortar_trechos_video(video_path, momentos_relevantes)
