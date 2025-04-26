-- 1) Inclua na tabela cidade um novo campo chamado UF. Exempo dos valores que serão gravados nesse campo: 'SP', 'PR', 'SC'.
alter table cidade
add column UF varchar(2);

select * from cidade;

-- 2) Inclua na tabela cliente um novo campo chamado email onde será gravado um email que o cliente possuir.
alter table cliente
add column email varchar(50);

select * from cliente;

-- 3) Inclua na tabela funcionario um campo chamado nrdependentes, esse campo será usado para informar quantos dependentes 
-- o funcionário possui, esse campo não pode conter valores nulos e o valor padrão deve ser 0.

select * from funcionario;

alter table funcionario
add column nrdependentes int not null default 0;

select * from funcionario;

-- 4) Faça a correção do sequencial de todas as tabelas(vide final da apostila postada no moodle).
-- BAIRRO
SELECT pg_get_serial_sequence('bairro', 'idbairro');
SELECT setval('public.bairro_idbairro_seq', (SELECT MAX(idbairro) FROM bairro), true);
select * from bairro;
INSERT INTO public.bairro(nomebairro)
VALUES ('SANTOS DUMONT');
select * from public.bairro_idbairro_seq;
-- CIDADE
select * from cidade;
SELECT pg_get_serial_sequence('cidade', 'idcidade');
SELECT setval('public.cidade_idcidade_seq', (SELECT MAX(idcidade) FROM cidade), true);
INSERT INTO public.cidade(nomecidade)
VALUES ('GUARULHOS');
select * from public.cidade_idcidade_seq;
-- FUNCIONARIO
INSERT INTO public.cliente(nome) 
VALUES ('GUSTAVO RANDI');

SELECT pg_get_serial_sequence('cliente', 'idcliente');
select setval('public.cliente_idcliente_seq', (select max(idcliente) from cliente), true);
select * from public.cliente_idcliente_seq;
-- FUNCIONARIO
INSERT INTO public.funcionario(nomefuncionario) VALUES ('CATARINA');
SELECT pg_get_serial_sequence('funcionario', 'idfuncionario');
select setval('public.funcionario_idfuncionario_seq', (select max(idfuncionario) from funcionario), true);
select * from public.funcionario_idfuncionario_seq;
-- PRODUTO
INSERT INTO public.produto(descricao)
VALUES 
('MELANCIA');

SELECT pg_get_serial_sequence('produto', 'idproduto');

select setval('public.produto_idproduto_seq', (select max(idproduto) from produto), true);

select * from public.produto_idproduto_seq;

-- VENDA

INSERT INTO public.venda(idcliente, idfuncionario, datavenda, valorbruto, desconto, acrescimo, valorliquido, parcelas) VALUES 
(27, 3, '2025-08-29', 0.00, 0.00, 0.00, 0.00, 6);

select pg_get_serial_sequence('venda', 'idvenda');

select setval('public.venda_idvenda_seq', (select max(idvenda) from venda), true);

select * from public.venda_idvenda_seq;

-- VENDA ITEM
INSERT INTO public.vendaitem(idvenda, idproduto, quantidade, valorunitario, valortotal)  VALUES 
(1, 29, 38, 3.29, 1342.02); 

select pg_get_serial_sequence('vendaitem', 'idvendaitem');
select setval('public.vendaitem_idvendaitem_seq', (select max(idvendaitem) from vendaitem), true);

select * from public.vendaitem_idvendaitem_seq;