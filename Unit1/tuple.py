# 3.1 Create and access tuple
t1 = (10, 20, 30)
print("Tuple:", t1)
print("First element:", t1[0])

# 3.2 Nested tuple
t2 = (1, 2, (3, 4))
print("Nested Tuple:", t2)
print("Access nested element:", t2[2][0])

# 3.3 Repetition of tuple
t3 = t1 * 2
print("Repeated Tuple:", t3)

# 3.4 Concatenation of tuples
t4 = t1 + (40, 50)
print("Concatenated Tuple:", t4)
