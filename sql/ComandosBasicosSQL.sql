-- SQL 2ª DO MÓDULO 04

select e.empid, e.firstname, e.lastname, e.country, e.region, e.city 
from HR.Employees as e
where region <> N'WA' --OR region is null;



-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-- Aqui estamos essa query para a quarta aula ----

use DataEngineer
go

/*
Um select buscando alguns campos de uma determinada tabela onde o meu lastname
contenha a última letra e (Lembrando que em outros banco são case sensitive)
*/

select d.empid, d.firstname, d.lastname
from HR.Employees as d
where d.lastname like N'%e'


select d.empid, d.firstname, d.lastname
from HR.Employees as d
where d.lastname like N'D___e'; /*Palavra que começam com D, que contenham 3 caracteres e terminar com a letra e */



with Contato as(
	select Email from ( values ('CONTATO@EMAIL.COM.BR'), ('CONTATO_SUPORTE@EMAIL.COM.BR')
	) as Tabela(Email)
)
select Email
from Contato
where Email like '%\_%' ESCAPE '\' -- Uma pesquisa para trazer somente e-mails que tenham underscore. 
                                   -- Se eu deixar do mesmo jeito que está em cima, ele vai 
								   -- contar os caracteres. Aqui neste caso precisamos 
								   -- definir um escape de qual caracter para ele funcionar.

-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------


-- Olhem na documentação para Datatime2 ou Datatime

select o.orderid, o.orderdate, o.empid, o.custid
from Sales.Orders as o
where o.orderdate = '20140708'

select @@LANGID, @@LANGUAGE -- Pegar a data e sua linguagem
select * from sys.syslanguages -- entender a linguagem do banco de dados


---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------



use DataEngineer
go
/*
select d.empid, d.firstname, d.lastname, d.city, MONTH(d.birthdate) as birthmonth 
from HR.Employees as d
where d.country = N'USA' and d.region = N'WA'
order by d.city, d.empid*/

/* utilizando o TOP para trazer as 3 primeiras linhas na consulta */
select top (3) orderid, orderdate, custid, empid
from DataEngineer.Sales.Orders
order by orderdate desc

/** A função PERCENT é trazendo 1% da minha base total */
select top (1) percent orderid, orderdate, custid, empid
from DataEngineer.Sales.Orders
order by orderdate desc

/** Estamos declarando uma varivel que recebe o nome e essa variável entra no select **/
declare @n as BIGINT = 5;
select top (@n) orderid, orderdate, custid, empid
from DataEngineer.Sales.Orders
order by orderdate desc


/** Vai trazer com o with ties vai puxar os top3 porém com resultados iguais com a ordenação de orderdate**/
select top (3) with ties orderid, orderdate, custid, empid
from DataEngineer.Sales.Orders
order by orderdate desc, orderid desc

/** Aqui eu consigo travar a consulta definindo o orderdate e oderid sempre trazendo os top 3 **/
select top (3) orderid, orderdate, custid, empid
from DataEngineer.Sales.Orders
order by orderdate desc, orderid desc


--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------

/**
Função Row number para inserir um campo onde eu trago o número da linha
OFFSET 50 ROWS ele vai pular as primeiras 50 linhas e vai continuar com todo o resto delas
OFFSET 50 ROWS FETCH NEXT 25 ROWS ONLY e aqui ele pula as primeiras 50 linhas e vai me trazer as próximas 25 linhas. (51 até 75)
**/
select orderid, orderdate, custid, empid, ROW_NUMBER() OVER (ORDER BY orderdate DESC, orderid DESC) as rownumber
from DataEngineer.Sales.Orders
order by orderdate desc, orderid desc
OFFSET 50 ROWS FETCH NEXT 25 ROWS ONLY



/**
Função Row number para inserir um campo onde eu trago o número da linha
OFFSET 0 ROW ele não vai pular nenhuma linha
FETCH FIRST 3 ROWS ONLY só vai trazer as primeiras 3 linhas

OBS: Não necessáriamente precisa do ROW NUMBER para utilizar o OFFSET com FETCH

**/
select orderid, orderdate, custid, empid, ROW_NUMBER() OVER (ORDER BY orderdate DESC, orderid DESC) as rownumber
from DataEngineer.Sales.Orders
order by orderdate desc, orderid desc
OFFSET 0 ROW FETCH FIRST 3 ROWS ONLY


/**
DECLARE - declaração das variáveis para usar como parâmetro dentro do OFFSET + FETCH 
Função Row number para inserir um campo onde eu trago o número da linha
Vai trazer as primeiras 25 linhas

**/

DECLARE @pagesize AS BIGINT = 25, @pagenum AS BIGINT = 1;
SELECT orderid, orderdate, custid, empid, ROW_NUMBER() OVER (ORDER BY orderdate DESC, orderid DESC) as rownumber
FROM  DataEngineer.Sales.Orders
order by orderdate desc, orderid desc
OFFSET (@pagenum - 1) * @pagesize ROWS FETCH NEXT @pagesize ROWS ONLY;






