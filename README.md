Projekt pranostiky CZECHITAS 2025

Veronika pořekadlo: Svatá Veronika seká ledy z rybníka. -když bude průměrná denní teplota víc než 0 stupňů celsia tak pranostika platí.
Kateřina pořekadlo: Kateřina na blátě, Vánoce na ledě. - Když bude 25.11 průměrná denní teplota nad 0 stupňů celsia a srážky budou v součtu aspoň 10mm a 24.12 bude průměrná teplota pod 0 stupňů Celsia tak pranostika platí.
Domi pořekadlo: Keď sa potí Dominik, Marek bude v kožuchu. 
		-aktuální počet pořekadel v týmu celkem : 3
15.11.2025 HACKHATON 2 Jsme vybrali nové pořekadlo: Svatá Tonička mívá často uplakaná očička.
		[12. červen - sv.Antonie] s podmínkou že když bude déšť více než 0 mm, tak pranostika platí.


Co zkoumáme? 
Jestli jsou pořekadla v ČR a na Slovensku pravdivá/aktuální dnes v porovnání s minulostí v jednotlivých městech na Jižní moravě. Zkoumáme  50 let. A jestli pravdivost pořekadel ovlivnilo globální oteplování.
Hlavní hypotéza: Jak často se pranostiky vyplní v rámci 5(nebo 10) letých období a jak/zda tento trend koreluje s CO2 v atmosféře. Lze použít a spojit data z vícero měřících stanic pro více dat. 
Dílčí hypotézy: Platí v průměru méně/více/stejně v urbanizovaných oblastech než na menších vesnicích?

zdroje dat: https://open-meteo.com/en/docs/historical-weather-api (zdroj od Katky), https://gml.noaa.gov/ccgg/trends/gl_data.html (CO2)
		

GIT: https://github.com/DominiqueKiss/WomenPower - zde jsou kódy, výsledné tabulky s daty
Google disk: https://drive.google.com/drive/folders/1G-Ry583qr82gVinstg9QT2HB1_iSN6XD?usp=sharing - zde jsou vešerá vyčištěná data z open meteo pro díry a města

POSTUP:

1.stáhnout data z open meteo a CO2 ze zmíněného webu
2.pročistit data v Pythonu (pomocí kodu ze souboru Kod na čištění dat.py který je zde nahrán) a umazat prázdné řádky nahoře, projít data
-A dále použít specializovaný kod s kterým nám pomohl mentor, je zde nahrán:Kód_pranostika_06-12.ipynb
3.Nahrát soubory do azure pomocí import wizard (nvarchar(MAX) a Allow null zašrktnout, poté jsme to všechno spojili pomocí:Spojení tabulek do Veronika_final_diry.md a Spojení tabulek do Veronika_final_mesta.md, soubory jsou zde nahrány--měly by vyjít dvě finální tabulky. Poté jsme tyto dvě tabulky spojili
kodem z tohoto souboru: Spojení_tabulek_s_CO2.csv, který je zde nahrán.
4.Poté nahrát tyto dvě tabulky do PowerBI a změnit datové typy. Také změnit Pravdu na typ TRUE/FALSE. 
[5.Udělat správný datový model v Ludcidchart: https://lucid.app/lucidchart/0fda4100-22fe-41ae-a9b7-6962e53faf27/edit?viewport_loc=-702%2C-19%2C2301%2C1051%2C0_0&invitationId=inv_b0a62c2b-9ce7-43b0-ad29-dc6a7c981a7c]
6.Udělat krásnou vizualizaci v PowerBI
7.sepsání anotace a její odevzdání (Hotová anotace je na Discord skupině WomenPower a musí se odevzdat do 23.11.2025)
8.sepsání finálního příspěvku na blog a jeho odevzdání ( Termín odevzdání je 30.11.2025)
9.příprava na prezentaci projektu

-sepisujeme poznámky na blog medium, rozepíšeme je později.

ANOTACE:
Projekt se zaměřuje na analýzu platnosti vybraných meteorologických pranostik v průběhu posledních 50 let. Současně zkoumá vztah mezi mírou platnosti těchto pranostik a úrovní i změnou koncentrace CO₂ v atmosféře. Dále porovnává rozdíly v platnosti pranostik mezi velkými městy a venkovskými oblastmi Jihomoravského kraje. Projekt také sleduje dlouhodobé trendy teplot, srážek a sněhové pokrývky a jejich možné dopady na spolehlivost tradičních pranostik.
