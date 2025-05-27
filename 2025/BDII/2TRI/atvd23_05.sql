-- 1) Mostre os 10 clientes com o maior valor total de vendas.
SELECT cliente.nome, SUM(venda.valorliquido) AS totalVendas
FROM venda
JOIN cliente ON cliente.idcliente = venda.idcliente
GROUP BY cliente.idcliente
ORDER BY totalVendas DESC
LIMIT 10;

 -- 2) Mostre a quantidade de vendas de cada cliente.
 SELECT cliente.nome, COUNT(venda.idvenda) as totalVendas -- garante que conte até as vendas = NULL
 from venda
 JOIN cliente ON cliente.idcliente = venda.idcliente
 GROUP BY cliente.idcliente
 ORDER BY totalVendas DESC;

 -- 3) Mostre os 5 clientes que menos compraram.
 SELECT cliente.nome, COUNT(venda.idvenda) as menosCompraram
 FROM venda
 JOIN cliente ON cliente.idcliente = venda.idcliente
 GROUP BY cliente.idcliente 
 ORDER BY menosCompraram ASC
 LIMIT 5;

 -- 4) Mostre os clientes que não possuem vendas.
SELECT cliente.nome, venda.idvenda
FROM cliente
LEFT JOIN venda ON cliente.idcliente = venda.idcliente -- inclui todos até os que não possuem vendas. diferente do (INNER) JOIN
WHERE venda.idvenda IS NULL;

-- 5) Mostre o nome, a quantidade e o total de venda de cada vendedor.
SELECT funcionario.nomefuncionario, 
	SUM(venda.valorliquido) AS valorTotalVendas, 
	COUNT(venda.idvenda) AS totalVendas
FROM venda
JOIN funcionario ON funcionario.idfuncionario = venda.idfuncionario
GROUP BY funcionario.idfuncionario, funcionario.nomefuncionario
ORDER BY totalVendas DESC, valorTotalVendas DESC; -- tem que adicionar DESC em ambos para sair bonitinho e não só em um
