# Importa bibliotecas necessárias
import random  # Para gerar números aleatórios
import streamlit as st  # Para criar interface web interativa
import time  # Para adicionar pausas na animação

# Título do aplicativo no Streamlit
st.title("🎯 Jogo da Adivinhação Interativo com Sorteio")

# --------------------------
# Inicialização do estado do jogo
# --------------------------
# O Streamlit mantém o estado entre interações usando st.session_state
# Aqui definimos variáveis principais do jogo apenas se ainda não existirem

# Número secreto aleatório entre 1 e 5
if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 5)

# Contador de tentativas do usuário
if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

# Lista para armazenar todos os palpites do usuário
if "palpites" not in st.session_state:
    st.session_state.palpites = []

# Número máximo de tentativas permitido
max_tentativas = 5

# --------------------------
# Entrada do usuário
# --------------------------
# Permite que o usuário insira um palpite usando um campo numérico
palpite = st.number_input("Digite seu palpite (1-5):", min_value=1, max_value=5, step=1)

# --------------------------
# Botão para verificar o palpite
# --------------------------
if st.button("Verificar"):
    # Incrementa o contador de tentativas
    st.session_state.tentativas += 1
    # Adiciona o palpite atual à lista de palpites
    st.session_state.palpites.append(palpite)
    
    # --------------------------
    # Animação de sorteio
    # --------------------------
    # Cria um espaço temporário para mostrar animação de "sorteio"
    sorteio_placeholder = st.empty()
    for i in range(10):
        # Exibe números aleatórios piscando para simular sorteio
        sorteio_placeholder.markdown(f"🎲 Sorteando... {random.randint(1,5)}")
        time.sleep(0.2)  # Pausa de 0,2s para efeito visual
    sorteio_placeholder.empty()  # Limpa a animação antes de mostrar o resultado

    # --------------------------
    # Verifica se o palpite está correto
    # --------------------------
    if palpite == st.session_state.numero_secreto:
        # Palpite correto → mensagem de sucesso
        st.success(f"🎉 Parabéns! Você acertou o número {st.session_state.numero_secreto} em {st.session_state.tentativas} tentativas!")
        # Reinicia o jogo
        st.session_state.numero_secreto = random.randint(1, 5)
        st.session_state.tentativas = 0
        st.session_state.palpites = []
    elif st.session_state.tentativas >= max_tentativas:
        # Usuário esgotou todas as tentativas → mensagem de erro
        st.error(f"😢 Suas 5 tentativas acabaram! O número era {st.session_state.numero_secreto}.")
        # Reinicia o jogo
        st.session_state.numero_secreto = random.randint(1, 5)
        st.session_state.tentativas = 0
        st.session_state.palpites = []
    elif palpite < st.session_state.numero_secreto:
        # Palpite menor que o número secreto → dica para tentar maior
        st.info(f"Tente um número maior! Tentativa {st.session_state.tentativas}/{max_tentativas}")
    else:
        # Palpite maior que o número secreto → dica para tentar menor
        st.info(f"Tente um número menor! Tentativa {st.session_state.tentativas}/{max_tentativas}")

# --------------------------
# Histórico de palpites
# --------------------------
# Mostra todos os palpites do usuário até o momento
if st.session_state.palpites:
    st.write("Seus palpites até agora:", st.session_state.palpites)
