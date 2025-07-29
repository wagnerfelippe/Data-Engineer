-- ===================================================================================
-- SCRIPT DE CRIAÇÃO DA TABELA DE DIMENSÃO CALENDÁRIO
-- ===================================================================================
-- Instrução para criar (ou substituir, se já existir) a tabela.
/* Nome: Wagner Felippe
   Data: 15/07/2025
   Descrição: Uma tabela calendário dinâmico para utilizar para filtragem e validação.

*/


CREATE OR REPLACE TABLE `prep_dashboards_develop.dim_calendario` AS

-- Usamos uma CTE (Common Table Expression) para gerar a lista de datas.
WITH date_range AS (
-- GENERATE_DATE_ARRAY cria um array de datas entre um início e um fim.
-- UNNEST transforma esse array em linhas.
SELECT calendar_date
FROM UNNEST(GENERATE_DATE_ARRAY('2020-01-01', CURRENT_DATE(), INTERVAL 1 DAY)) AS calendar_date
)

-- Selecionamos a data e extraímos vários atributos úteis dela.
SELECT
d.calendar_date AS data,
EXTRACT(YEAR FROM d.calendar_date) AS ano,
EXTRACT(MONTH FROM d.calendar_date) AS mes,
EXTRACT(DAY FROM d.calendar_date) AS dia,
EXTRACT(QUARTER FROM d.calendar_date) AS trimestre,
EXTRACT(WEEK FROM d.calendar_date) AS semana_do_ano,
EXTRACT(DAYOFWEEK FROM d.calendar_date) AS dia_da_semana_num, -- 1 (Domingo) a 7 (Sábado)
FORMAT_DATE('%Y-%m', d.calendar_date) AS ano_mes,
-- === ALTERAÇÃO PARA PORTUGUÊS: NOME DO MÊS ===
CASE EXTRACT(MONTH FROM d.calendar_date)
  WHEN 1 THEN 'Janeiro'
  WHEN 2 THEN 'Fevereiro'
  WHEN 3 THEN 'Março'
  WHEN 4 THEN 'Abril'
  WHEN 5 THEN 'Maio'
  WHEN 6 THEN 'Junho'
  WHEN 7 THEN 'Julho'
  WHEN 8 THEN 'Agosto'
  WHEN 9 THEN 'Setembro'
  WHEN 10 THEN 'Outubro'
  WHEN 11 THEN 'Novembro'
  WHEN 12 THEN 'Dezembro'
END AS nome_mes,

-- === ALTERAÇÃO PARA PORTUGUÊS: NOME DO DIA DA SEMANA ===
CASE EXTRACT(DAYOFWEEK FROM d.calendar_date)
  WHEN 1 THEN 'Domingo'
  WHEN 2 THEN 'Segunda-feira'
  WHEN 3 THEN 'Terça-feira'
  WHEN 4 THEN 'Quarta-feira'
  WHEN 5 THEN 'Quinta-feira'
  WHEN 6 THEN 'Sexta-feira'
  WHEN 7 THEN 'Sábado'
END AS nome_dia_da_semana,
CASE
  WHEN EXTRACT(DAYOFWEEK FROM d.calendar_date) IN (1, 7) THEN 'Fim de Semana'
  ELSE 'Dia de Semana'
END AS tipo_dia
FROM
date_range d
ORDER BY
data;