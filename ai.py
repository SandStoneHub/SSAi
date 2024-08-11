from gigachat import GigaChat
from config import GIGACHAT

def gen_text(prompt: str) -> str:
    with GigaChat(credentials=GIGACHAT, verify_ssl_certs=False) as giga:
        response = giga.chat(prompt)
        return response.choices[0].message.content
