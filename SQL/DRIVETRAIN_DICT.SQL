create table Drivetrain
(
    DE         nvarchar(100),
    PT         nvarchar(100),
    Tracao     nvarchar(3),
    CODE       varchar not null
        constraint Drivetrain_pk
            primary key,
    TracaoTipo varchar(3)
)
go

INSERT INTO swiss_data_dicionarios.dbo.Drivetrain (DE, PT, Tracao, CODE, TracaoTipo) VALUES (N'Allrad', N'Tração integral', N'4X4', N'A', N'AWD');
INSERT INTO swiss_data_dicionarios.dbo.Drivetrain (DE, PT, Tracao, CODE, TracaoTipo) VALUES (N'Geländegängig', N'Todo-o-terreno', N'4X4', N'G', N'AWD');
INSERT INTO swiss_data_dicionarios.dbo.Drivetrain (DE, PT, Tracao, CODE, TracaoTipo) VALUES (N'Hinterrad', N'Tração traseira', N'4X2', N'H', N'RWD');
INSERT INTO swiss_data_dicionarios.dbo.Drivetrain (DE, PT, Tracao, CODE, TracaoTipo) VALUES (N'Raupenantrieb', N'Tração por lagartas', null, N'R', null);
INSERT INTO swiss_data_dicionarios.dbo.Drivetrain (DE, PT, Tracao, CODE, TracaoTipo) VALUES (N'Vorderrad', N'Tração dianteira', N'4X2', N'V', N'FWD');
