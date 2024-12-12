-- Insere valores na tabela `situacao_task`, que representa as situações possíveis para uma tarefa.
INSERT INTO situacao_task (situacao) 
VALUES 
('Pendente'), 
('Em andamento'), 
('Concluída');

-- Insere valores na tabela `status_sprints`, indicando os status possíveis das sprints.
INSERT INTO status_sprints (situacao) 
VALUES 
('Ativa'), 
('Finalizada');

-- Insere valores na tabela `status_geral`, que indicam o status de uma tarefa dentro de uma sprint.
INSERT INTO status_geral (status) 
VALUES 
('Planejado'), 
('Em execução'),
('Bloqueada'),
('Transferida'), 
('Finalizado');

-- Insere valores na tabela `status_projeto`, que indicam os diferentes status que um projeto pode ter.
INSERT INTO status_projeto (status)
VALUES 
('Planejado'),
('Em progresso'),
('Concluído'),
('Cancelado'),
('Em análise');

-- Insere funções relacionadas aos membros dos projetos na tabela `funcao`, com um campo indicando se estão associados a um projeto.
INSERT INTO funcao (descricao_funcao, esta_no_projeto) 
VALUES 
('Product Owner', TRUE), 
('Scrum Master', TRUE), 
('Desenvolvedor', TRUE);

-- Insere registros na tabela `funcionario`, com informações como nome, email e senha.
INSERT INTO funcionario (nome, email, senha) 
VALUES 
('João Silva', 'joaosilva@gmail.com', 'senha123'),
('Maria Oliveira', 'mariaoliveira@gmail.com', 'senha456'),
('Carlos Pereira', 'carlospereira@gmail.com', 'senha789'),
('Ana Costa', 'anacosta@gmail.com', 'senha321'),
('Paulo Santos', 'paulosantos@gmail.com', 'senha654'),
('Fernanda Lima', 'fernandalima@gmail.com', 'senha987'),
('Lucas Almeida', 'lucasalmeida@gmail.com', 'senha741'),
('Isabela Rocha', 'isabelarocha@gmail.com', 'senha852'),
('Ricardo Nunes', 'ricardonunes@gmail.com', 'senha963'),
('Juliana Ribeiro', 'julianaribeiro@gmail.com', 'senha147');

-- Insere dois projetos na tabela `projeto`, especificando informações como nome, descrição, datas, objetivo, escopo e status.
INSERT INTO projeto (nome_projeto, descricao, data_inicio, data_termino, objetivo, escopo, status_projeto_id) 
VALUES 
('Sistema Gerenciador de Tarefas', 
 'Desenvolvimento de um sistema de gestão baseado no SCRUM', 
 '2024-10-01', 
 '2024-12-31', 
 'Aprimorar gestão de tarefas', 
 'Criar um Banco de dados Baseado na metodologia SCRUM', 
 3),
('Plataforma E-commerce', 
 'Plataforma para vendas online', 
 '2024-11-01', 
 '2025-02-28', 
 'Facilitar vendas online', 
 'Criar uma plataforma de vendas incluindo integração com gateways de pagamento', 
 2);

-- Insere sprints na tabela `sprints`, com nomes, datas de início e término, e status associados.
INSERT INTO sprints (nome_sprints, data_inicio_sprint, data_termino_sprint, status_sprint_id) 
VALUES 
('Sprint 1', '2024-11-01', '2024-11-15', 2),
('Sprint 2', '2024-11-16', '2024-11-30', 2),
('Sprint 3', '2024-12-01', '2024-12-15', 2),
('Sprint 4', '2024-12-16', '2024-12-25', 1);

-- Relaciona sprints a projetos na tabela `projeto_sprint`.
INSERT INTO projeto_sprint (projeto_id, sprints_id) 
VALUES 
(1, 1), 
(1, 2),
(2, 3),
(2, 4);

-- Adiciona membros a projetos, vinculando funcionários, projetos e funções na tabela `membros`.
INSERT INTO membros (projeto_id, funcionario_id, funcao_id) 
VALUES 
(1, 1, 1), 
(1, 2, 2), 
(1, 3, 3),
(1, 8, 3),
(2, 10, 1),
(2, 9, 2),
(2, 8, 3),
(2, 7, 3);

-- Insere tarefas na tabela `tasks`, com detalhes como nome, descrição, tempo estimado, tempo gasto e referências a outras tabelas.
INSERT INTO tasks (nome_task, descricao_task, tamanho, tempo_estimado_task, tempo_gasto, situacao_task_id, funcionario_id) 
VALUES 
('Criação do DER', 'Criar um Diagrama Entidade-Relacionamento', 5, 16, 10, 3, 8),
('Criar tabelas', 'Criar as tabelas em  SQL', 3, 8, 4, 3, 3),
('Inserts', 'inserir dados nas tabelas', 4, 8, 6, 3, 8),
('Documentação', 'Documentar todo o sistema', 2, 6, 6, 3, 3),
('Implementação do carrinho de compras', 'Desenvolver e integrar a funcionalidade de carrinho de compras', 2, 6, 4, 3, 8),
('Integração com gateway de pagamento', 'Desenvolver e implementar integração com o serviço de pagamento', 5, 8, 10, 3, 7),
('Configuração de envio de e-mails', 'Implementar envio automático de e-mails para confirmações de pedidos e notificações', 2, 6, 3, 2, 8),
('Desenvolvimento de filtros de busca', 'Desenvolver filtros de busca para facilitar a navegação dos produtos no e-commerce', 3, 8, 4, 2, 7);

-- Relaciona tarefas à tabela `relacionadoA` para marcar relações entre atividades.
INSERT INTO relacionadoA (nome_task) 
VALUES 
('Inserts'), 
('Implementação do carrinho de compras');

-- Relaciona tarefas a sprints e status geral.
INSERT INTO task_sprint (sprints_id, task_id, status_geral_id) 
VALUES 
(1, 1, 5), 
(1, 2, 5), 
(2, 3, 5),
(2, 4, 5),
(3, 5, 5),
(3, 6, 5),
(4, 7, 2),
(4, 8, 2);

-- Insere relações entre tarefas, situação e outros detalhes na tabela `relacao_task`.
INSERT INTO relacao_task (task_id, situacao_tasks_id, relacionadoA_id, descricao, funcionario_id) 
VALUES 
(1, 3, NULL, NULL, NULL),
(2, 3, NULL, NULL, NULL),
(3, 3, NULL, NULL, NULL),
(4, 3, 1, 'Desenvolver uma documentação com os Inserts utilizados', 8), 
(5, 3, NULL, NULL, NULL),
(6, 3, 2, 'O gateway de pagamento precisa dos dados do carrinho para processar o pagamento corretamente', 7),
(7, 2, NULL, NULL, NULL),
(8, 2, NULL, NULL, NULL);
