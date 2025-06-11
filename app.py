import streamlit as st
import google.generativeai as genai
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Gerador de Ideias")
st.title("Gerador de Ideias Criativas para Marketing")

produto = st.text_input("Digite o tipo de produto:")

publico = st.text_input("Qual o público-alvo ?")

col1,col2,col3 = st.columns(3)
with col1:
    foco = st.selectbox("Objetivo principal da campanha:", ["Engajamento","Conversão de vendas","Reconhecimento de Marca","Educação do Público"])
with col2:
    rede_social = st.selectbox("Escolha a rede social:",["Instagram","Twitter","Youtube","Facebook"])
with col3:
    if rede_social == "Instagram":
        tipo_postagem = st.selectbox("Escolha o tipo de postagem:",["Storys","Feed","Reels"])
    elif rede_social == "Twitter":
        tipo_postagem = st.selectbox("Escolha o tipo da postagem:",["Foto","Vídeo"])
    elif rede_social == "Youtube":
        tipo_postagem = st.selectbox("Escolha o tipo de postagem:",["Shorts","Vídeo"])
    else: 
        tipo_postagem = st.selectbox("Escolha o tipo de postagem:",["Foto","Vídeo"])

hashtags = "não"
criacao_legenda = st.checkbox("Criação de legenda, se desejar marcar")
if criacao_legenda:
    hashtags = st.radio("Deseja incluir Hashtags:", ["Sim","Não"])
    legenda= "sim"
else:
    legenda = "não"

campanha_temporaria = st.checkbox("Campanha Sazonal, se desejar marcar. (ex: Dias das Mães, Black Friday, Natal)")
if campanha_temporaria:
    tema_evento = st.text_input("Qual é o evento ou data comemorativa?")
else:
    tema_evento = "Nenhum"

qtd_ideias = st.slider("Quantidade de Ideias:",1,5)

def logica(qtd_ideias,produto,publico,rede_social,tipo_postagem,legenda,foco,tema_evento):
    prompt = (
        f"Gere ideias de marketing com base nos seguintes parâmetros: \n"
        f"Produto:{produto} \n"
        f"Público-Alvo:{publico} \n"
        f"Rede Social:{rede_social} \n"
        f"Tipo de postagem:{tipo_postagem} \n"
        f"Com o foco:{foco}"
        f"Com o tema ou evento:{tema_evento}"
        f"{legenda} precisa de uma criação de uma legenda para publicação \n"
        f"{hashtags} precisa de uma criação de hashtags para publicação \n"
        f"Retorne: \n"
        f"Títulos para a campanha \n"
        f"Um slogan envolvente \n"
        f"{qtd_ideias} ideias de postagens para redes sociais \n"
        f"Responda em formato estruturado"
    )
    return prompt

def gerar_resposta_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
    
def gerar_pdf(texto):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    largura, altura = letter
    y = altura - 50
    for linha in texto.split('\n'):
        if y < 50:
            pdf.showPage()
            y = altura - 50
        pdf.drawString(50, y, linha)
        y -= 15
    pdf.save()
    buffer.seek(0)
    return buffer

if st.button("Gerar Ideias"):
    prompt = logica(qtd_ideias,produto,publico,rede_social,tipo_postagem,legenda,foco,tema_evento)
    with st.spinner("Gerando resposta ..."):
        resposta = gerar_resposta_gemini(prompt)
        st.write("**Resposta**")
        st.write(resposta)

        st.download_button(
            label="📥 Baixar Ideias como .txt",
            data=resposta,
            file_name="ideias_marketing.txt",
            mime="text/plain"
        )

        pdf_bytes = gerar_pdf(resposta)
        st.download_button(
            label="📄 Baixar como .pdf",
            data=pdf_bytes,
            file_name="ideias_marketing.pdf",
            mime="application/pdf"
        )