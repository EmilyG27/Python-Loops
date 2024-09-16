import random

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
moods = ["happy", "sad", "energetic", "calm"]

for i in days_of_week:
    print(f"On {i}, you were feeling {random.choice(moods)}.")