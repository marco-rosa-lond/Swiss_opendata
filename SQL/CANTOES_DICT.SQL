
create table CANTOES
(
    Code        varchar(2),
    Italiano    varchar(200),
    Deutsch     varchar(200),
    Français    varchar(200),
    Portuguese  varchar(200),
    [Cantão CH] bit
)
go

INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'A', N'Amministrazione', N'Administration', N'Administration', N'Administração', 0);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'AG', N'Argovia', N'Aargau', N'Argovie', N'Argóvia', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'AI', N'Appenzello interno', N'Appenzell-Innerrhoden', N'Appenzell, Rhodes-Intérieures', N'Appenzell Interior', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'AR', N'Appenzello esterno', N'Appenzell-Ausserrhoden', N'Appenzell, Rhodes-Extérieures', N'Appenzell Exterior', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'AS', N'Ufficio federale delle strade', N'Bundesamt für Strassen', N'Office fédéral des routes', N'Administração das Estradas', 0);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'BE', N'Berna', N'Bern', N'Berne', N'Berna', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'BL', N'Basilea Campagna', N'Basel-Landschaft', N'Bâle-Campagne', N'Basileia-Campo', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'BS', N'Basilea Città', N'Basel-Stadt', N'Bâle-Ville', N'Basileia-Cidade', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'BU', null, N'Büsingen', null, N'Büsingen (Germany)', 0);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'FL', N'Principato del Liechtenstein', N'Fürstentum Liechtenstein', N'Principauté de Liechtenstein', N'Principado do Liechtenstein', 0);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'FR', N'Friburgo', N'Freiburg', N'Fribourg', N'Friburgo', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'GE', N'Ginevra', N'Genf', N'Genève', N'Genebra', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'GL', N'Glarona', N'Glarus', N'Glaris', N'Glarus', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'GR', N'Grigioni', N'Graubünden', N'Grisons', N'Grisões', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'JU', N'Giura', N'Jura', N'Jura', N'Jura', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'LU', N'Lucerna', N'Luzern', N'Lucerne', N'Lucerna', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'M', N'Forze armate svizzere', N'Militär', N'Militaire', N'Forças Armadas Suíças', 0);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'NE', N'Neuchâtel', N'Neuenburg', N'Neuchâtel', N'Neuchâtel', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'NW', N'Nidvaldo', N'Nidwalden', N'Nidwald', N'Nidwalden', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'OW', N'Obvaldo', N'Obwalden', N'Obwald', N'Obwalden', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'P', N'Posta', N'Post', N'Poste', N'Correios', 0);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'RP', N'RIPOL', N'RIPOL', N'RIPOL', N'RIPOL (Swiss national police information system)', 0);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'SG', N'San Gallo', N'St. Gallen', N'Saint-Gall', N'São Galo', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'SH', N'Sciaffusa', N'Schaffhausen', N'Schaffhouse', N'Schaffhausen', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'SO', N'Soletta', N'Solothurn', N'Soleure', N'Soleura', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'SZ', N'Svitto', N'Schwyz', N'Schwyz', N'Schwyz', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'TG', N'Turgovia', N'Thurgau', N'Thurgovie', N'Turgóvia', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'TI', N'Ticino', N'Tessin', N'Tessin', N'Tessino', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'UR', N'Uri', N'Uri', N'Uri', N'Uri', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'VD', N'Vaud', N'Waadt', N'Vaud', N'Vaud', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'VS', N'Vallese', N'Wallis', N'Valais', N'Valais', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'ZG', N'Zugo', N'Zug', N'Zoug', N'Zug', 1);
INSERT INTO swiss_data_dicionarios.dbo.CANTOES (Code, Italiano, Deutsch, Français, Portuguese, [Cantão CH]) VALUES (N'ZH', N'Zurigo', N'Zürich', N'Zurich', N'Zurique', 1);
