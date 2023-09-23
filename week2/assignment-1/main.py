import scheduler as sc

time_quantum = 2

# Run and print all scheduling algorithms
fcfs_schedule, fcfs_avg_waiting_time, fcfs_avg_turnaround_time = sc.fcfs_scheduling(sc.tasks)
sjf_schedule, sjf_avg_waiting_time, sjf_avg_turnaround_time = sc.sjf_scheduling(sc.tasks)
ps_schedule, ps_avg_waiting_time, ps_avg_turnaround_time = sc.ps_scheduling(sc.tasks)
rr_schedule, rr_avg_waiting_time, rr_avg_turnaround_time = sc.rr_scheduling(sc.tasks, time_quantum)

print("FCFS Schedule:")
for task, start_time in fcfs_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {fcfs_avg_waiting_time}")
print(f"Average Turnaround Time: {fcfs_avg_turnaround_time}")

print("\nSJF Schedule:")
for task, start_time in sjf_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {sjf_avg_waiting_time}")
print(f"Average Turnaround Time: {sjf_avg_turnaround_time}")

print("\nPriority Schedule:")
for task, start_time in ps_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {ps_avg_waiting_time}")
print(f"Average Turnaround Time: {ps_avg_turnaround_time}")

print("\nRound Robin Schedule:")
for task, start_time in rr_schedule:
    print(f"{task}: Start Time = {start_time}")
print(f"Average Waiting Time: {rr_avg_waiting_time}")
print(f"Average Turnaround Time: {rr_avg_turnaround_time}")

# Compare scheduling algorithms
average_waiting_times = {
    "FCFS": fcfs_avg_waiting_time,
    "SJF": sjf_avg_waiting_time,
    "Priority": ps_avg_waiting_time,
    "Round Robin": rr_avg_waiting_time,
}

average_turnaround_times = {
    "FCFS": fcfs_avg_turnaround_time,
    "SJF": sjf_avg_turnaround_time,
    "Priority": ps_avg_turnaround_time,
    "Round Robin": rr_avg_turnaround_time,
}

most_efficient_algorithm = min(average_waiting_times, key=average_waiting_times.get)
most_fair_algorithm = min(average_turnaround_times, key=average_turnaround_times.get)

print("\nMost Efficient Scheduling Algorithm:", most_efficient_algorithm)
print("Most Fair Scheduling Algorithm:", most_fair_algorithm)