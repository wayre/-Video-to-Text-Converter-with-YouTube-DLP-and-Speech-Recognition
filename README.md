# 🎥 Video-to-Text Converter with YouTube-DLP and Speech Recognition

Este projeto é um script em Python que baixa o vídeo de uma URL usando `yt-dlp`, extrai o áudio, e converte o áudio em texto usando reconhecimento de fala. Ele exibe o progresso do download em tempo real no terminal e garante que o arquivo foi baixado corretamente antes de processá-lo.

## 📝 Funcionalidades

- Baixar vídeos a partir de um link (usando `yt-dlp`).
- Exibir o progresso do download em tempo real.
- Extrair o áudio do vídeo baixado.
- Converter o áudio em texto utilizando reconhecimento de fala.
- Verificação de erros e integridade do download.

## 🛠️ Requisitos

Certifique-se de ter os seguintes pacotes instalados:

- Python 3.x
- yt-dlp (`pip install yt-dlp`)
- moviepy (`pip install moviepy`)
- SpeechRecognition (`pip install SpeechRecognition`)
- pydub (`pip install pydub`)
- ffmpeg (necessário para o processamento de áudio e vídeo)
  - Você pode baixar o `ffmpeg` [aqui](https://ffmpeg.org/download.html) ou instalá-lo via seu gerenciador de pacotes.

## 🚀 Como usar

Siga as instruções abaixo para rodar o projeto:

### 1. Clone o repositório

```
git clone https://github.com/wayre/Video-to-Text-Converter-and-Speech-Recognition
cd Video-to-Text-Converter-and-Speech-Recognition
```

### 2. Instale as dependências

Use o `pip` para instalar os pacotes Python necessários:

```
pip install -r requirements.txt
```

> **Nota**: O arquivo `requirements.txt` deve conter as seguintes dependências:
>
> `yt-dlp moviepy SpeechRecognition pydub`

### 3. Certifique-se de que o `ffmpeg` está instalado

- No **Windows**: Adicione o `ffmpeg` ao seu PATH.
- No **macOS**: Instale via `brew`:

```
brew install ffmpeg
```

- No **Linux**: Instale via gerenciador de pacotes:

```
sudo apt install ffmpeg
```

### 4. Rodando o script

Para baixar um vídeo, extrair o áudio e transcrever para texto, rode o script fornecendo o link do vídeo:

```
python video_to_text.py
```

O script solicitará que você insira a URL do vídeo:

```
Digite o link do vídeo: https://www.youtube.com/....
```

O progresso do download será exibido no terminal em tempo real. Após a conclusão do download, o áudio será extraído e transcrito para texto.

### 5. Transcrição do áudio

O arquivo de texto resultante será salvo no diretório do projeto, contendo a transcrição do áudio extraído do vídeo.

## 📂 Estrutura do projeto

```
├── src/baixar_video.py    # Script download youtube video
├── src/main.py            # Script principal do projeto
├── README.md              # Documentação do projeto
├── requirements.txt       # Lista de dependências do projeto
```

## ⚠️ Possíveis Erros e Soluções

- **`yt-dlp: comando não encontrado`**:

  Certifique-se de que o `yt-dlp` está instalado corretamente. Rode `pip install yt-dlp` para instalar.

- **`ffmpeg: comando não encontrado`**:

  Verifique se o `ffmpeg` está instalado e adicionado ao PATH do seu sistema.

- **Erro ao transcrever áudio**:

  Verifique se o arquivo de áudio foi corretamente extraído e está em um formato suportado.

## 🛡️ Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.
