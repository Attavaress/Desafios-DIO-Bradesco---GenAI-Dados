# Conversa Multi-idiomas com Whisper, ChatGPT e gTTS

Este projeto integra três tecnologias de IA para criar uma interface de comunicação por voz fluida e inteligente.

## Tecnologias Utilizadas
* **OpenAI Whisper:** Transcrição robusta de áudio para texto (STT).
* **OpenAI ChatGPT:** Modelo de linguagem para geração de respostas contextuais.
* **Google Text-to-Speech (gTTS):** Síntese de voz para a resposta final.

## Como Funciona
1. O usuário fornece um arquivo de áudio ou entrada de voz.
2. O **Whisper** processa o áudio, lidando com sotaques e ruídos.
3. O texto resultante é enviado ao **ChatGPT**, que gera uma resposta.
4. O **gTTS** converte essa resposta em um arquivo `.mp3` para audição.

## Arquivos
* `talk_to_ai.py`: Script principal de integração.
