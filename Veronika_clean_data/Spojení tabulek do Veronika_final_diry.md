SELECT 
    CAST(rok AS nvarchar(MAX))                    AS Rok,
    N'Sudoměřice'                                 AS Díra,
    CAST([true] AS nvarchar(MAX))                 AS Pravda,
    CAST(teplota AS decimal(10,2))                AS Teplota,
    CAST(dest    AS decimal(10,2))                AS Déšť,
    CAST(snih    AS decimal(10,2))                AS Sníh
INTO dbo.Veronika_final_diry
FROM dbo.Veronika_sudomerice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Kostice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_kostice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Lelekovice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_lelekovice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Předklášteří',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_predklasteri

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Prštice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_prstice

UNION ALL
SELECT 
    CAST(rok AS nvarchar(MAX)),
    N'Rebešovice',
    CAST([true] AS nvarchar(MAX)),
    CAST(teplota AS decimal(10,2)),
    CAST(dest    AS decimal(10,2)),
    CAST(snih    AS decimal(10,2))
FROM dbo.Veronika_rebesovice
;