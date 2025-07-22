
create table dbo.BodyTypes
(
    CODE char(3) not null
        constraint BodyTypes_pk
            primary key,
    DE   nvarchar(150),
    PT   nvarchar(100)
)
go

INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'000', N'---', null);
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'161', N'Stationswagen', N'Stationwagon');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'163', N'Limousine', N'Sedan');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'172', N'Offen mit Blache', N'Convertible / Open vehicle with cover');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'175', N'Offen', N'Convertible / Roadster');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'176', N'Offen mit Verdeck / Hardtop', N'Convertible / Roadster with soft top or removable hardtop');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'265', N'Einsatzfahrzeug', N'Special-purpose vehicle');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'308', N'Kabine', N'Single cab / Utility Vehicle');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'339', N'Limousine gepanzert', N'Armored sedan');
INSERT INTO swiss_data_dicionarios.dbo.BodyTypes (CODE, DE, PT) VALUES (N'699', N'Übrige gemäss Angaben des Verkehrsexperten', N'Other ');