# Projeto Criador de Shorts Automático

Este projeto automatiza o processo de criação de vídeos curtos (shorts) a partir de vídeos do YouTube. O fluxo do projeto é dividido em três etapas principais:

1. **Baixar o vídeo do YouTube**:
    - No arquivo `baixar_video.py`, você deve colocar o link do vídeo do YouTube que deseja baixar.
    - O script utiliza a biblioteca `yt_dlp` para baixar o vídeo na melhor qualidade disponível e salvá-lo na pasta `videos`.

2. **Extrair o áudio do vídeo**:
    - No arquivo `extrair_audio.py`, o áudio do vídeo baixado é extraído e salvo na pasta `audios`.
    - O script utiliza o `ffmpeg` para realizar a extração do áudio, convertendo-o para o formato MP3.

3. **Gerar os shorts**:
    - No arquivo `detectar_picos.py`, são detectados os momentos relevantes no áudio e, em seguida, são gerados os vídeos curtos (shorts) a partir desses momentos.
    - A função `detectar_picos_audio` utiliza a biblioteca `pydub` para carregar o áudio e detectar trechos não silenciosos. Esses trechos são filtrados para garantir que tenham uma duração mínima adequada para shorts.
    - A função `cortar_trechos_video` utiliza o `ffmpeg` para cortar os trechos relevantes do vídeo original e salvá-los na pasta `shorts` já com o formato de vídeo shorts (9:16).

## Bibliotecas Utilizadas

- `yt_dlp`: Utilizada para baixar vídeos do YouTube.
  - Instalação: `pip install yt-dlp`
- `pydub`: Utilizada para manipulação de áudio, incluindo a detecção de trechos não silenciosos.
  - Instalação: `pip install pydub`
- `ffmpeg`: Utilizado para extração de áudio e corte de vídeos.
  - Instalação: Siga as instruções em https://ffmpeg.org/download.html para instalar o `ffmpeg` no seu sistema.
