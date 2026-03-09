"""
Aim: Write a program to demonstrate Dictionary & related functions in python
"""

def demonstrate_dictionaries():
    print("\n--- DICTIONARY DEMONSTRATION ---")
    
    student = {
        "name": "Alice",
        "age": 22,
        "major": "Computer Science",
        "gpa": 3.8
    }
    print(f"Original Dictionary: {student}")
    
    print(f"Student's Name: {student['name']}")
    
    # get()
    print(f"Student's GPA using get(): {student.get('gpa')}")
    print(f"Missing key using get(): {student.get('graduation_year', 'Not Specified')}")
    
    student["graduation_year"] = 2026  
    student["gpa"] = 3.9               
    print(f"After adding/updating: {student}")
    
    # update()
    student.update({"age": 23, "honors": True})
    print(f"After update() method: {student}")
    
    # keys()
    print(f"Dictionary Keys: {student.keys()}")
    
    # values()
    print(f"Dictionary Values: {student.values()}")
    
    # items()
    print(f"Dictionary Items: {student.items()}")
    
    # pop()
    removed_major = student.pop("major")
    print(f"Removed Major: {removed_major}")
    
    # popitem()
    last_item = student.popitem()
    print(f"Removed last item: {last_item}")
    
    # clear()
    student.clear()
    print(f"Dictionary after clear(): {student}")

demonstrate_dictionaries()
