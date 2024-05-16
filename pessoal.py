import streamlit as st


class SobreMin():
    
    def __init__(self):
        st.title("""[Sobre Mim](#sobre-mim)""")
        st.header("Historia")
        st.write( """Olá! Meu nome é Maykoll Rocha, natural de Junqueirópolis, interior de São Paulo, no Oeste Paulista.
                 Tenho 21 anos, nascido em 17 de julho de 2002. Atualmente, estou cursando Engenharia de Computação, com
                 foco em Engenharia de Dados.  
                 Minha paixão pela área de Engenharia de Dados surge do meu fascínio pelo aspecto matemático e pela 
                 análise exploratória. Gosto de trabalhar com gerenciamento de dados e análises, buscando insights
                 valiosos para impulsionar decisões estratégicas.  
                 Estou comprometido em aprimorar minhas habilidades e conhecimentos constantemente, buscando contribuir
                 de forma significativa para projetos desafiadores e inovadores.
                """)
        st.header("Estudos")
        #Para adicionar um novo Ensino
        #0 : Nome da graduação 
        #1 : Curso 
        #2 : Grau de Ensino 
        #3 : inicio - termino
        estudos = [['Escola 13 de junho - Colégio Objetivo',"Ensino Médio","Ensino Médio","2018-2020"],
                ["Universidade Federal da Grande Dourados - UFGD","Engenharia da Computação","Ensino Superior","2021-2025"]]
        self.imprimir_estudo(estudos)
        st.header("Cursos")
        #Cursos cary Organização
        #0 : nome do curso
        #1 : Lista 
        #    0 : Materia
        #    1 : Status
        #    2 : Ano ou Ano de incio e fim
        #2 : Modalidade Presencial ou online
        curso_cary = [["Kumon - Junqueirópolis",[["Portugues","Concluido","2008-2016"],["Matemática","Concluido","2017-2020"]],"Presencial"],
                  ["CCAA - Junqueirópolis",[["Inglês","Incompleto","2014-2016"]],"Presencial"],
                  ["DATA SCIENCE ACADEMY(DSA)",[["Introdução à Ciência de Dados 3.0","Concluido","2022"],["Fundamentos de Linguagem Python Para Análise de Dados e Data Science","Concluido","2023"]],"Online"]]
        self.imprimir_curso(curso_cary)
        
        st.header("Experiências de trabalho")
        #Adicinar mais trabalhos
        #0 : Nome do estabelecimento
        #1 : Cidade
        #2 : Periodo de trabalho
        #3 : Descrição da função
        trabalhos = [["Kumon - Donomae","Dourados - Mato Grosso do Sul","meio de 2021 - incio de 2022","Auxiliar os professores na correção de materiais acadêmicos e ajudar alunos no conhecimento de conteúdos da minha area."]]
        self.imprimir_trabalhos(trabalhos)
    
    def imprimir_estudo(self,estudos):
        for i in estudos:
            st.markdown(f"""
                        **{i[0]}**  
                        :blue[_{i[1]}_]  
                        {i[2]}, {i[3]}  
                        """)
    def imprimir_curso(self,curso_cary):
        for curso in curso_cary:
            aux = ""
            for materias in curso[1]:
                aux += f""":blue[{materias[0]}] _{materias[1]}_, {materias[2]}  \n"""
            string = f"""**{curso[0]}**  
                    {aux}:orange[Tipo]: {curso[2]}  
                    """
            st.markdown(string)

    def imprimir_trabalhos(self,trabalhos):
        for trabalho in trabalhos:
            st.markdown(f"""
            **{trabalho[0]}**  
            :orange[Cidade]: {trabalho[1]}  
            :orange[Data]: {trabalho[2]}  
            :orange[Trabalho]  
            {trabalho[3]}
            """)
    
