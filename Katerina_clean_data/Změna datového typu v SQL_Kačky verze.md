ALTER TABLE dbo.katerina_hodonin ALTER COLUMN teplota_11_25 DECIMAL(10,2) NULL;
ALTER TABLE dbo.katerina_hodonin ALTER COLUMN dest_11_25    DECIMAL(10,2) NULL;
ALTER TABLE dbo.katerina_hodonin ALTER COLUMN snih_11_25    DECIMAL(10,2) NULL;
ALTER TABLE dbo.katerina_hodonin ALTER COLUMN teplota_12_24 DECIMAL(10,2) NULL;
ALTER TABLE dbo.katerina_hodonin ALTER COLUMN dest_12_24    DECIMAL(10,2) NULL;
ALTER TABLE dbo.katerina_hodonin ALTER COLUMN snih_12_24    DECIMAL(10,2) NULL;

select * from dbo.katerina_hodonin
