
create table Plate_Type
(
    Tipo      nvarchar(100),
    Categoria nvarchar(100),
    DE        nvarchar(100),
    PT        nvarchar(100),
    CODE      varchar(2)
)
go



INSERT INTO swiss_data_dicionarios.dbo.Plate_Type (Tipo, Categoria, DE, PT, CODE) VALUES (N'Diplomática ', N'consular', N'Dienstwagen von Konsularbeamten', N'Veículos oficiais de funcionários consulares', N'CC');
INSERT INTO swiss_data_dicionarios.dbo.Plate_Type (Tipo, Categoria, DE, PT, CODE) VALUES (N'Diplomática ', N'missão', N'Diplomatische Missionen', N'Missões diplomáticas', N'CD');
INSERT INTO swiss_data_dicionarios.dbo.Plate_Type (Tipo, Categoria, DE, PT, CODE) VALUES (N'Diplomática ', N'administrativo', N'Diplomatisches Verwaltungspersonal', N'Pessoal administrativo diplomático', N'AT');
INSERT INTO swiss_data_dicionarios.dbo.Plate_Type (Tipo, Categoria, DE, PT, CODE) VALUES (N'Temporária ', N'cantão', N'Kantonsbefristet', N'Temporário no cantão', N'K');
INSERT INTO swiss_data_dicionarios.dbo.Plate_Type (Tipo, Categoria, DE, PT, CODE) VALUES (N'Normal', N'', N'Normalschild', N'Placa normal', N'N');
INSERT INTO swiss_data_dicionarios.dbo.Plate_Type (Tipo, Categoria, DE, PT, CODE) VALUES (N'Temporária ', N'alfândega', N'Zollbefristet', N'Temporário na alfândega', N'Z');
