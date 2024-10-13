import streamlit as st

pesquisas = [
    {
        "Titlo":"Regressão Linear",
        "Descrição":'''
            Um dos meus estudos mais interessantes foi sobre regressão linear, motivado por pura curiosidade em compreender o modelo em profundidade. Mergulhei em sua história, explorei suas fórmulas e fundamentos teóricos, além de examinar suas aplicações práticas. Esse estudo me proporcionou uma visão abrangente e detalhada, ampliando minha compreensão sobre o uso da regressão linear como uma ferramenta essencial na ciência de dados.  
        ''',
        "LinkPDF":"https://drive.google.com/file/d/1JNJOLPRZf5BPP0LJ-_xJmyn6wJ2piySz/view?usp=sharing",
        "Colaboratory":"https://colab.research.google.com/drive/1BH-e5sjW2BUfTM4f3SNXYFFu13CQJoUs?usp=sharing"
    },
]

class Pesquisas:
    
    def __init__(self):
        
        st.markdown('''
                    # Pesquisas
Minhas pesquisas concentram-se principalmente em algoritmos de Machine Learning (ML) e Inteligência Artificial (IA). Tenho o hábito de implementá-los manualmente para explorar suas nuances e, sempre que possível, buscar melhorias. Esse processo não só me ajuda a aprofundar meu conhecimento sobre o funcionamento dos modelos, como também me permite explorar novas formas de aplicá-los de maneira mais eficiente e inovadora.  
                    ''')

        for pesq in pesquisas:
            st.markdown(f"""
                        ### {pesq['Titlo']}  
                        {pesq['Descrição']}  
                        Documento PDF: [{pesq['Titlo']}]({pesq['LinkPDF']})  
                        Documento PDF: [Colaboratorio]({pesq['Colaboratory']})  
                    
                        """)
