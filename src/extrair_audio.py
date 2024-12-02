import os

def extrair_audio(video_path, output_folder='audios'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    nome_audio = os.path.splitext(os.path.basename(video_path))[0] + '.mp3'
    output_path = os.path.join(output_folder, nome_audio)

    comando = f'ffmpeg -i "{video_path}" -q:a 0 -map a "{output_path}"'

    os.system(comando)
    return output_path

def main():
    video_path = 'videos/E se o YURI ALBERTO fosse para o REAL MADRID？ GANHARIA TUDO？.mp4'
    extrair_audio(video_path)

if __name__ == '__main__':
    main()
    