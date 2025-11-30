SELECT 
    CAST(rok AS nvarchar(MAX))                    AS Rok,
    N'Blansko'                                    AS Město,
    CAST([true] AS nvarchar(MAX))                 AS Pravda,
    CAST(teplota_11_25 AS decimal(10,2))          AS Teplota_11_25,
    CAST(dest_11_25    AS decimal(10,2))          AS Déšť_11_25,
    CAST(snih_11_25    AS decimal(10,2))          AS Sníh_11_25,
    CAST(teplota_12_24 AS decimal(10,2))          AS Teplota_12_24,
    CAST(dest_12_24    AS decimal(10,2))          AS Déšť_12_24,
    CAST(snih_12_24    AS decimal(10,2))          AS Sníh_12_24
INTO dbo.Katerina_final_mesta
FROM dbo.katerina_blanko

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Břeclav',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_breclav

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Ivančice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_ivancice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Vyškov',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_vyskov

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Znojmo',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_znojmo

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Hodoním',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_hodonin
;

select * from dbo.Katerina_final_mesta order by Rok ASC




