from pydub import AudioSegment
from pydub.silence import detect_nonsilent

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

caminho_audio = "audios/E se o YURI ALBERTO fosse para o REAL MADRID？ GANHARIA TUDO？.mp3"
momentos_relevantes = detectar_picos_audio(caminho_audio)
print("Momentos relevantes (ms):", momentos_relevantes)