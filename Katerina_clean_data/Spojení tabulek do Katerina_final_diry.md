--Propojení všech tabulek do jedné (pozor na sloupce, které máme v originálních tabulkách - nutné doplnit)
SELECT 
    CAST(rok AS nvarchar(MAX))                    AS Rok,
    N'Kostice'                                    AS Díra,
    CAST([true] AS nvarchar(MAX))                 AS Pravda,
    CAST(teplota_11_25 AS decimal(10,2))          AS Teplota_11_25,
    CAST(dest_11_25    AS decimal(10,2))          AS Déšť_11_25,
    CAST(snih_11_25    AS decimal(10,2))          AS Sníh_11_25,
    CAST(teplota_12_24 AS decimal(10,2))          AS Teplota_12_24,
    CAST(dest_12_24    AS decimal(10,2))          AS Déšť_12_24,
    CAST(snih_12_24    AS decimal(10,2))          AS Sníh_12_24
INTO dbo.Katerina_final_diry                                    -- název finální tabulky ve formátu Jmeno_fina_diry/mesta
FROM dbo.katerina_kostice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Rebešovice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_rebesovice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Lelekovice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_lelekovice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Předklášteří',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_predklasteri

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Sudoměřice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_sudomerice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Prštice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota_11_25 AS decimal(10,2)),
    CAST(dest_11_25    AS decimal(10,2)),
    CAST(snih_11_25    AS decimal(10,2)),
    CAST(teplota_12_24 AS decimal(10,2)),
    CAST(dest_12_24    AS decimal(10,2)),
    CAST(snih_12_24    AS decimal(10,2))
FROM dbo.katerina_prstice
;

--Kontrola nahraných dat a talubky + seřazení podle roku (stejný dotaz lze použít i pro díry, je potřeba změnit v dotazu)
select * from dbo.Katerina_final_mesta order by Rok ASC

-- Přepis pravdivosti do češtiny
UPDATE dbo.Katerina_final_diry
SET Pravda = CASE 
    WHEN Pravda = 'True' THEN 'Platí'
    WHEN Pravda = 'False' THEN 'Neplatí'
END;
