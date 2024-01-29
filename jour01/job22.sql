SELECT *
FROM etudiants
WHERE age = (SELECT MIN(age) FROM etudiant);
