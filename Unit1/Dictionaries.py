# 4.1 Create and access dictionary
student = {"name": "Aadit", "roll": 1, "marks": 85}
print("Dictionary:", student)
print("Name:", student["name"])

# 4.2 Update dictionary
student["marks"] = 90
student["grade"] = "A"
print("Updated Dictionary:", student)

# 4.3 Remove elements
student.pop("roll")
print("After removing roll:", student)

# 4.4 Merge dictionaries
extra = {"city": "Delhi", "age": 19}
student.update(extra)
print("Merged Dictionary:", student)
