"""
Aim: Write a program to demonstrate tuple & related functions in python.
"""

def dictionaries():
    student = {
        "name": "Alice",
        "age": 22,
        "major": "Computer Science",
        "gpa": 3.8
    }
    
    print("Original Dictionary:", student)
    
    print("Student's Name:", student['name'])
    
    print("Student's GPA using get:", student.get('gpa'))
    
    student["graduation year"] = 2026
    student["gpa"] = 3.9
    print("After updating:", student)
    
    student.update({"age": 23, "honors": True})
    print("After update :", student)
    
    print("Dictionary Keys:", student.keys())
    print("Dictionary Values:", student.values())
    print("Dictionary Items:", student.items())
    
    removed_major = student.pop("major")
    print("Removed Major:", removed_major)
    
    last_item = student.popitem()
    print("Removed last item:", last_item)
    
    student.clear()
    print("Dictionary after clear():", student)

dictionaries()
