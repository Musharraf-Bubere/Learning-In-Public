CREATE DATABASE titanic;

USE titanic;

SELECT * FROM titanic_dataset; -- All columns
SELECT Name,Sex,Survived FROM titanic_dataset; -- Filter Columns
SELECT Name AS PassengerName, SEX AS Gender, Survived AS Survived FROM titanic_dataset; -- Alias AS
