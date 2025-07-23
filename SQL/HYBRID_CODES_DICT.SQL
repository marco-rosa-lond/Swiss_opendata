create table Hybrid_codes
(
    Code        nvarchar(20) not null
        constraint Hybrid_codes_pk
            primary key,
    Motorizacao nvarchar(100)
)
go

INSERT INTO Hybrid_codes (Code, Motorizacao) VALUES (N'N/A', null);
INSERT INTO Hybrid_codes (Code, Motorizacao) VALUES (N'NOVC-FCHV', N'Híbrido');
INSERT INTO Hybrid_codes (Code, Motorizacao) VALUES (N'NOVC-HEV', N'Híbrido');
INSERT INTO Hybrid_codes (Code, Motorizacao) VALUES (N'OVC-HEV', N'Híbrido Plug-In');
