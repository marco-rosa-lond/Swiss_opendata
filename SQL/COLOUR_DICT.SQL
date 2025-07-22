create table Colour
(
    COLOR_DE nvarchar(100) not null
        constraint Colour_pk
            primary key,
    EN       nvarchar(100),
    PT       nvarchar(100)
)
go

INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Beige', N'Beige', N'Bege');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Blau', N'Blue', N'Azul');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Braun', N'Brown', N'Castanho');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Bunt', N'Multicolored', N'Colorido');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Effektlack', N'Effect paint', N'Tinta com efeito');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Feldgrau (Nur für Militärfahrzeuge)', N'Field gray (only for military vehicles)', N'Cinza-campo (apenas para veículos militares)');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Fleckentarnung ( Nur für Militärfahrzeuge)', N'Camouflage (only for military vehicles)', N'Camuflagem manchada (apenas para veículos militares)');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Gelb', N'Yellow', N'Amarelo');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Grau', N'Gray', N'Cinzento');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Grün', N'Green', N'Verde');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Orange', N'Orange', N'Laranja');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Rot', N'Red', N'Encarnado');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Schwarz', N'Black', N'Preto');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'unbekannt', N'Unknown', null);
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Violett', N'Purple', N'Violeta');
INSERT INTO swiss_data_dicionarios.dbo.Colour (COLOR_DE, EN, PT) VALUES (N'Weiss', N'White', N'Branco');
