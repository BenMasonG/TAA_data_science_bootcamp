-- Ensure the correct database is selected.
USE uni;


-- Write a select statement to obtain all of the student information for successful applications made for Course 11 which do not relate to current students
SELECT * FROM application
WHERE CourseAppliedFor = 11 AND StudentID = 0 AND accepted = 1;

-- Modify the select statement from the previous example into an insert statement and insert the data into the student table
INSERT INTO student (CourseID, Forenames, Surname, EmailAddress)
SELECT CourseAppliedFor, Forenames, Surname, EmailAddress
FROM application
WHERE CourseAppliedFor = 11 AND StudentID = 0 AND accepted = 1;


-- Write a select statement to obtain all the information for the unsuccessful applications made for Course 11
SELECT * FROM application
WHERE CourseAppliedFor = 11 AND accepted = 0;


-- Modify the select statement from the previous example into a delete statement and delete the unsuccessful Course 11
DELETE FROM application
WHERE CourseAppliedFor = 11 AND accepted = 0;

-- Write a select statement to identify the unsuccessful applications for course 1 made after 01/08/2020
SELECT * FROM application
WHERE CourseAppliedFor = 1 AND accepted = 0 AND DateOfApplication > '2020-08-01';

-- The above query does not return any results as there were no unsuccessful applications for course 1 made after the given date.


-- Using the select statement from the previous example, modify it into an update statement and update the applications to successful
UPDATE application
SET accepted = 1
WHERE CourseAppliedFor = 1 AND accepted = 0 AND DateOfApplication > '2020-08-01';


-- Roll back the previous update
ROLLBACK;

-- The above command would not work unless I had previous used the command 'SET autocommit = 0' as MYSQL intrinsically commits all updates and the rollback function cannot be used after an update has been committed. 


-- Modify the previous update to include applications for economics courses made after 01/09/2020
-- No modifications needed as Course 1 is economics.
