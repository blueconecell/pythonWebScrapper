numbers = [
  1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️",
  10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16
]
result = 0
for i in range(len(numbers)):
  if type(numbers[i]) == int:
    result += numbers[i]
print(result)
