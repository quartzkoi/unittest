import unittest
from Student import Student, Event, Assignment

class TestAssignment(unittest.TestCase): #Confirming if grade percentages are correct
    def test_getPercentage(self):
        a = Assignment("Assignment 1", 10, 20)
        self.assertEqual(a.getPercentage(), 0.5)

class TestStudent(unittest.TestCase):#Confirming correct student
    def setUp(self):
        self.student = Student("Matthew Pogue", "h735f787")

    def test_addEvent(self):#Testing if Events are properly added
        event = Event("Lecture", "Meeting")
        self.student.addEvent(event)
        self.assertEqual(len(self.student.events), 1)

    def test_countMeetings(self): #Testing the number and type of each event
        events = [Event("Lecture 1", "Meeting"), Event("Lecture 2", "Meeting")]
        self.student.addEvent(events)
        self.assertEqual(self.student.countMeetings(), 3)

    def test_getGrade(self): #Testing the numerical grade of each assignment
        assignments = [Assignment("Assignment 1", 10, 20), Assignment("Assignment 2", 20, 20)]
        self.student.addAssignment(assignments)
        self.assertEqual(self.student.getGrade(), 0.75)

    def test_getLetterGrade(self): #Test of letter grade matching numerical grade
        grade = 0.8
        self.assertEqual(self.student.getLetterGrade(grade), "B")

if __name__ == '__main__':
    unittest.main()