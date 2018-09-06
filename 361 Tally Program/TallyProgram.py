#https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/
from collections import Counter
import operator

input = 'dbbaCEDbdAacCEAadcB'
points_dict = Counter(input)
total_points = {}

for person, points in points_dict.items():
    total_points[person.lower()] = points_dict[person.lower()] - points_dict[person.upper()]

total_points = sorted(total_points.items(), key = operator.itemgetter(1), reverse = True)
    
print(total_points)
    
    