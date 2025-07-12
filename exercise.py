# Initial list of lowercase names
names = ["alice", "bob", "charlie", "dana"]

# Task A: Capitalize first letter of each name
upper_names = [n.capitalize() for n in names]
print("Uppercase names:", ", ".join(upper_names))

# Task B: Print index + 1 alongside each name
for idx, name in enumerate(upper_names, start=1):
    print(f"{idx}. {name}")

# Task C: Demonstrate list methods
# Start with capitalized list again
names = upper_names.copy()

# Insert a new name at position 2
names.insert(1, "Eve")
print("After insert:", names)

# Remove "Charlie" (case-sensitive match)
if "Charlie" in names:
    names.remove("Charlie")
print("After removing 'Charlie':", names)

# 3. Sort by length of name
names.sort(key=len)
print("Sorted by length:", names)

# Final Output: ["Dana", "Alice", "Charlie"] (filtered result)
# For this, we rebuild the original list and filter it
names = ["alice", "bob", "charlie", "dana"]
capitalized = [n.capitalize() for n in names]
filtered = [n for n in capitalized if n not in ("Bob")]
filtered.sort(key=len)
print("Final result:", filtered)
