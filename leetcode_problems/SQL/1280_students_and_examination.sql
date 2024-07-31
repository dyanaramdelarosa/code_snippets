-- Problem Link: https://leetcode.com/problems/students-and-examinations/
-- Author: Dyanara Dela Rosa
-- Date: June 16, 2024


select stud.student_id, stud.student_name, subj.subject_name, coalesce(exam.attended_exams,0) as attended_exams
from students stud
cross join subjects subj
left join (
    select student_id, subject_name, count(*) as attended_exams
    from examinations
    group by student_id, subject_name
) exam
on stud.student_id = exam.student_id 
and subj.subject_name = exam.subject_name 
order by stud.student_id, subj.subject_name