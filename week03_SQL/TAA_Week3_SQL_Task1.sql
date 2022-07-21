-- Ensure the correct database is selected.
USE uni;

-- Count how many students are enrolled overall
SELECT COUNT(StudentID)
FROM student;

-- Calculate the sum of full time fees for every full-time course
SELECT SUM(FullTimeFee)
FROM fees;

-- Identify the cost of the least and most expensive course
SELECT MIN(FullTimeFee) AS LowestPrice, MAX(FulltimeFee) AS HighestPrice
From fees;

-- Calculate the average cost of all part time courses
SELECT AVG(PartTimeFee) AS AveragePartTimeFee
FROM fees;

-- Calculate the fee of each full time course after applying (subtracting) the scholarship discount
SELECT FullTimeFee - ScholarshipDiscount AS FullTimeCostWithScholarship
FROM fees;

-- Extension:
-- Select only the course number of the cheapest full-time course
SELECT CourseID
FROM fees
ORDER BY FullTimeFee
LIMIT 1;

-- Find cost of the most expensive course after applying the scholarship discount
SELECT MAX(FullTimeFee - ScholarshipDiscount) AS MaxFullTimeCostWithScholarship
FROM fees;

-- Count the number of applications for History courses made between 01/03/2020 and 30/08/2020
SELECT COUNT(applicationID) AS NumberOfApplications
FROM application
WHERE CourseAppliedFor = 11 AND DateOfApplication BETWEEN '2020-03-01' AND '2020-08-30';