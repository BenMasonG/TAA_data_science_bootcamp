-- Ensure the correct database is selected.
USE uni;

-- Obtain a list of Students and the name of the Courses they are studying
SELECT CourseName, concat(Forenames, ' ',Surname) AS `Student Name` FROM course
INNER JOIN student
ON student.CourseID = course.CourseID;

-- Obtain a list of course names, full time fees and part time fees for each course
SELECT CourseName, FullTimeFee, PartTimeFee FROM course
INNER JOIN fees
ON fees.CourseID = course.CourseID;

-- Obtain a list of classIDs for the Economics Course and the modules they relate to
SELECT ClassID, ModuleName, Subject FROM class
INNER JOIN module
ON class.ModuleID = module.ModuleID
WHERE CourseID = 1;