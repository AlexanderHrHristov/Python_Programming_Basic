from math import ceil

movie_name = str(input())
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght * 1 / 8
recreation_time = break_lenght * 1 / 4

left_time_for_movie = break_lenght - (lunch_time + recreation_time)
needed_time = ceil(abs(left_time_for_movie - episode_lenght))

if left_time_for_movie >= episode_lenght:
    print(f"You have enough time to watch {movie_name} and left with "
          f"{needed_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you "
          f"need {needed_time} more minutes.")

