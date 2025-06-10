import streamlit as st

st.title("Gerador de Ideias Criativas para Marketing")

st.text_input("Digite o tipo de produto:")

st.selectbox("Tom da Mensagem:",["Divertido","Profissional","Emocinal"])

st.text_input("Qual o público-alvo ?")

st.selectbox("Escolha a rede social:",["Instagram","Twitter","Youtube","Facebook"])

st.slider("Quantidade de Ideias:",1,5)

st.button("Gerar Ideias")