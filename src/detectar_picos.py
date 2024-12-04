from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import os

def detectar_picos_audio(caminho_audio, min_duracao=1500, limiar_silencio=-20, duracao_minima_short=30000):
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
    picos_filtrados = []
    for inicio, fim in picos:
        if (fim - inicio) < duracao_minima_short:
            fim = min(inicio + duracao_minima_short, len(audio))  # Expande, mas não ultrapassa o áudio
        picos_filtrados.append((inicio, fim))

    return picos_filtrados

def cortar_trechos_video(video_path, momentos, output_folder="shorts"):
    """
        Corta os momentos destacados de um vídeo e salva como arquivos separados.
        - video_path: Caminho do vídeo original.
        - momentos: Lista de intervalos [(inicio, fim), ...] em milissegundos.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, (inicio, fim) in enumerate(momentos):
        inicio_seg = inicio / 1000
        fim_seg = fim / 1000
        output_file = os.path.join(output_folder, f"short_{i + 1}.mp4")

        comando = (
            f'ffmpeg -i "{video_path}" -ss {inicio_seg} -to {fim_seg} '
            f'-vf "scale=-1:1920, crop=1080:1920, pad=1080:1920:(ow-iw)/2:(oh-ih)/2, setsar=1" '
            f'-c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k "{output_file}"'
        )

        os.system(comando)
        print(f"Trecho salvo em: {output_file}")


caminho_audio = "audios/Descobri uma estratégia no Fortnite que mudou tudo... 😱.mp3" # AQUI VC COLOCA O CAMINHO DO AUDIO
momentos_relevantes = detectar_picos_audio(caminho_audio)

video_path = "videos/Descobri uma estratégia no Fortnite que mudou tudo... 😱.mp4" # AQUI VC COLOCA O CAMINHO DO VPIDEO
cortar_trechos_video(video_path, momentos_relevantes)
