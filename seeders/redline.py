

query = '''
INSERT INTO towns (name, postal_code) VALUES ('Dallas', '752000');
INSERT INTO towns (name, postal_code) VALUES ('Nanterre', '92001');

INSERT INTO nationalities (name) VALUES ('Français');
INSERT INTO nationalities (name) VALUES ('Américain');

INSERT INTO persons (last_name, first_name, genre, street_number, street_name, additional_address, town_id, nationality_id) VALUES ('Perrier', 'Hugo', 0, '1 bis', 'Rue de la Paix', 'Bat. 7', 2, 1);
INSERT INTO persons (last_name, first_name, genre, street_number, street_name, additional_address, town_id, nationality_id) VALUES ('Leclerc', 'Vanessa', 0, '7', 'Bd. de la Guerre', 'Etg. 10', 2, 1);
INSERT INTO persons (last_name, first_name, genre, street_number, street_name, additional_address, town_id, nationality_id) VALUES ('Smith', 'William', 0, '465', 'Main Street', '', 1, 2);
INSERT INTO persons (last_name, first_name, genre, street_number, street_name, additional_address, town_id, nationality_id) VALUES ('Phillix', 'Zack', 0, '789', 'Pine Lane', '', 1, 2);
INSERT INTO persons (last_name, first_name, genre, street_number, street_name, additional_address, town_id, nationality_id) VALUES ('Jackson', 'Agata', 0, '101', 'Maple Joe Court', 'Flat 8888', 1, 2);

INSERT INTO policemen (person_id, serial_numbers) VALUES (4, '777LUCKYPLC');

INSERT INTO suspects (person_id, verdict) VALUES (1, '');
INSERT INTO suspects (person_id, verdict) VALUES (2, '');
INSERT INTO suspects (person_id, verdict) VALUES (3, '');

INSERT INTO juries (person_id) VALUES (5);

INSERT INTO fusillades (street_number, street_name, additional_address, date, description, town_id) VALUES ('482', 'Oak Avenue', '', '2007-02-21', 'It started in the morning at 09:17 near the traffic jam and ended near 09:45. Two people were injuried. No deaths.', 1);
 
INSERT INTO investigations (advancement, fusillade_id) VALUES ('Enquête ouverte à ce jour.', 1);

INSERT INTO investigation_policemen (investigation_id, policeman_id) VALUES (1, 1);

INSERT INTO investigation_juries (investigation_id, jury_id) VALUES (1, 1);

INSERT INTO investigation_suspects (investigation_id, suspect_id) VALUES (1, 1);
INSERT INTO investigation_suspects (investigation_id, suspect_id) VALUES (1, 2);
INSERT INTO investigation_suspects (investigation_id, suspect_id) VALUES (1, 3);    
'''