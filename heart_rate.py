"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
import math

current_age = 23
min_heart_rate = (220 - current_age)*0.65
max_heart_rate = (220 - current_age)*0.85

print(f'Min heart rate: {min_heart_rate}')
print(f'Max heart rate: {max_heart_rate:.2f}')
