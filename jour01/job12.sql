INSERT INTO etudiants (nom, prenom, email, age)
VALUES ('Dupuis', 'Martin', 'martin.dupuis@laplateforme.io', 18);

SELECT *
FROM etudiants
WHERE nom = 'Dupuis';
