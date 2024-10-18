import subprocess
import os

def baixar_video(link_video):
  """
  Downloads a video from the given link using the yt-dlp command-line tool.
  
  Args:
      link_video (str): The URL of the video to be downloaded.
  
  Returns:
      bool: True if the download was successful, False otherwise.
  """
  arquivo="video.webm"
  # Verificar se o arquivo de destino já existe
  if os.path.exists(arquivo):
      print("O arquivo de destino já existe. Não será feito o download.")
      return False

  # Comando yt-dlp para baixar o vídeo
  comando = [
    "yt-dlp",
    "--progress",
    "--restrict-filenames",
    "--write-info-json",
    "-o",
    arquivo,
    link_video
  ]

  # Executar o comando com Popen para capturar a saída em tempo real
  processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

  # Ler a saída do processo em tempo real
  for linha in processo.stdout:
    #limpa a tela do terminal
    os.system("clear")
    print(linha, end="")  # Exibir a saída no terminal conforme ela ocorre

  # Aguardar o processo terminar e pegar o código de retorno
  processo.wait()

  # Verificar o código de retorno
  if processo.returncode != 0:
      print("Erro ao baixar o vídeo. Código de erro:", processo.returncode)
      return False

  # Passo 3: Verificar se o arquivo foi baixado corretamente
  if os.path.exists(arquivo) and os.path.getsize(arquivo) > 0:
      print("\nDownload concluído com sucesso!")
      return True
  else:
      print("\nErro: Arquivo não encontrado ou está vazio.")
      return False

