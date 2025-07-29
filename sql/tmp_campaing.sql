CREATE OR REPLACE TABLE `prep_dashboards_develop.tmp_campaing` AS 
(  
SELECT
-- Colunas da Tabela de Campanhas (tb_campaign)
c.id AS campaign_id,
c.name AS campaign_name,
c.status AS campaign_status,
c.type AS campaign_type,
c.canal__c AS campaign_canal,
c.startdate AS campaign_startdate,
c.enddate AS campaign_enddate,
c.amountwonopportunities,
c.numberofopportunities,
c.dt_partition AS campaign_dt_partition,

-- Colunas da Tabela de Membros (tb_campaignmember)
cm.id AS member_id,
cm.contactid,
cm.status AS member_status, -- Status real do membro (ex: 'Enviado')
cm.dt_partition AS member_dt_partition

-- Coluna da Tabela de Status (tb_campaignmemberstatus)
-- cms.label AS member_status_label -- O nome legível do status (será o mesmo que cm.status)

FROM
`prep_dashboards_develop.tb_campaign` AS c
LEFT JOIN
`prep_dashboards_develop.tb_campaignmember` AS cm
ON c.id = cm.campaignid
LEFT JOIN
`prep_dashboards_develop.tb_campaignmemberstatus` AS cms
-- --- CORREÇÃO FUNDAMENTAL AQUI ---
-- 1. Juntamos o status do membro (que é um texto) com o label da tabela de status.
ON cm.status = cms.label
-- 2. E garantimos que ambos pertencem à mesma campanha para evitar erros.
AND cm.campaignid = cms.campaignid

);