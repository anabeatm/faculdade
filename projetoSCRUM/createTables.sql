-- Criação da tabela para tarefas, incluindo informações como nome, descrição, tamanho, 
-- tempo estimado, e tempo gasto.
create table tasks(
	task_id serial primary key not null, -- Identificador único para cada tarefa
	nome_task varchar(50) not null, -- Nome da tarefa, obrigatório
	descricao_task varchar(500), -- Descrição da tarefa (opcional)
	tamanho int not null, -- Tamanho da tarefa (valor numérico, obrigatório)
	tempo_estimado_task int not null, -- Tempo estimado para concluir a tarefa (obrigatório)
	tempo_gasto int not null -- Tempo efetivamente gasto na tarefa (obrigatório)
);

-- Criação da tabela para a situação das tarefas.
create table situacao_task(
	situacao_tasks_id serial primary key not null, -- Identificador único para cada situação
	situacao varchar(15) not null -- Descrição da situação (ex: "Concluído", "Pendente")
);

-- Criação da tabela para sprints, incluindo nome, data de início e término.
create table sprints(
	sprints_id serial primary key not null, -- Identificador único do sprint
	nome_sprints varchar(10) not null, -- Nome do sprint (ex: "Sprint 1")
	data_inicio_sprint date not null, -- Data de início do sprint
	data_termino_sprint date not null -- Data de término do sprint
);

-- Criação da tabela para status geral de tarefas.
create table status_geral(
	status_geral_id serial primary key not null, -- Identificador único do status geral
	status varchar(500) not null -- Descrição detalhada do status
);

-- Associação entre tarefas e sprints, incluindo status geral.
create table task_sprint(
	task_sprint_id serial primary key not null, -- Identificador único para a associação
	sprints_id int not null references sprints(sprints_id) on update cascade, -- Referência ao sprint
	task_id int not null references tasks(task_id) on update cascade, -- Referência à tarefa
	status_geral_id int not null references status_geral(status_geral_id) on update cascade -- Referência ao status geral
);

-- Criação da tabela para status dos sprints.
create table status_sprints(
	status_sprints_id serial primary key not null, -- Identificador único do status do sprint
	situacao varchar(50) not null -- Descrição da situação do sprint (ex: "Em andamento")
);

-- Criação da tabela para projetos, incluindo informações como nome, escopo, e datas.
create table projeto(
	projeto_id serial primary key not null, -- Identificador único do projeto
	nome_projeto varchar(200) not null, -- Nome do projeto
	descricao text not null, -- Descrição detalhada do projeto
	data_inicio date not null, -- Data de início do projeto
	data_termino date not null, -- Data de término do projeto
	objetivo varchar(100) not null, -- Objetivo do projeto
	escopo varchar(100) not null -- Escopo do projeto
);

-- Associação entre projetos e sprints.
create table projeto_sprint(
	projeto_sprint_id serial primary key not null, -- Identificador único para a associação
	projeto_id int not null references projeto(projeto_id) on update cascade, -- Referência ao projeto
	sprints_id int not null unique references sprints(sprints_id) on update cascade -- Referência ao sprint
);

-- Tabela para tarefas relacionadas (dependências entre tarefas).
create table relacionadoA(
	relacionadoA_id serial primary key not null, -- Identificador único da relação
	nome_task varchar(50) not null -- Nome da tarefa relacionada
);

-- Associação entre tarefas e sua relação com outras tarefas e situações.
create table relacao_task(
	relacao_task_id serial primary key not null, -- Identificador único para a relação
	task_id int not null references tasks(task_id) on update cascade, -- Referência à tarefa
	situacao_tasks_id int not null references situacao_task(situacao_tasks_id) on update cascade, -- Situação da tarefa
	relacionadoA_id int references relacionadoA(relacionadoA_id) on update cascade, -- Referência à tarefa relacionada
	descricao varchar(100) -- Descrição da relação
);

-- Criação da tabela para funcionários, contendo informações básicas como nome, e-mail e senha.
create table funcionario(
	funcionario_id serial primary key not null, -- Identificador único do funcionário
	nome varchar(150) not null, -- Nome do funcionário
	email varchar(150) not null, -- E-mail do funcionário
	senha varchar(8) not null -- Senha do funcionário
);

-- Adiciona uma coluna para associar tarefas a funcionários.
alter table relacao_task
	add column funcionario_id int references funcionario(funcionario_id) on update cascade;

-- Adiciona uma coluna para associar tarefas a situações específicas.
alter table tasks
	add column situacao_task_id int not null references situacao_task(situacao_tasks_id) on update cascade;

-- Adiciona uma coluna para associar tarefas a funcionários responsáveis.
alter table tasks
	add column funcionario_id int not null references funcionario(funcionario_id) on update cascade;

-- Adiciona uma coluna para associar sprints ao status dos sprints.
alter table sprints
	add column status_sprint_id int not null references status_sprints(status_sprints_id) on update cascade;

-- Criação da tabela para status dos projetos.
create table status_projeto (
    status_projeto_id serial primary key not null, -- Identificador único do status do projeto
    status varchar(50) not null -- Descrição do status (ex: "Aprovado", "Em andamento")
);

-- Adiciona uma coluna para associar projetos ao status dos projetos.
alter table projeto 
	add column status_projeto_id int not null references status_projeto(status_projeto_id) on update cascade;

-- Criação da tabela para funções dentro do projeto.
create table funcao(
	funcao_id serial primary key not null, -- Identificador único da função
	descricao_funcao varchar(100) not null, -- Descrição da função (ex: "Scrum Master", "Desenvolvedor")
	esta_no_projeto boolean not null -- Indica se a função está ativa no projeto
);

-- Criação da tabela para membros do projeto, associando projetos, funcionários e funções.
create table membros(
	membros_id serial primary key not null, -- Identificador único do membro
	projeto_id int not null references projeto(projeto_id) on update cascade, -- Referência ao projeto
	funcionario_id int not null references funcionario(funcionario_id) on update cascade, -- Referência ao funcionário
	funcao_id int not null references funcao(funcao_id) on update cascade -- Referência à função
);
