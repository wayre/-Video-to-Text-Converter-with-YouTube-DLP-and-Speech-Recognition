from baixar_video import baixar_video

def main():
  sample_link = "https://www.youtube.com/watch?v=xDGjs_rnb9A"
  print("Bem-vindo ao programa de transcrição de vídeo!")
  print("Por favor, insira o link do vídeo que deseja transcrição.")
  print(f"Exemplo: {sample_link}\n")
  link = input("Digite o link do vídeo: ")
  
  if link == "":
    print("Link não fornecido. O programa será encerrado.")
    return
  
  print(f"Baixando o vídeo de {link}...")
  baixar_video(link)

# Passo 1: Extrair o áudio do vídeo
# - Usar moviepy para carregar o vídeo e extrair o áudio
# - Salvar o áudio como um arquivo .wav ou outro formato

# Passo 2: Converter o formato do áudio se necessário
# - Usar pydub para converter o arquivo de áudio se não estiver no formato correto

# Passo 3: Fazer a transcrição
# - Usar SpeechRecognition para abrir o arquivo de áudio e transcrevê-lo em texto
# - Tratar possíveis erros de transcrição ou melhorar a qualidade do áudio

# Passo 4 (Opcional): Melhorar o fluxo, como remover ruídos do áudio antes de transcrever


if __name__ == "__main__":
  main()
    