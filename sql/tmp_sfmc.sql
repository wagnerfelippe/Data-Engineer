CREATE OR REPLACE TABLE `prep_dashboards_develop.tmp_sfmc` AS 
(  
SELECT
          Email,
          NULL AS jobid,
          domain,
          NULL AS emailname,
          CAST(PARSE_DATETIME('%m/%d/%Y %I:%M:%S %p', datejoined) AS DATE) AS eventdate, -- Usando a data de inscrição como data do evento
          dt_partition,
          status,
          dateunsubscribed,
          datejoined,
          NULL AS bouncecategory,
          NULL AS bouncesubcategory,
          NULL AS bouncetype,
          NULL AS smtpbouncereason,
          NULL AS linkname,
          NULL AS linkcontent,
          'subs' AS source_table
        FROM
          `prep_dashboards_develop.subscribers_mkt_cloud`

        UNION ALL

        -- Tabela 2: sent_mkt_cloud
        SELECT
          Email,
          CAST(jobid AS STRING) AS jobid,
          domain,
          emailname,
          CAST(PARSE_DATETIME('%m/%d/%Y %I:%M:%S %p', eventdate) AS DATE) as eventdate,
          dt_partition,
          NULL AS status,
          NULL AS dateunsubscribed,
          NULL AS datejoined,
          NULL AS bouncecategory,
          NULL AS bouncesubcategory,
          NULL AS bouncetype,
          NULL AS smtpbouncereason,
          NULL AS linkname,
          NULL AS linkcontent,
          'sent' AS source_table
        FROM
          `prep_dashboards_develop.sent_mkt_cloud`

        UNION ALL

        -- Tabela 3: open_mkt_cloud
        SELECT
          Email,
          CAST(jobid AS STRING) AS jobid,
          domain,
          emailname,
          CAST(PARSE_DATETIME('%m/%d/%Y %I:%M:%S %p', eventdate) AS DATE) as eventdate,
          dt_partition,
          NULL AS status,
          NULL AS dateunsubscribed,
          NULL AS datejoined,
          NULL AS bouncecategory,
          NULL AS bouncesubcategory,
          NULL AS bouncetype,
          NULL AS smtpbouncereason,
          NULL AS linkname,
          NULL AS linkcontent,
          'open' AS source_table
        FROM
          `prep_dashboards_develop.open_mkt_cloud`

        UNION ALL

        -- Tabela 4: bounce_mkt_cloud
        SELECT
          Email,
          CAST(jobid AS STRING) AS jobid,
          domain,
          NULL AS emailname,
          CAST(PARSE_DATETIME('%m/%d/%Y %I:%M:%S %p', eventdate) AS DATE) as eventdate,
          dt_partition,
          NULL AS status,
          NULL AS dateunsubscribed,
          NULL AS datejoined,
          bouncecategory,
          bouncesubcategory,
          bouncetype,
          smtpbouncereason,
          NULL AS linkname,
          NULL AS linkcontent,
          'bounce' AS source_table
        FROM
          `prep_dashboards_develop.bounce_mkt_cloud`

        UNION ALL

        -- Tabela 5: click_mkt_cloud
        SELECT
          Email,
          CAST(jobid AS STRING) AS jobid,
          domain,
          emailname,
          CAST(PARSE_DATETIME('%m/%d/%Y %I:%M:%S %p', eventdate) AS DATE) as eventdate,
          dt_partition,
          NULL AS status,
          NULL AS dateunsubscribed,
          NULL AS datejoined,
          NULL AS bouncecategory,
          NULL AS bouncesubcategory,
          NULL AS bouncetype,
          NULL AS smtpbouncereason,
          linkname,
          linkcontent,
          'click' AS source_table
        FROM
          `prep_dashboards_develop.click_mkt_cloud`
);