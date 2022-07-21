USE uni;

-- Obtain a list of applications where the CourseID is unknown
SELECT * FROM application
WHERE CourseAppliedFor IS null;

-- Obtain a list of students where their CourseID is not unknown
SELECT * FROM student
WHERE CourseID IS null;

-- Obtain a list of students whom were born in the month of June 2002
SELECT * FROM student
WHERE year(DateOfBirth) = '2002' AND monthname(DateOfBirth) = 'June';

-- Obtain a list of applications where CourseID is unknown and the applications where  made between 01/04/2020 and 31/07/2020
SELECT * FROM application
WHERE CourseAppliedFor IS null AND DateOfApplication BETWEEN '2020-04-01' AND '2020-07-31';

-- Task 2
-- Obtain the number of modules which are assigned to each course
SELECT Subject, COUNT(ModuleID) AS NumberOfModules FROM module -- sorted by subject as 2 chemistry modules do not have an assigned CourseID
GROUP BY Subject;

-- Retrieve Information on the number of successful applications per course
SELECT CourseAppliedFor, COUNT(accepted) AS NumberOfSuccessfullApplications FROM application
GROUP BY CourseAppliedFor;


-- Find the average Membership Fee of Student Clubs by the ID of the Staff member (Lecturer) supervising it
SELECT SupervisingStaff, AVG(MembershipFee) AS AvgFeeByStaffID FROM club
GROUP BY SupervisingStaff;

-- Find the Sum total of Joining Fees for all active clubs by Staff Member supervising them
SELECT SupervisingStaff, Sum(JoiningFee) AS SumOfJoiningFeeByStaffID FROM club
WHERE Active = 1
GROUP BY SupervisingStaff;

-- Task 3
-- Obtain a list of all modules and the names of any courses they may be taught [on (I am guessing this is the mssing word)](include modules without courses)
SELECT ModuleName, CourseName, course.CourseID FROM module
LEFT JOIN course
ON module.CourseID = course.CourseID
ORDER BY CourseID; 

-- Obtain a list of students along with any related application numbers if they have them
SELECT student.*, ContactNumber FROM student
lEFT JOIN application
ON student.StudentID = application.StudentID;


-- Obtain the Class ID, Class Date and Feedback score of the latest class scheduled for each Class ID
SELECT schedule.ClassID, schedule.CDate, schedule.FeedbackScore FROM schedule
INNER JOIN (
    SELECT ClassID, MAX(CDate) AS LatestDate
    FROM schedule
    GROUP BY ClassID
) tm ON schedule.ClassID = tm.ClassID AND schedule.CDate = tm.LatestDate;



