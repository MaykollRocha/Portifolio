import streamlit as st

from paginas.Globais import *


class SobreMin():
    
    def __init__(self):
        st.title("""Sobre Mim""")
        
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
        self.imprimir_estudo()
        st.header("Cursos")
        self.imprimir_curso()
        
        st.header("Experiências de trabalho")
        self.imprimir_trabalhos()
        st.header("Habilidades")
        st.markdown("""
                **Soft Skills:**  
                1. **Comunicação Eficaz:** Habilidade de transmitir ideias de forma clara e concisa, tanto verbalmente quanto por escrito.  
                2. **Trabalho em Equipe:** Capacidade de colaborar efetivamente com colegas e contribuir para um ambiente de trabalho positivo.  
                3. **Pensamento Analítico:** Forte habilidade para analisar dados e problemas de forma lógica e estruturada.  
                4. **Adaptabilidade:** Facilidade para se ajustar a novas situações e desafios, mantendo a eficiência e a produtividade.  
                5. **Gestão de Tempo:** Competência em gerenciar múltiplas tarefas e prazos, garantindo a entrega de projetos de qualidade.  
                **Hard Skills:**  
                1. **Programação:** Conhecimento em linguagens de programação como Python, Java, e SQL.  
                2. **Análise de Dados:** Experiência em técnicas de análise exploratória e estatística para extrair insights de grandes volumes de dados.  
                3. **Engenharia de Dados:** Habilidade em gerenciar e otimizar bancos de dados, incluindo habilidades em ferramentas como Hadoop e Spark.  
                4. **Matemática e Estatística:** Forte base em matemática aplicada e estatística, essencial para análises quantitativas e modelagem de dados.  
                5. **Ferramentas de BI:** Competência em ferramentas de Business Intelligence como Tableau e Power BI para visualização de dados.  
                    """)
        st.header("Linguagens de Programação")
        self.imprimir_linguagens()
    
    def imprimir_estudo(self):
        for estudo in estudos:
            st.markdown(f"""
                        **{estudo['instituicao']}**  
                        :blue[_{estudo['curso']}_]  
                        {estudo['grau']}, {estudo['periodo']}  
                        """)
    def imprimir_curso(self):
        for curso in curso_cary:
            aux = ""
            for materia in curso["materias"]:
                aux += f""":blue[{materia['materia']}] _{materia['status']}_, {materia['periodo']}  \n"""
            string = f"""**{curso['instituicao']}**  
                    {aux}:orange[Modalidade]: {curso['modalidade']}  
                    """
            st.markdown(string)


    def imprimir_trabalhos(self):
        for trabalho in trabalhos:
            st.markdown(f"""
            **{trabalho['estabelecimento']}**  
            :orange[Cidade]: {trabalho['cidade']}  
            :orange[Período]: {trabalho['periodo']}  
            :orange[Descrição da Função]  
            {trabalho['descricao']}
            """)

    def imprimir_linguagens(self):
        for linguagem in linguagens:
            st.markdown(f"""
            :blue[Linguagem]: {linguagem['nome']}  
            :blue[Ano que começou]: {linguagem['ano']}  
            :blue[Descrição e opinião]  
            {linguagem['descricao']}
            """)

    