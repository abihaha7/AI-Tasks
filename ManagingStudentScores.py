scores = [10, 20, 30, 40, 50]
# add a new score
scores.append(25)
# remove a specific score
scores.remove(20)
# Find the highest and lowest scores
highest = max(scores)
lowest = min(scores)
# sorting the scores
scores.sort()
# calculate average
average = sum(scores)/len(scores)
print("scores:", scores)
print("highest score:", highest)
print("lowest scores:", lowest)
print("average score:", average)
