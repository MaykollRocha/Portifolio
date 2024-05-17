#Para adicionar um novo Ensino
#0 : Nome da graduação 
#1 : Curso 
#2 : Grau de Ensino 
#3 : inicio - termino
estudos = [['Escola 13 de junho - Colégio Objetivo',"Ensino Médio","Ensino Médio","2018-2020"],
        ["Universidade Federal da Grande Dourados - UFGD","Engenharia da Computação","Ensino Superior","2021-2025"]]
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

#Adicinar mais trabalhos
#0 : Nome do estabelecimento
#1 : Cidade
#2 : Periodo de trabalho
#3 : Descrição da função
trabalhos = [["Kumon - Donomae","Dourados - Mato Grosso do Sul","meio de 2021 - incio de 2022","Auxiliar os professores na correção de materiais acadêmicos e ajudar alunos no conhecimento de conteúdos da minha area."]]


#Linguagens Organização
#0 : nome da Linguagem
#1 : Ano que começou a estudar 
#2 : Breve Descrição
linguagens = [["C/C++","2021","Primeira liguagem de programação que aprendi e usei muito durante a faculdade, já produzi muita coisas nela e as mais importante estará presente no portifólio."],
                      ["Python","2022","Apego mais forte por sua simplicidade e facilidade e compreenção sobre seu auto custo."],
                      ["Java","2023","Uma exlente linguagem para usar em desenvolvimento e aprendizagem de POO, porem tenho poucos feitos nela."],
                      ["VBA","2024","Em processo de utilização."]]

#-------------------Trabalhos em C ------------------------------------------
#Tenta colocar o mais resumido sobre o codigo
# 0 : Nome do trabalho
# 1 : Informações
#   0 : Matéria ou assunto
#   1 : Data que foi feito
#   2 : Local universidade ou cidade ou coloca none  
#   3 : Professor se não teve so por none
#   4 : nota se não teve so por none
#
#

codigo_c = [
    ["Universo com Matriz Sparça",
             ["Laboratório de Programação II",
              "25 de outubro de 2022 ",
              "UFGD - Universidade Ferderal da grande dourados",
              "Carlos Elias Armonio Zampieri",
              "7.0"],
            """
            A Prova 2 de Laboratório de Programação II foi a mais desafiadora que já enfrentei. A ideia era
            relativamente simples: você receberia três arquivos e precisaria alimentar uma matriz esparsa 
            com os dados contidos neles. O primeiro arquivo, chamado "Galáxia", fornecia o número de 
            estrelas e o nome da galáxia (cada matriz representava uma galáxia). O segundo arquivo, chamado
            "Estrela", trazia informações sobre cada estrela, incluindo código da estrela, número de corpos 
            celestes, fator de dobra, próxima estrela, e o nome da estrela. Os corpos celestes podiam ser de 
            quatro tipos: satélite, asteroide, planeta anão e planeta. Cada tipo de corpo celeste tinha um 
            código específico que precisava ser considerado.  
            O objetivo era utilizar a matriz esparsa para representar o espaço, empregando pilhas e filas
            para inserir os dados na matriz. Além disso, era necessário implementar uma função para carregar
            os dados na matriz esparsa e outras funcionalidades descritas no PDF disponível no GitHub. 
            Abaixo, há uma imagem ilustrativa de como as estruturas deveriam ser organizadas.
            """,
            ["estruturas.png","Imagem referente ao pdf no github"],
            """
            Foi realmente um projeto muito interessante. Na época em que o fiz, minha mentalidade em relação à
            otimização de código e à qualidade de programação era bem limitada. Se eu já tivesse cursado 
            Algoritmos e Estruturas de Dados III, teria tido uma visão muito melhor de como desenvolver 
            esse código. No entanto, foi uma experiência inesquecível de prova, que contribuiu 
            significativamente para o programador que sou hoje.
            """,
            "https://github.com/MaykollRocha/Atividades_Faculade/tree/main/Star_Wars"],
        ["Jogo da cobrinha",
         ["hobby","31 de Julho de 2023","Dourados-MS",0,0],
         """A ideia principal do projeto é desenvolver um jogo da cobrinha utilizando uma lista encadeada. Nele, você usa as setas do teclado para mover a cobra, que se desloca de forma contínua. O projeto faz uso intensivo de ponteiros para controlar o movimento da cobra no mapa. À medida que a cobra se move, os ponteiros ajustam sua posição e o último segmento da cobra é atualizado de acordo.  
            Além disso, o jogo pinta o pixel onde a cobra está localizada e utiliza uma matriz para representar o espaço de jogo, permitindo que a cobra se mova dentro dela. A lista encadeada é utilizada para gerenciar o crescimento da cobra conforme ela coleta itens, permitindo a adição de novos segmentos ao corpo da cobra. O projeto também inclui a funcionalidade de salvar a pontuação em um arquivo .txt, registrando os pontos acumulados pelo jogador.""",
         0,
         """Minha experiência ao desenvolver esse projeto foi extremamente agradável. Gostei de cada minuto, pois estava totalmente confiante de que a ideia funcionaria. Logicamente, não é fácil criar algo que simule gráficos em C, mas à medida que o projeto avançava, tudo se tornava cada vez mais real e satisfatório. No final das contas, o resultado foi muito bom e recompensador.""",
         "https://github.com/MaykollRocha/Jogo_da_cobrinha"
         ]
        ]