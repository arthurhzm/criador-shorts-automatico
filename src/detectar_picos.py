from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import os

def detectar_picos_audio(caminho_audio, min_duracao=1000, limiar_silencio=-20, duracao_minima_short=3000):
    """
    Detecta os trechos não silenciosos no áudio com filtros refinados.
    - min_duracao: Duração mínima de um trecho não silencioso (em ms).
    - limiar_silencio: Volume mínimo considerado como "som" (em dBFS).
    - duracao_minima_short: Duração mínima dos trechos relevantes para Shorts (em ms).

    Retorna: Lista de intervalos [(inicio, fim), ...] em milissegundos.
    """
    # Carrega o áudio
    audio = AudioSegment.from_mp3(caminho_audio)

    # Detecta trechos não silenciosos
    picos = detect_nonsilent(audio, min_silence_len=min_duracao, silence_thresh=limiar_silencio)

    # Filtra trechos pela duração mínima para Shorts
    picos_filtrados = [(inicio, fim) for inicio, fim in picos if (fim - inicio) >= duracao_minima_short]

    return picos_filtrados

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
