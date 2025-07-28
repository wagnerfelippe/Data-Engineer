CREATE OR REPLACE TABLE `prep_dashboards_develop.tmp_vendas` AS (
select  gv.contact_name,
        gv.agencyid_accountid,
        gv.agency_name_recipe,
        gv.agency_name_account,
        gv.id360,
        gv.contactid_uniqueid,
        gv.contact_name,
        gv.effective_date as data_ref_venda,
        gv.recipe_advertiser_name,
        gv.platform,
        gv.product,
        gv.master_channel,
        gv.display_channel,
        gv.program_name,
        gv.program_genre,
        gv.sale_type 
from `prep_dashboards_develop.tb_contatos_gestao_vendas_20250327` as gv
);