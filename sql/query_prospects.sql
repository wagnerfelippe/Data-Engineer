select * from `enext-general.dca.sfmc_de_geral_audiencias`
where de_origem NOT LIKE '%full%'
AND FORMAT_TIMESTAMP("%Y-%m-%d", data) = "2025-05-31"
AND FORMAT_TIMESTAMP("%Y-%m-%d", data_primeira_compra) between "2025-05-01" and "2025-05-31"
and de_origem not like "%espelho%"
and de_origem like "%_eng%"
and de_origem like "%_acne%"
