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
# 2 : Breve descrição de como foi o trabalho
# 3 : Imagem
#   0 : nome
#   1 : rodape
# 4 : Lista de codigos
#   0 : codigo
#   1 : Parte interessante
# 5 : O valor que ele agregou na minha programação
# 6 : Link do GitHub

codigo_c = [
    ["Universo com Matriz Esparsa",
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
            [["estruturas.png","Imagem referente ao pdf no github"]],
            0,
            """
            Foi realmente um projeto muito interessante. Na época em que o fiz, minha mentalidade em relação à
            otimização de código e à qualidade de programação era bem limitada. Se eu já tivesse cursado 
            Algoritmos e Estruturas de Dados III, teria tido uma visão muito melhor de como desenvolver 
            esse código. No entanto, foi uma experiência inesquecível de prova, que contribuiu 
            significativamente para o programador que sou hoje.
            """,
            "https://github.com/MaykollRocha/Atividades_Faculade/tree/main/Star_Wars"],
    ["Memoria Cache",
     ["Arquitetura e Organização de Computadores","Setembro de 2022","UFGD - Universidade Federal da Grande Dourados","Rodrigo Porfírio da Silva Sacchi","7.0"],
     """A ideia do projeto é implementar os três tipos de mapeamento de memória cache: Direto, Associativo por Conjunto e Totalmente Associativo. O programa recebe um arquivo .txt e permite escolher entre os três tipos de mapeamento. Você insere uma cadeia binária, e ele verifica se há espaço na memória cache.  
        Embora o funcionamento seja simples, sua construção como um todo é bastante complexa.  
        As imagens do mapeamento faz referencia a STALLINGS, William. Arquitetura e organização de computadores. 8. ed. São Paulo: Pearson, 2010. p. 86-116, imagens de mapeamentos.""",
    [["mapeamento_direto.png","Mapeamento Direto"],["mapeamento_associativo.png","Mapeamento Associativo"],["mapeamento_associativo_por_conjunto.png","Mapeamento Associativo por Conjunto"]],
    0,
    """Foi um trabalho que levou dois meses para ser concluído, e terminei apenas na última hora. Apesar da baixa nota, tenho muito carinho por esse projeto. Ainda me lembro de sonhar com maneiras de desenvolvê-lo. Hoje, como muitos dos meus primeiros projetos, eu teria uma metodologia muito melhor para desenvolvê-los. No entanto, é gratificante ver essa evolução, pois enriquece meu portfólio. Tanto esse quanto o da matriz esparsa foram feitos na mesma época. Os projetos das threads e do MPI foram realizados nos anos seguintes.""",
    "https://github.com/MaykollRocha/Atividades_Faculade/tree/main/Arquitetura_Mapeamentos"
    ],
    ["Envio e Recebimento de Mensagem",
    ["Sistemas Distribuidos","Janeiro de 2024","UFGD - Universidade Federal da Grande Dourados","Rodrigo Porfírio da Silva Sacchi","9.5"],
    """
    O projeto consiste em utilizar duas máquinas virtuais para trocar um grande volume de informações, já que não temos uma conexão estável. Dentro de cada máquina, executamos dois processos distintos. Eles irão trocar um alto volume de informações, sendo que a quantidade de dados varia de 2^0 a 2^19, ou seja, de 1 a 524.288 valores. A troca de informações é realizada de forma não bloqueante tanto na hora de enviar quanto de receber. Inicialmente, os dados são enviados do processo 0 para o processo 1, e então o processo 1 retorna os dados para o vetor vazio do processo 0. O tempo necessário para essa operação é registrado.  
    O codigo foi feito para o terminal ubunto.
    """,
    [["output.png","Saida do codigo no terminal Ubunto"]], 
    [
        ["Bibliotecas/Prototipações",
         """
        #include <stdio.h>
        #include <mpi.h>
        #include <ctime>
        #include <cmath>
        #include <random>    
        
        void print_com_verificacao(double dadosE[], double dadosR[],double Fim,double Inicio,int tam);
        void print_sem_verificacao(double dadosE[], double dadosR[],double Fim,double Inicio,int tam);
        void encherce_envio(double dadosE[],int tam);   
         ""","Funções protótipos"],
        ["Main",
         """
         int main()
{
	int rank;//Não vou utilizar o size então não vou pedir a entrada deste so dos rankings
	MPI_Init(NULL, NULL);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	//Caso entre com um rank maior que 1 que seria mais de 2 maquinas ele simplesmente)
	if(rank > 1){
		 MPI_Finalize();
		 return 0 ;
	}
	//Apenas o printa o cabeça-lho da tabela.
	if(rank == 0){
		 printf("+-------+-----------------+---------------+\n");
		 printf("|n      | tempo(segundos) |  Taxa(MB/s)   |\n");
		 printf("|-------+-----------------+---------------|\n");
	}
	for (int i = 0; i < 20; i++)
	{
		int tam = pow(2, i);
		double *dadosE = new double[tam]; // Aloca o vetor de envio dinamicamente 
		double *dadosR = new double[tam]; // Aloca o vetor de recebimento dinamicamente
		//OBS: O rank 1 não usa o vetor de DadosE so de so o dadosR e elvia o mesmo que chega em tal
		//para o ranking 0;

		//Enche o vetor de recebimento com os números aleatórios dos dois rank que
		//Cria um distribuição de numero reais aletorios entre 0 e 10000
		//Para que os dados enviado pelo Maquina 1 seja diferente da 2 os dois possiem uma semente diferente
		//Sendo a semente 1000 e a semente 1001
		if(rank == 0)encherce_envio(dadosE,tam);

		MPI_Request send_request, recv_request;
		//Calcula o tempo inicial
		double Inicio = MPI_Wtime();

		for (int j = 0; j < tam; j++)
		{
		    if (rank == 0)
		    {
		        MPI_Isend(&dadosE[j], 1, MPI_DOUBLE, 1, 0, MPI_COMM_WORLD, &send_request);
			    MPI_Wait(&send_request, MPI_STATUS_IGNORE);
		        MPI_Irecv(&dadosR[j], 1, MPI_DOUBLE, 1, 0, MPI_COMM_WORLD, &recv_request);
		      	MPI_Wait(&recv_request, MPI_STATUS_IGNORE);
			}
		    else if (rank == 1)
		    {
		        MPI_Irecv(&dadosR[j], 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &recv_request);
			    MPI_Wait(&recv_request, MPI_STATUS_IGNORE);
		        MPI_Isend(&dadosR[j], 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &send_request);
		        MPI_Wait(&send_request, MPI_STATUS_IGNORE);
			}
		}
		//Pega o tempo final
		 double Fim = MPI_Wtime();

		//O primeiro print checa se o mesmoq ue chegou no rank 1 é o mesmo que saio do 
		//Envio do 0 e chegou nele novemente pelo 1
		//if (rank == 0)print_com_verificacao(dadosE,dadosR,Fim,Inicio,tam);
		if (rank == 0)print_sem_verificacao(dadosE,dadosR,Fim,Inicio,tam);

		 delete[] dadosE;
		 delete[] dadosR;
	}
	if(rank==0)printf("+-------+-----------------+---------------+\n");
	MPI_Finalize();

	return 0;
}
         ""","Função Principal que faz o ping-pong"],
        ["Encher Matriz",
          """
        void encherce_envio(double dadosE[],int tam){
            std::uniform_real_distribution<double>unif(0,10000);
            std::default_random_engine re;
            for( int i = 0; i < tam; i ++)dadosE[i] = unif(re);
        }   
          ""","Encher os Vatores com numeros rodômicos Aleatórios"]],
    """Foi realmente um trabalho muito tranquilo, não demorei mais de uma semana, gostei de cada segundo programando este, alem
    de que meu colega de sala fazia outra matéria com o mesmo onde tinha a mesma ideia de projeto só que era com o send e recive bloquenate.""",
    "https://github.com/MaykollRocha/MPI_PingPong/tree/main"
    ],
    ["Soma de Primos na Matriz com Theads",
    ["Sistemas Operacionais","Novembro de 2023","UFGD - Universidade Federal da Grande Dourados","Marcos Paulo Mouro","10.0"],
    """
    O trabalho consiste em calcular números primos em uma matriz gerada aleatoriamente com sementes aleatórias. A matriz será subdividida em submatrizes menores, e as threads irão processar esses valores de forma paralela para realizar as somas.  
    A subdivisão da matriz deve gerar o menor número possível de submatrizes. O algoritmo busca otimizar essa divisão. Na seção de dados, haverá uma análise de desempenho que demonstrará, por meio de cálculos, o tamanho ideal das submatrizes em relação ao número de threads, evidenciando a correlação entre esses fatores para obter uma boa performance.
    """,
    0,
    [
        ["""Divão das Submatrizes""","""
     void sep_matriz(int l, int c, int tl, int tc)
{
    int l0, c0;//Valor incial onde minhas matriz estra
    int nmc = (c - (c % tc)) / tc;//Passos na coluna da minha matriz
    int nml = (l - (l % tl)) / tl;//Passos na linha da minha matriz
    int rc = c % tc;//Resto que sobra quando a matriz não da colunas perfeita
    int rl = l % tl;//Resto que sobra quando a matriz não da linhas perfeitas
    // tudo inicia do [0,0]
    //Setando parametros inicias
    c0 = 0;
    l0 = 0;
    int count;
    count = 0;
    vector<int> linhas;
    vector<int> colunas;
    vector<submatrizes> resto;//Esse funcina especialmente para 
    linhas.push_back(l0);
    colunas.push_back(l0);

    //Criando stacs de valores para fazer a submatriz MxN
    while (nml > count)
    {
        int l1 = l0 + tl;
        linhas.push_back(l1);

        l0 = l1;

        count++;
    }
    count = 0;
   
    while (nmc > count)
    {
        int c1 = c0 + tc;
        colunas.push_back(c1);
        c0 = c1;
        count++;

    }
    // Armazenando resto
    if (rc) {
        colunas.push_back(colunas[colunas.size() - 1] + rc);
        nmc++;
    }
    if (rl) {
        linhas.push_back(linhas[linhas.size() - 1] + rl);
        nml++;
    }

    //Aquile ele trabalha colunas por linhas
    for (int kl = 1; kl < nmc + 1; kl++)
    {
        //Trabalho por linhas
        for (int ll = 1; ll < nml + 1; ll++)
        {
            //Cria uma auxiliar 
            matrizes aux;
            aux.l = linhas[ll] - linhas[ll - 1];
            aux.c = colunas[kl] - colunas[kl - 1];
            aux.pross = 0;
            // caso consiga fazer uma submatriz com o tamanho correto ele faz caso não ele guarda os valores para fazer uso no futuro
            if (aux.l * aux.c == tl * tc) {
                aux.m = AlocaSubMatriz( colunas, linhas, kl, ll);
                vet_mat.push_back(aux);
            }
            else {
                for (int k1 = 0, k = colunas[kl - 1]; k < colunas[kl]; k1++, k++){
                    for (int j1 = 0, j = linhas[ll - 1]; j < linhas[ll]; j1++, j++){
                        submatrizes aux2;
                        aux2.l = j;
                        aux2.c = k;
                        resto.push_back(aux2);
                    }
                }
            }
            
            
        }
    }
    //Limpa as linhas e colunas que não é mais nescessário já que todos os enderaços já foram pré setados
    linhas.clear();
    colunas.clear();

    // caso não prescise fazer mais submatrizes ele para de trabalhar
    if (resto.size() == 0) return;

    //faz o numero maximo de submatriz MxN
    while (resto.size() >= (tc*tl)){
        matrizes aux;
        aux.l = tl;
        aux.c = tc;
        aux.pross = 0;
        aux.m = AlocaRest(&resto,tl,tc);
        vet_mat.push_back(aux);
    } 

    //Se restar algo ainda ele faz uma submatriz menor mxn que vai ser a unica diferente de todas as outras
    if (resto.size())
    {
        int rcs;
        rcs = 1;
        //ele não consegue contruir um matriz com valor primo, não exite matriz de valor de numero primo apenas vetor.
        if (chek_primo(resto.size())!=1) {
            int i = 2;
            //  Aqui ele procura os dois mmenores numero para 
            //  Alcançar a solução
            //  EX: se resta 20 valores para bor em uma sumatriz
            //  Ele pode fazer de 2 geitos 2x10 ou 4x5 matematicamente falando
            //  Melhor caso é o 4x5 que seria uma matriz mais redoda isso que ele faz
            //  Se for 100 nos podemos faze 1x100, 2x50,4x25,5x20,10x10, matematicamente a melhor
            //  Sera a 10 po 10 que somado é 20
            //  Tinha duas maneiras de acaçar esse valor uma seria pegando todo e vendo a menor soma
            //  101,52,29,25,20 ou você segue a ideia de Busca binaria
            //      1. Começo minha busca de 2 a Numeroa de valores que resta
            //      2. busco o proxo %i == 0 se econtra esse n é o novo valor de linha
            //      3. com isso incremento i
            //      4. busca é feita até que i < resto/i
            // com isso acho a menor soma automaticamente
            while (i < resto.size() / rcs) {
                if (resto.size() % i==0)rcs = i;
                i++;
            }    
        }
        int rls = (int)(resto.size())/ rcs;

        matrizes aux;
        aux.l = rls;
        aux.c = rcs;
        aux.pross = 0;
        aux.m = AlocaRest(&resto, rls, rcs);
        vet_mat.push_back(aux);
    }
    resto.clear();
}
""",
"""Este trecho de código mostra uma parte importante do processo de subdivisão da matriz. Nele, os elementos são armazenados em uma nova matriz, e o resto é mantido. É importante lembrar que toda a subdivisão depende de a matriz conter números primos ou não, pois números primos acabam se transformando em um vetor."""],
        ["""Threads""","""
      void my_parelelar_busca_prims(void* param)
{
    // Reber os parametros externos
    PARAM* paramt = (PARAM*)param;
    //Variaveis locais das threds
    bool sair_do_laco;//para ver se toda matriz foi percorrida
    sair_do_laco = FALSE;
    bool tem_id;//Para ver se tem algo para ver averiguado
    tem_id = FALSE;
    matrizes aux;//Para auxiliar pegar a submatriz que contem os indeces
    int somas;//Auxiliar temporaria que pega a soma da submatriz
    somas = 0;
    //Verifica se há submatris suficiente para cada indice
    if (vet_mat.size() > paramt->id)
    {
        aux = vet_mat[paramt->id];
        vet_mat[paramt->id].pross = 1;
        tem_id = TRUE;
    }

    while (TRUE)
    {   
        //Checa se ele conseguiu pegar algo logo de inicio
        if (tem_id) {
            somas = funcao_somatoria_primos_paralelo(aux.c, aux.l,aux.m);// Faz a soma uma a um e já coloca no epaço da soma
            paramt->count += 1;//Conta o numero de matrizes analisadas
        }
        
        //Faz uma seção critica para soma
        WaitForSingleObject(SecCrtSoma, INFINITE);//Sessão para espera dos outros processo
        sum += somas;
        ReleaseMutex(SecCrtSoma);
        //Faz uma sessão crítcia para tirar valores da sub matriz
        WaitForSingleObject(SecCrtRetirada, INFINITE);//Sessão para espera dos outros processo
        if (num_threads > vet_mat.size()) sair_do_laco = TRUE;
        
        //Comça no numero de treads
        for (int i = num_threads; i < vet_mat.size(); i++)
        {
            if (vet_mat[i].pross == 0)//Checa se já não foi consumida
            {
                vet_mat[i].pross = 1;
                aux = vet_mat[i];
                break;
            }
            //Confirma que já foi tudo averiguado e sai da matriz
            if ((i + 1) == vet_mat.size()) {
                sair_do_laco = TRUE;
                break;
            }
        }
        ReleaseMutex(SecCrtRetirada);
        // Caso todos os valores da sub matriz tenha sido checado e todos apresentão como processado sai da sub matriz
        if (sair_do_laco) break;
    }

    // Termina Thread
    _endthread();
}

int processar_em_paralelo()
{   
    vector<HANDLE> hThread;// Armazenas as therds
    vector<PARAM> vParam;// Armazena os parametros de cada thread
    PARAM addve;// auxiliar para receber e enxer os parametros

    //Sessão critica de soma
    SecCrtSoma = CreateMutex(NULL, FALSE, NULL);
    // sessão critoca de checar e pegar as submtrizes
    SecCrtRetirada = CreateMutex(NULL, FALSE, NULL);

    // Encher os parametros com o indice da thread e tbem para contar quantas threads ele pegou
    for (int i = 0; i < num_threads; i++)
    {
        addve.id = i;
        addve.count = 0;
        vParam.push_back(addve);
    }

    //Criar as threads todas suspensas
    for (int i = 0; i < num_threads; i++)
        hThread.push_back(CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)&my_parelelar_busca_prims, &vParam[i], CREATE_SUSPENDED, NULL));
    
    int init, find;// variaveis de conta clock
    
    //Informa o inicio do processo
    cout << "Começou os processos" << endl;

    //incia a contagem de tempo
    init = clock();

    // Incia as theads
    for (int i = 0; i < num_threads; i++) {
        ResumeThread(hThread[i]);
    }

    // Espera todos os objetos terminar
    WaitForMultipleObjects(num_threads, hThread.data(), TRUE, INFINITE);

    //Fecha as treads
    for (int i = 0; i < num_threads; i++) {
        CloseHandle(hThread[i]);
    }

    //Para de contar o tempo
    find = clock(); 

    //Informa que acabou o processo
    cout << "saiu os processos" << endl;

    //Fecha as sessões crítica
    if (SecCrtSoma != 0)
        CloseHandle(SecCrtSoma);
    if (SecCrtRetirada != 0)
        CloseHandle(SecCrtRetirada);
    
    //Conta o numero de submatriz processada
    int sun_matrix_process = 0;
    cout << "Informações apos o termino do processamento:" << endl;

    //Informa qunato cada indice processou
    for (int i = 0; i < num_threads; i++) {
        cout << "Processador de identidade [" << vParam[i].id << "]" << "processou: " << vParam[i].count << endl;
        sun_matrix_process += vParam[i].count;
    }

    //Mostra quantas foram processadas
    cout << sun_matrix_process << endl;

    //Retorna o clok to tempo
    return find - init;

}
      ""","""Essa é a parte que faz as threads e um pré preparamento depois que já temos as matrizes cheias."""]],
    """Foi um dos trabalhos mais desafiadores que fiz, depois do projeto de memória cache. Embora a parte relacionada às threads fosse relativamente simples, a subdivisão das matrizes foi, sem dúvida, um dos maiores desafios. Consegui demonstrar a inviabilidade de criar uma matriz de números primos, já que, por definição, um número primo é indivisível além de por um e por ele mesmo.""",
    "https://github.com/MaykollRocha/Trabalhos_SO/tree/main"
        ],
    ["Jogo da cobrinha",
         ["hobby","31 de Julho de 2023","Dourados-MS",0,0],
         """A ideia principal do projeto é desenvolver um jogo da cobrinha utilizando uma lista encadeada. Nele, você usa as setas do teclado para mover a cobra, que se desloca de forma contínua. O projeto faz uso intensivo de ponteiros para controlar o movimento da cobra no mapa. À medida que a cobra se move, os ponteiros ajustam sua posição e o último segmento da cobra é atualizado de acordo.  
            Além disso, o jogo pinta o pixel onde a cobra está localizada e utiliza uma matriz para representar o espaço de jogo, permitindo que a cobra se mova dentro dela. A lista encadeada é utilizada para gerenciar o crescimento da cobra conforme ela coleta itens, permitindo a adição de novos segmentos ao corpo da cobra. O projeto também inclui a funcionalidade de salvar a pontuação em um arquivo .txt, registrando os pontos acumulados pelo jogador.""",
         0,
         0,
         """Minha experiência ao desenvolver esse projeto foi extremamente agradável. Gostei de cada minuto, pois estava totalmente confiante de que a ideia funcionaria. Logicamente, não é fácil criar algo que simule gráficos em C, mas à medida que o projeto avançava, tudo se tornava cada vez mais real e satisfatório. No final das contas, o resultado foi muito bom e recompensador.""",
         "https://github.com/MaykollRocha/Jogo_da_cobrinha"
         ],
    ["Calculadora Binaria",
     ["Atividade Prática Arquitetura","5 de Julho de 2023","UFGD - Universidade Federal da Grande Dourados","Rodrigo Porfírio da Silva Sacchi","10.0"],
    """Esse é um trabalho desenvolvido por mim com o auxilo de um colega de sala, durante a matéria aquitetura e organização de computadores um projeto prático avaliativo foi posto em pauta onde teriamos que senvolver uma calculadora bit a bit onde eles faria os calculos como a maquina faz, para valores interios apenas e criar um terminal agradável de se ver e bem tratado na questão de erros e tudo mais.  
    O algoritmo criado em C foi desenvolvido em varias documentos cabeça e o Main possui apenas o menu de interação principal, a versão aqui expressa não é a entregue para o professor a que esta aqui tbemm faz calulo de 4 bits por ser mais legivel e entendivel do que as de 8,16 e 32 pricipalmente na parte da multiplicação e divisão.  
    Todas as operações são execultadas em complemento a 2 onde os positivos existe em um intervalo de 2^(n-1) - 1 e os negativos 2^(n-1). Isso se da para podermos ter apenas uma representação de zero.  
    Para multiplicação e divisão utilizamos o algoritmo de booth onde mostrar passo a passo de cada operação de divisão e/ou multiplicação.  
    Os algorimos Bases se basea em funções básicas como tranformar decimal para binario, expanção de bit, Bin decimal.  
    Os algoritmos de Calculos são Soma, Subtração, Multiplicação e Divisão.  
    Ao final de cada conta tem a representação decimal de cada uma das contas de acordo que deu certo caso de Underflow ou overflow verá algo errado.  
    Para saber mais o código todo ta bem comentado e sua correção ortográtca vai estar melhor do que a daqui expressa.  
""" ,
    0,
    0,
    """Programar isso foi uma excelente experiência. Demorei cerca de um dia para desenvolver os algoritmos e, como tive bastante tempo, tornei-o bastante educativo, mostrando as interações e todos os detalhes possíveis. Foi numa fase em que eu já estava programando muito melhor, o que resultou em um código muito mais limpo e fácil de utilizar.""",
    "https://github.com/MaykollRocha/Calculadora_Binaria"
    ],
    ]
