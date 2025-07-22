create table Gearbox
(
    DE   nvarchar(50),
    PT   nvarchar(50),
    Tipo nvarchar(50),
    CODE char not null
        constraint Gearbox_pk
            primary key
)
go

INSERT INTO swiss_data_dicionarios.dbo.Gearbox (DE, PT, Tipo, CODE) VALUES (N'Automat', N'Automático', N'Automática', N'A');
INSERT INTO swiss_data_dicionarios.dbo.Gearbox (DE, PT, Tipo, CODE) VALUES (N'Hydrostat', N'Hidrostático', null, N'H');
INSERT INTO swiss_data_dicionarios.dbo.Gearbox (DE, PT, Tipo, CODE) VALUES (N'Mechanisch', N'Mecânico', N'Manual', N'M');
INSERT INTO swiss_data_dicionarios.dbo.Gearbox (DE, PT, Tipo, CODE) VALUES (N'Stufenlos', N'CVT', N'Automática', N'S');
