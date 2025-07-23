create table fuel
(
    Code                 char not null
        constraint fuel_pk
            primary key,
    IT                   nvarchar(max),
    DE                   nvarchar(max),
    FR                   nvarchar(max),
    EN                   nvarchar(max),
    PT                   nvarchar(150),
    TipoMotorizacao      nvarchar(200),
    CombustivelPrincipal nvarchar(100),
    Combustivel2         varchar(200)
)
go

INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'B', N'Benzina', N'Benzin', N'Essence', N'Gasoline', N'Gasolina', N'Combustão', N'Gasolina', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'C', N'Benzina / elettrico', N'Benzin / Elektrisch', N'Essenze / électrique', N'Gasoline / electric', N'Gasolina / Elétrico', N'Híbrido', N'Gasolina', N'Electricidade');
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'D', N'Diesel', N'Diesel', N'Diesel', N'Diesel', N'Diesel', N'Combustão', N'Diesel', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'E', N'Elettrico', N'Elektrisch', N'Electrique', N'Electric', N'Elétrico', N'Eléctrico Puro', N'Electricidade', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'F', N'Diesel / elettrico', N'Diesel / Elektrisch', N'Diesel / électrique', N'Diesel / electric', N'Diesel / Elétrico', N'Híbrido', N'Diesel', N'Electricidade');
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'G', N'Gaz (CNG/GPL)', N'Gas (CNG/GPL)', N'Gaz (CNG/GPL)', N'Gaz (CNG/LPG)', N'Gás (GNC/GPL)', N'Combustão', N'GNC/GPL', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'J', N'Alcohol (ethanol)', N'Alkohol (Ethanol)', N'alcool (éthanol)', N'Alcohol (ethanol)', N'Álcool (etanol)', N'Combustão', N'Ethanol (E95)', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'K', N'Benzina / alcohol (ethanol)', N'Benzin / Alkohol (Ethanol)', N'Essence / alcool (éthanol)', N'Gasoline / alcohol (ethanol)', N'Gasolina / Álcool (etanol)', N'Combustão', N'Gasolina', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'L', N'Gas di petrolio liquefatti (LPG)', N'Flüssiggas (LPG)', N'Gaz de pétrole liquéfié (LPG)', N'Liquefied petroleum gas (LPG)', N'Gás liquefeito (GPL)', N'Combustão', N'GPL', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'M', N'Metanolo', N'Methanol', N'Méthanol', N'Methanol', N'Metanol', N'Combustão', N'Metanol', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'N', N'Gas naturale (CNG)', N'Erdgas (CNG)', N'Gaz naturel (CNG)', N'Natural gas (CNG)', N'Gás natural (GNC)', N'Combustão', N'GNC', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'P', N'Petrolio', N'Petrol', N'Pétrole', N'Petroleum', N'Gasolina', N'Combustão', N'Gasolina', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'R', N'Elettrico con RE (Range Extender)', N'Elektrisch mit RE (Range Extender)', N'Electrique avec RE (Range Extender)', N'Electric with RE (Range Extender)', N'Elétrico com RE (Range Extender)', N'Eléctrico (REX)', N'Electricidade', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'U', N'altri carburanti', N'übrige Treibstoffe', N'autres carburants', N'Other fuels', N'Outros combustíveis', null, null, null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'W', N'Idrogeno', N'Wasserstoff', N'Hydrogène', N'Hydrogen', N'Hidrogénio', N'Combustão', N'Hidrogénio', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'X', N'Idrogeno / elettrico', N'Wasserstoff / Elektrisch', N'Hydrogène / électrique', N'Hydrogen / electric', N'Hidrogénio / Elétrico', N'Eléctrico (Fuel Cell)', N'Electricidade', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'Y', N'Gas naturale (CNG) / benzina', N'Erdgas (CNG) / Benzin', N'Gaz naturel (CNG) / essence', N'Natural gas (CNG) / gasoline', N'Gás natural (GNC) / Gasolina', N'Combustão', N'GNC', null);
INSERT INTO fuel (Code, IT, DE, FR, EN, PT, TipoMotorizacao, CombustivelPrincipal, Combustivel2) VALUES (N'Z', N'Gas di petrolio liquefatti (LPG) / benzina', N'Flüssiggas (LPG) / Benzin', N'Gaz de pétrole liquéfié (LPG) / essence', N'Liquefied petroleum gas (LPG) / gasoline', N'Gás liquefeito (GPL) / Gasolina', N'Combustão', N'GPL', null);
