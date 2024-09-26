import requests
import streamlit as st

from paginas.Globais import *


class Trabalhos_Py():
    
    def __init__ (self):
        self.introdução()
    
    def introdução(self):
        st.title("Python")
        st.markdown("""
Entrei na faculdade em 2021 e comecei a explorar o mundo da programação em 2022. Nos primeiros meses, a maioria da programação que eu via era em C. No entanto, quando procurei aprender uma linguagem mais versátil e prática, escolhi o Python. Durante a faculdade, tive uma matéria chamada Programação Aplicada à Engenharia, que usava Python, mas foi uma experiência horrível e não agregou nada de especial à minha vida ou ao meu portfólio, assim como muitas outras matérias que fiz até então.  
É interessante salientar que tudo o que realmente aprendi de Python foi por conta própria. O ponto de virada foi quando estudei Ciência de Dados usando Python. Embora o Python fosse apenas uma ferramenta para a programação, a matéria estava mais focada em Ciência de Dados. Eu já havia estudado muitos algoritmos e conceitos de Data Science antes de começar essa matéria, mas ela foi fundamental para me aprofundar em pontos que eu havia visto superficialmente, além de corrigir alguns pontos que eu não havia entendido corretamente.  
Assim, meu aprendizado em Python e Ciência de Dados se desenvolveu mais através do meu próprio esforço e estudos independentes do que através das matérias da faculdade.  
Um curso online que faço para ter uma base para aprentar como portifólio e que é descente é o curso da FreeCodeCamp e usarei minha esperiencias na atividade para mostrar mais essa introdução.                
                """)
        st.markdown("""
                    No meu portfólio, pretendo destacar dois pontos distintos: programação e ciência de dados. Embora a ciência de dados utilize a programação para facilitar o trabalho, ela se baseia fundamentalmente em matemática e estatística. Portanto, no meu portfólio, vou focar em projetos de programação em Python, onde utilizei diversas bibliotecas como Tkinter, Matplotlib e SymPy, que são bibliotecas matemáticas.  
Dessa forma, poderei mostrar minhas habilidades de programação de forma independente da ciência de dados, destacando os seguintes aspectos:  
1. **Programação em Python**:   
   - Projetos desenvolvidos com Python, utilizando bibliotecas como Tkinter para criar interfaces gráficas.  
   - Uso de Matplotlib para visualização de dados e criação de gráficos.  
   - Aplicação de SymPy para resolver problemas matemáticos e simbólicos.  

2. **Ciência de Dados**:  
   - Projetos que envolvem análise de dados, modelagem estatística e aplicação de algoritmos de machine learning.  
   - Exemplos de como utilizei Python para realizar análises de dados, implementar modelos preditivos e gerar insights.  
  
Com essa abordagem,nessa sessão de Python deixarei só minha programação em python evidente nada alem disso.  
                    """)

        st.subheader("Trabalhos finais da FreecCodeCamp")
        st.markdown("Os projetos que apresentarei nessa sessãos seram o da freeCodeCamp, em questão só as provas do curso não vou apresentar os desenvolvidos na aulas porem na mesma pasta tem os desenvolvidos na pasta.")
        self.criate_works(["https://raw.githubusercontent.com/MaykollRocha/estudos_python/main/FCC/Python%201%20of%205/data.dat",
                "https://raw.githubusercontent.com/MaykollRocha/estudos_python/main/FCC/Python%202%20of%205/data.dat",
                "https://raw.githubusercontent.com/MaykollRocha/estudos_python/main/FCC/Python%203%20of%205/data.dat",
                "https://raw.githubusercontent.com/MaykollRocha/estudos_python/main/FCC/Python%204%20of%205/data.dat",
                "https://raw.githubusercontent.com/MaykollRocha/estudos_python/main/FCC/Python%205%20of%205/data.dat"
                ])
        st.subheader("Projetos Usando a Biblioteca TKinter")
        st.markdown("Os projetos que apresentarei nessa sessãos seram o da TKinter biblioteca gráfica que já utilizei uma boa quantidade de vez e tive muita evolução usando ela, o projeto em quetão que apresentarei são os mais relevantes")
        self.criate_works(["https://raw.githubusercontent.com/MaykollRocha/estudos_python/main/Metodos/data.dat",
                           "https://raw.githubusercontent.com/MaykollRocha/JogoDaVelhaMinMax/refs/heads/main/data.bat",
                ])
        
        
    
    def puxar_codigo(self,caminho):
        response = requests.get(caminho)
        if response.status_code == 200:
            return response.text
        else:
            return 'Não tem codigo'
    
    def criate_works(self,urls):
        for data in urls:
            response = requests.get(data)

            # Verificar se a requisição foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                dat_content = response.text

                try:
                    # Usar eval() para converter a string do arquivo em um dicionário Python
                    codigo = eval(dat_content)
                except SyntaxError as e:
                    continue
            else:
                st.markdown("não tem nada")
            
            with st.expander(f"{codigo['nome']}"):
                st.markdown(f"""
                            :blue[Projeto titulo]: {codigo['infos']['atividade']}  
                            :blue[Data]: {codigo['infos']['dia']}  
                            """)
                st.markdown(f"""
                            :red[Projeto]:  
                            {codigo['descrição']}
                            """)
                st.markdown(f""":red[Código]:  """)
                try:
                    st.code(self.puxar_codigo(codigo['Código']), language="py", line_numbers=True)
                except:
                    st.code(codigo['Código'], language="py", line_numbers=True)
                
                if codigo['imag']:
                    st.markdown(f""":red[Output]:  """)
                    for imag in codigo['imag']:
                        st.image(f"imgs/{imag}")
                st.markdown(f"""
                            :red[Visão sobre como foi o projeto]:  
                            {codigo['agregamento']}
                            """)
                st.markdown(f"Para mais informações: [GitHub da Atividade]({codigo['link']})")