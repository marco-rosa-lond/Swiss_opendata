create table vehicle_type
(
    Code       int not null
        constraint vehicle_type_pk
            primary key,
    Italiano   nvarchar(max),
    Deutsch    nvarchar(max),
    Français   nvarchar(max),
    English    nvarchar(max),
    Portuguese nvarchar(150),
    IsValid    bit
)
go

INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (1, N'Automobile', N'Personenwagen', N'Voiture de tourisme', N'Passenger car', N'Ligeiro de Passageiros', 1);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (2, N'Automobile pesante', N'Schwerer Personenwagen', N'Voiture de tourisme lourde', N'Heavy passenger car', N'Pesado de Passageiros', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (10, N'Autoveicolo leggero', N'Leichter Motorwagen', N'Voiture automobile légère', N'Light motor car', N'Veículo ligeiro para fins especiais', null);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (11, N'Autoveicolo pesante', N'Schwerer Motorwagen', N'Voiture automobile lourde', N'Heavy motor car', null, null);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (20, N'Autobus', N'Gesellschaftswagen', N'Autocar', N'Company car', null, null);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (21, N'Furgoncino', N'Kleinbus', N'Minibus', N'Minibus', N'Minibus', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (22, N'Autobus snodato', N'Gelenkbus', N'Bus à plate-forme pivotante', N'Articulated bus', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (23, N'Filobus', N'Trolleybus', N'Trolleybus', N'Trolley bus', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (24, N'Filobus snodato', N'Gelenktrolleybus', N'Trolleybus articule', N'Articulated trolley bus', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (30, N'Autofurgone', N'Lieferwagen', N'Voiture de livraison', N'Delivery van', N'Furgão', null);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (35, N'Autocarro', N'Lastwagen', N'Camion', N'Truck', N'Camião', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (36, N'Autoarticolato leggero', N'Leichtes Sattelmotorfahrzeug', N'Véhicule articulé léger', N'Light articulated vehicle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (37, N'Autoarticolato pesante', N'Schweres Sattelmotorfahrzeug', N'Véhicule articulé lourd', N'Heavy articulated vehicle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (38, N'Trattore a sella', N'Sattelschlepper', N'Tracteur à sellette', N'Articulated lorry', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (42, N'Trattore', N'Traktor', N'Tracteur', N'Tractor', N'Trator', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (43, N'Trattore agricolo', N'Landwirt. Traktor', N'Tracteur agricole', N'Farmer''s car Tractor', N'Trator agrícola', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (50, N'Macchina semovente', N'Arbeitsmaschine', N'Machine de travail', N'Working machine', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (51, N'Carro di lavoro', N'Arbeitskarren', N'Chariot de travail', N'Work cart', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (52, N'Carro di lavoro agricolo', N'Landw. Arbeitskarren', N'Chariot de travail agricole', N'Farm work cart', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (60, N'Motoveicolo', N'Motorrad', N'Motocycle', N'Motorcycle', N'Ciclomotor', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (61, N'Motoleggera', N'Kleinmotorrad', N'Motocycle léger', N'Small motorcycle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (62, N'Motoveicolo a tre ruote', N'Motorrad-Dreirad', N'Motocycle-tricar', N'Motorcycle tricycle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (63, N'Motoveicolo con carrozzino laterale', N'Motorrad-Seitenwagen', N'Motocycle-side-car', N'Motorcycle sidecar', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (64, N'Motoleggera a tre ruote', N'Kleinmotorrad-Dreirad', N'Motocycle léger-tricar', N'Small motorcycle tricycle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (65, N'Quadriciclo leggero a motore', N'Leichtmotorfahrzeug', N'Quadricycle léger à moteur', N'Light motor vehicle', null, null);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (66, N'Quadriciclo a motore', N'Kleinmotorfahrzeug', N'Quadricycle à moteur', N'Small motor vehicle', null, null);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (67, N'Triciclo a motore', N'Dreirädr. Motorfahrzeug', N'Tricycle à moteur', N'Three-wheeled motor vehicle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (68, N'Slitta a motore', N'Motorschlitten', N'Luge à moteur', N'Snowmobile', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (80, N'Carro con motore', N'Motorkarren', N'Chariot à moteur', N'Motorized cart', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (81, N'Carro con motore agricolo', N'Landw. Motorkarren', N'Chariot à moteur agricole', N'Farm motorized cart', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (82, N'Monoasse', N'Motoreinachser', N'Monoaxe', N'Motorized axle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (83, N'Monoasse agricolo', N'Landw. Motoreinachser', N'Monoaxe agricole', N'Farm motorized axle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (84, N'Veicolo agricolo combinato', N'Landw. Kombinations-Fahrzeug', N'Véhicule agricolo combiné', N'Farm combination vehicle', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (85, N'Rimorchio agricolo', N'Landw. Anhänger', N'Remorque agricole', N'Farm trailer Motorcycle trailer Trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (86, N'Rimorchio motoveicolo', N'Motorradanhänger', N'Remorque motocycle', N'Motorcycle trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (87, N'Rimorchio di lavoro agricolo', N'Landw. Arbeitsanhänger', N'Remorque de travail agricole', N'Agricultural work trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (88, N'Semirimorchio abitabile', N'Sattel-Wohnanhänger', N'Semi-remorque caravane', N'Semitrailer-caravan', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (89, N'Semirimorchio', N'Sattel-Anhänger', N'Semi-remorque', N'Semitrailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (90, N'Rimorchio per il trasporto di chose', N'Sachentransportanhänger', N'Remorque transport de choses', N'Goods transport trailer', N'Reboque de transporte de mercadorias', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (91, N'Rimorchio per il trasporto di persone', N'Personentransportanhänger', N'Remorque transport de personnes', N'Passenger transport trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (92, N'Rimorchio abitabile', N'Wohnanhänger', N'Caravane', N'Caravan', N'Caravana', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (93, N'Rimorchio per il trasporto attrezzi sportivi', N'Sportgeräteanhänger', N'Remorque engins de sport', N'Sports equipment trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (94, N'Rimorchio di lavoro', N'Arbeitsanhänger', N'Remorque de travail', N'Work trailer', N'Reboque de carga', 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (95, N'Semirimorchio trasporto di cose', N'Sattel-Sachentransportanhänger', N'Semi-remorque transport de choses', N'Semitrailer-goods transport trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (96, N'Semirimorchio per il trasporto di persone', N'Sattel-Personentransportanhänger', N'Semi-remorque transport de personnes', N'Semitrailer-passenger transport trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (97, N'Semirimorchio trasporto di attrezzi sportivi', N'Sattel-Sportgeräteanhänger', N'Semi-remorque engins de sport', N'Semitrailer-sports equipment trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (98, N'semirimorchio di lavoro', N'Sattel-Arbeitsanhänger', N'semi-remorque de travail', N'Semitrailer-work trailer', null, 0);
INSERT INTO swiss_data_dicionarios.dbo.vehicle_type (Code, Italiano, Deutsch, Français, English, Portuguese, IsValid) VALUES (99, N'Rimorchio', N'Anhänger', N'Remorque', N'Trailer', null, 0);
