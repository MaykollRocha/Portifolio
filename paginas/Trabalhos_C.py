

import requests
import streamlit as st

from paginas.Globais import *


class Trabalhos_C():
    
    def __init__ (self):
        self.texto_inicio()
        self.criate_works()
        
            
        
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
    
    def criate_works(self):
        urls = ["Atividades_Faculade/main/Star_Wars",
                "Atividades_Faculade/main/Arquitetura_Mapeamentos",
                "MPI_PingPong/main",
                "Trabalhos_SO/main",
                "Jogo_da_cobrinha/main",
                "Calculadora_Binaria/main"]
        for data in urls:
            response = requests.get(f"https://raw.githubusercontent.com/MaykollRocha/{data}/data.dat")

            # Verificar se a requisição foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                dat_content = response.text

                try:
                    # Usar eval() para converter a string do arquivo em um dicionário Python
                    codigo = eval(dat_content)
                except SyntaxError as e:
                    continue
            else:
                continue

            with st.expander(f"{codigo['titulo']}"):
                st.markdown(f"""
                            :blue[Materia]: {codigo['info']['materia']}  
                            :blue[Data]: {codigo['info']['data']}  
                            :blue[Local]: {f"{codigo['info']['local']}" if codigo['info']['local'] else " "}  
                            {f":blue[Professor]: {codigo['info']['professor']}  " if codigo['info']['professor'] else " "}
                            {f":blue[Nota]: {codigo['info']['nota']}  " if codigo['info']['nota'] else " "} 
                            """)
                st.markdown(f"""
                            :red[Projeto]:  
                            {codigo['descricao']}
                            """)
                if codigo['imag']:   
                    for img in codigo['imag']:
                        st.image(f"imgs/{img['nome']}", caption=img['rodape'])
                if codigo['codigos']: 
                    cont = 1                      
                    for cod in codigo['codigos']:
                        st.subheader(f"{cont}. {cod['motivo']}")
                        st.code(cod['codigo'], language="c", line_numbers=True)
                        st.markdown(cod['descricao'])
                        cont += 1
                st.markdown(f"""
                            :red[Visão sobre como foi o projeto]:  
                            {codigo['agregamento']}
                            """)
                st.markdown(f"Para mais informações: [GitHub da Atividade]({codigo['Link']})")
        codigo = 0
        
        