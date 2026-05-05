Projeto: Sistema de Gestão (Tema Livre)
Objetivo
Desenvolver uma aplicação em Python que implemente um sistema de gestão completo (tema à escolha), com interface em linha de comandos (CLI) ou opcionalmente interface gráfica simples. O sistema deve permitir o registo, validação, armazenamento e manipulação de dados de forma persistente.
Requisitos Funcionais
1. Registo de dados
•
Criar novos registos (mínimo 5 atributos por entidade)
•
Geração automática de identificador único (ID)
2. Consulta e Pesquisa
•
Listar todos os registos
•
Pesquisa por:
o
ID
o
Nome (ou equivalente)
o
Outros campos relevantes
•
Implementar pelo menos 2 algoritmos de pesquisa, por exemplo:
o
Pesquisa linear
o
Pesquisa binária (em dados ordenados)
3. Atualização
•
Editar registos existentes com validação
4. Remoção
•
Eliminar registos com confirmação do utilizador
5. Ordenação de Dados
Implementar manualmente (sem usar apenas .sort()):
•
Pelo menos 2 algoritmos de ordenação diferentes, como:
o
Bubble Sort
o
Selection Sort
o
Insertion Sort
o
Merge Sort
o
Quick Sort
O utilizador deve poder escolher:
•
Campo de ordenação (ex: nome, data, preço)
•
Ordem (crescente/decrescente)
6. Estatísticas e Processamento
Implementar funcionalidades que envolvam processamento de dados, como:
•
Cálculo de médias, totais ou contagens
•
Identificação de valores máximos/mínimos
•
Filtros (ex: acima de X, dentro de intervalo, etc.)
Validações com Regex
Validar pelo menos 3 tipos de dados com expressões regulares, por exemplo:
•
Email → formato válido
•
Telefone → padrão nacional/internacional
•
Password → mínimo de caracteres, maiúsculas, números, etc.
•
Data → formato DD-MM-AAAA ou outro definido
Requisitos:
•
Bloquear entradas inválidas
•
Mensagens de erro claras e específicas
Persistência de Dados
Escolher uma opção:
•
JSON
•
CSV
•
SQLite (mais avançado)
O sistema deve:
•
Guardar quando solicitado e no fim do programa com escolha (S/N)
•
Carregar dados ao iniciar
Requisitos Técnicos
O projeto deve demonstrar:
•
Programação Orientada a Objetos (classes obrigatórias)
•
Modularização (múltiplos ficheiros)
•
Tratamento de exceções (try/except)
•
Separação entre lógica e interface
Funcionalidades Extra (Opcional)
•
Interface gráfica (ex: Tkinter)
•
Sistema de autenticação (login com validação por regex)
•
Exportação de dados
•
Logs de atividade
•
Testes automatizados
Desafio Extra
•
Comparar desempenho entre algoritmos de ordenação (tempo de execução)
•
Criar modo "benchmark"
•
Implementar estruturas como:
o
Pilhas (stack)
o
Filas (queue)
Entregáveis
•
Código em um repositório novo no GitHub, ex: joaoalvesTPSI0226
•
README com explicação das funcionalidades da app e instalação
Ideias de Temas
Aqui tens algumas sugestões de temas para o projeto:
Gestão Comercial
•
Sistema de gestão de loja (produtos, stock, vendas)
•
Gestão de encomendas online
Educação
•
Sistema de gestão de alunos e notas
•
Plataforma de cursos
Serviços
•
Sistema de reservas de hotel
•
Gestão de marcações (clínica, salão, etc.)
Mobilidade
•
Gestão de aluguer de carros
•
Sistema de boleias
Entretenimento
•
Biblioteca de jogos/filmes
•
Sistema de reviews e classificações
Produtividade
•
Gestor de tarefas (to-do list avançado)
•
Agenda pessoal com eventos
Saúde
•
Registo de treinos e progresso físico
•
Sistema de dietas/refeições
Ideias de Algoritmos
•
Biblioteca → ordenar livros por título, autor, ano
•
Loja → ordenar produtos por preço, stock
•
Alunos → calcular médias e rankings
•
Hotel → ordenar reservas por data
•
Aluguer → filtrar veículos disponíveis
•
Fitness → estatísticas de progresso