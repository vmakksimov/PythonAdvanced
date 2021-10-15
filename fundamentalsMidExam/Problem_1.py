food_per_month = float(input()) * 1000
hay_per_month = float(input()) * 1000
cover_per_month = float(input()) * 1000
pig_weight = float(input()) * 1000
none_food = False
for day in range(1, 30 +1):
   food_per_month -= 300

   if food_per_month <= 0:
        none_food = True
        break
   if day % 2 == 0:
        hay_per_month -= food_per_month * 0.05
        if hay_per_month <= 0:
            none_food = True
            break
   if day % 3 == 0:
        cover_per_month = cover_per_month - (pig_weight / 3)
        if cover_per_month <= 0:
            none_food = True
            break

if not none_food:
    print(f'Everything is fine! Puppy is happy! Food: {food_per_month / 1000:.2f}, Hay: {hay_per_month/ 1000:.2f}, Cover: {cover_per_month/ 1000:.2f}.')
else:
    print(f'Merry must go to the pet store!')


