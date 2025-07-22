create table Plate_colors
(
    CODE   char not null
        constraint Plate_colors_pk
            primary key,
    DE     nvarchar(100),
    COR_PT nvarchar(200)
)
go

INSERT INTO swiss_data_dicionarios.dbo.Plate_colors (CODE, DE, COR_PT) VALUES (N'0', N'Weiss (Motorwagen)', N'Branco ');
INSERT INTO swiss_data_dicionarios.dbo.Plate_colors (CODE, DE, COR_PT) VALUES (N'5', N'Braun, Ausnahmefahrzeug', N'Castanho, veículo especial');
INSERT INTO swiss_data_dicionarios.dbo.Plate_colors (CODE, DE, COR_PT) VALUES (N'6', N'Schwarz, Armeefahrzeug', N'Preto, veículo militar');
