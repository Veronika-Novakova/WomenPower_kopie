-- vytvoření cílové tabulky jednou
SELECT 
    CAST(rok AS nvarchar(MAX))                    AS Rok,
    N'Vyškov'                                     AS Město,
    CAST([true] AS nvarchar(MAX))                 AS Pravda,
    CAST(teplota AS decimal(10,2))                AS Teplota,
    CAST(dest    AS decimal(10,2))                AS Déšť,
    CAST(snih    AS decimal(10,2))                AS Sníh
INTO dbo.Veronika_final_mesta
FROM dbo.Veronika_Vyskov

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Hodonín',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_Hodonin

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Blansko',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_Blansko

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Břeclav',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_Breclav

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Ivančice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_Ivancice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Znojmo',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_Znojmo
;

