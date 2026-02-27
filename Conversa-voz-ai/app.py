import openai
from gtts import gTTS
import os

# Configuração da sua chave de API
openai.api_key = "SUA_CHAVE_AQUI"

def pipeline_conversa_voz(caminho_audio):
    # 1. Speech-to-Text com Whisper
    audio_file = open(caminho_audio, "rb")
    transcricao = openai.Audio.transcribe("whisper-1", audio_file)
    print(f"Você disse: {transcricao['text']}")

    # 2. Processamento com ChatGPT
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": transcricao['text']}]
    )
    texto_resposta = resposta.choices[0].message.content
    print(f"IA respondeu: {texto_resposta}")

    # 3. Text-to-Speech com gTTS
    tts = gTTS(text=texto_resposta, lang='pt')
    tts.save("resposta.mp3")
    
    # Reproduz o áudio (comando varia conforme o SO)
    os.system("mpg321 resposta.mp3") 

# Execução (exemplo com um arquivo de áudio gravado)
# pipeline_conversa_voz("pergunta.mp3")
