CREATE OR REPLACE TABLE `prep_dashboards_develop.tmp_contatos` AS (
select   q.score__c,
            q.GeneroDeProgramacao__C,
            q.Segmenta_o_do_Contato__c,
            q.Segmento__c,
            q.CanaisDePreferencia__c,
            q.TimeFutebol__c,
            q.Area__c,
            q.Department,
            q.Id_Account,
            q.Tipo_de_Conta__c,
            q.CategoriaConta__c,
            q.Status_de_Relacionamento__c,
            q.Email_contato,
            q.CPF,
            q.Phone,
            q.MobilePhone,
            q.unique_id, 
            q.Dt_Partition as data_ref_contato 
from `prep_dashboards_develop.Qualificacao_contatos_account` as q
);