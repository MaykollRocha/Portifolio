import webbrowser

import streamlit as st

from paginas.pessoal import *
from paginas.Trabalhos_C import *


class Main():
    
    def __init__(self) -> None:
        st.set_page_config(page_title="Maykoll Rocha - Portifolio Pessoal",
            page_icon=None ,
            layout="wide",
            initial_sidebar_state="expanded",
        )
        st.title("Maykoll Rocha - Portifólio")
        col1, col2, col3,col4 = st.columns([1,2,2,1]) # Divide the layout into two columns
        
        # Column 1 (left side) - Image
        with col2:
            st.image("imgs/eu.jpeg", width=150)

        # Column 2 (right side) - Contacts and PDF link
        with col3:
            st.subheader("Contatos")
            itens = ["Email: maykoll1412@gmail.com", "Telefone: +55 (18) 9 9699-3996", "Cidade: Doutados - MS","Cursando: Engenharia de Computação"]
            string = ""
            for item in itens:
                string += f"""* {item}  \n"""
            st.write(string)
            # PDF Download Button
            if st.button("Download Currículo"):
                webbrowser.open_new_tab("https://drive.google.com/file/d/1el_CYCvMjbi2Sy7t9P4ZLLUQBLZlj5u6/view?usp=drive_link")
        self.side_bar() 

    def side_bar(self):
        if st.sidebar.button("Sobre Mim"):
            SobreMin()
        st.sidebar.header("Tabalhos")
        if st.sidebar.button("C"):
            Trabalhos_C()      
        

Main()
