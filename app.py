import webbrowser

import streamlit as st


class Main():
    
    def __init__(self) -> None:
        st.set_page_config(page_title="Maykoll Rocha - Portifolio Pessoal",
            page_icon=None ,
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items=None
        )
        st.title("Maykoll Rocha - Portifólio")
       # Adicionar uma imagem
        st.image("imgs/eu.jpeg", caption="Maykoll Rocha", width=100)
        st.subheader("Contatos")
        itens = ["Email: maykoll1412@gmail.com", "Telefone: (18) 9 9699-3996", "Cidade: Doutados - MS", "Profifisão: Desempregado"]
        for item in itens:
            st.write(f"* {item}")
        # Adicionar um link para um PDF
        if st.button("Dowlond Curriculo"):
            webbrowser.open_new_tab("https://drive.google.com/file/d/1EaaRBFIIya1WIDCC5A9rA3FkIJ2WcXbw/view?usp=drive_link")
        self.side_bar() 

    def side_bar(self):

        if  st.sidebar.button("Sobre Mim"):
            self.pagina_sobre_mim()
        st.sidebar.header("Tabalhos")
    
    # Função para exibir a página "Sobre Mim"
    def pagina_sobre_mim(self):
        st.subheader('Sobre Mim')
        st.write( """
                Meu nome completo é Maykoll Rocha nascido em junqueirópolis interior de São Paulo, no Oeste Paulista, tenho 
                21 anos nascido no dia 17 de julho de 2002 e curso engenharia de computação, meu enfoque dos estudos em engenharia
                de dado, gosto de trabalhar com essa parte de gerencia e analise exploratória por conta do envolvimento
                matemático.
                """)
        
        

    # Função para exibir a página "Meus Estudos"
    def pagina_meus_estudos(self):
        st.subheader('Meus Estudos')
        st.write("Esta é a página 'Meus Estudos'. Aqui você pode colocar informações sobre seus estudos.")

    # Função para exibir a página "Trabalho"
    def pagina_trabalho(self):
        st.subheader('Trabalho')
        st.write("Esta é a página 'Trabalho'. Aqui você pode colocar informações sobre seu trabalho.")


Main()