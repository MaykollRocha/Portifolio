
import webbrowser

import streamlit as st

from paginas.Globais import *


class Trabalhos_C():
    
    def __init__ (self):
        self.texto_inicio()
        options = ['Option 1', 'Option 2', 'Option 3']

        for codigo in codigo_c:
            with st.expander(f"{codigo[0]}"):
                st.markdown(f"""
                            :blue[Materia]: {codigo[1][0]}  
                            :blue[Data]: {codigo[1][1]}  
                            :blue[Local]: {f"{codigo[1][2]}" if codigo[1][2] else " "}  
                            {f":blue[Professor]: {codigo[1][3]}  " if codigo[1][3] else " "}
                            {f":blue[Nota]: {codigo[1][4]}  " if codigo[1][4] else " "} 
                            """)
                st.markdown(f"""
                            :red[Projeto]:  
                            {codigo[2]}
                            """)
                if codigo[3] != 0:   
                    for i in codigo[3]:
                        st.image(f"imgs/{i[0]}",caption=i[1])
                if codigo[4] != 0: 
                    cont = 1                      
                    for i in codigo[4]:
                        st.subheader(f"{cont}. {i[0]}")
                        st.code(i[1])
                        st.markdown(i[2])
                        cont+= 1;
                st.markdown(f"""
                            :red[Visão sobre como foi o projeto]:  
                            {codigo[5]}
                            """)
                st.markdown(f"Para mais informações: [GitHub Atividade]({codigo[6]})")
        
            
        
    def texto_inicio(self):
        st.header("Linguagem C/C++")
        st.markdown("""Minha primeira linguagem de programação foi C. Esta linguagem oferece muitos ensinamentos e uma experiência única por ser muito próxima do hardware. A utilização de ponteiros foi a parte mais interessante que aprendi, e o trabalho com estruturas de dados me proporcionou uma melhor compreensão de como utilizá-la de maneira eficiente. Sempre gostei e continuo gostando muito de programar em C.  
Durante meus estudos acadêmicos, enfrentei quatro projetos desafiadores que me deram muita dor de cabeça, principalmente por minha falta de experiência em programação e estruturas de dados na época:  
1. **Simulação de todos os tipos de memória cache:** Esse projeto exigiu uma compreensão profunda dos conceitos de memória e sua implementação em C.  
2. **Desenvolvimento de um universo em C usando matriz esparsa:** Utilizei matrizes esparsas para criar uma simulação complexa, o que foi um desafio fascinante.  
3. **Cálculo de números primos em uma matriz utilizando threads em C++:** Este projeto envolveu o uso de threads para otimizar o cálculo de números primos, aprimorando minhas habilidades em programação paralela.  
4. **Implementação de um jogo de ping-pong usando MPI:** Trabalhei com a interface de passagem de mensagens (MPI) para criar um jogo de ping-pong, o que exigiu uma compreensão avançada de comunicação entre processos.  
Esses projetos, em especial, foram fundamentais para o meu desenvolvimento como programador. Cada um deles me desafiou de maneiras únicas e contribuíram significativamente para minha formação acadêmica e profissional.  
                    """)
        
        
        