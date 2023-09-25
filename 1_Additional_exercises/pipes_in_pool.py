pool_volume = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
time_hours = float(input())

liters_pipe_one = first_pipe_debit * time_hours
liters_pipe_two = second_pipe_debit * time_hours
total_liters = liters_pipe_one + liters_pipe_two

pool_fullness_percentage = ((liters_pipe_one + liters_pipe_two)/pool_volume) * 100
first_pipe_usage = (liters_pipe_one / total_liters) * 100
second_pipe_usage = (liters_pipe_two / total_liters) * 100
overflow = abs(pool_volume - total_liters)

if total_liters <= pool_volume:
    print(f'The pool is {pool_fullness_percentage:.2f}% full. Pipe 1: {first_pipe_usage:.2f}%. Pipe 2: {second_pipe_usage:.2f}%.')
else:
    print(f'For {time_hours:2f} hours the pool overflows with {overflow:.2f} liters.')
