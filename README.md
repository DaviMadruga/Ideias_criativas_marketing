
# 📌 Gerador de Ideias Criativas para Marketing
Um sistema SaaS com IA desenvolvido com Streamlit que auxilia profissionais de marketing, empreendedores e social media a gerar nomes de campanhas, slogans, ideias de postagens e legendas personalizadas para redes sociais. O sistema utiliza modelos generativos da Google (Gemini) para produzir resultados criativos com base nas preferências do usuário.

# 🧩 Funcionalidades
Entrada de:

- Tipo de produto

- Público-alvo

- Objetivo da campanha (engajamento, vendas, etc.)

- Rede social e tipo de postagem

- Campanha sazonal (opcional)

- Criação de legenda e hashtags (opcional)

Geração de:

- Título para a campanha

- Slogan

- De 1 a 5 ideias de postagens

Exportação:

- Download do conteúdo em .txt e .pdf

# 🧠 Tecnologias Utilizadas
| Tecnologia                        | Finalidade                    |
| --------------------------------- | ----------------------------- |
| **Python**                        | Lógica de programação         |
| **Streamlit**                     | Interface web interativa      |
| **Gemini (Google Generative AI)** | Geração de texto com IA       |
| **ReportLab**                     | Geração de PDFs               |
| **Google Generative AI SDK**      | Acesso à API do modelo Gemini |

# 📂 Estrutura do Projeto

```plaintext
gerador-ideias-marketing/
├── app.py                     # Código principal do Streamlit
├── requirements.txt           # Lista de dependências do projeto
├── README.md                  # Documentação do projeto
├── .streamlit/                # Configurações do Streamlit
│   └── secrets.toml           # Armazena a API_KEY
└── arquivos_exemplo/          # (opcional) Exemplos de saída
```

# 💻 Exemplo de Uso
- Preencha os campos com o tipo de produto e público-alvo.
- Selecione a rede social, tipo de postagem e o objetivo da campanha.
- (Opcional) Marque se é uma campanha sazonal, se deseja legenda e hashtags.
- Escolha quantas ideias quer gerar.
- Clique em "Gerar Ideias" e visualize o conteúdo sugerido.
- Faça o download do resultado em .txt ou .pdf.

# 📝 Exemplo de Prompt Enviado à IA
```
Gere ideias de marketing com base nos seguintes parâmetros: 
Produto: camiseta personalizada
Público-Alvo: jovens de 18 a 25 anos
Rede Social: Instagram
Tipo de postagem: ['Reels', 'Storys']
Com o foco: Engajamento
Com o tema ou evento: Nenhum
sim precisa de uma criação de uma legenda para publicação
Sim precisa de uma criação de hashtags para publicação

Retorne:
- Títulos para a campanha
- Um slogan envolvente
- 3 ideias de postagens para redes sociais
Responda em formato estruturado
```
# 📦 Requisitos
```
streamlit==1.36.0
google-generativeai==0.7.2
reportlab==4.1.0
protobuf==4.25.3
```

# Link do Streamlit
https://ideiascriativasmarketing-mu5yzt549knauijkgmn4m3.streamlit.app

# 👨‍💻 Autor
- Davi Madruga Cavalcanti
- Curso: Ciência da Computação
