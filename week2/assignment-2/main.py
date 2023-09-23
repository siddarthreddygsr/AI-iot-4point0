import scheduler as sc
from scheduler import processes

# Call the scheduling functions for different algorithms
fcfs_schedule, fcfs_avg_waiting_time, fcfs_avg_turnaround_time = sc.fcfs_scheduling(processes)
sjf_schedule, sjf_avg_waiting_time, sjf_avg_turnaround_time = sc.sjf_scheduling(processes)
# print(processes)
priority_schedule, priority_avg_waiting_time, priority_avg_turnaround_time = sc.priority_scheduling(processes)
round_robin_schedule, round_robin_avg_waiting_time, round_robin_avg_turnaround_time = sc.round_robin_scheduling(processes)


print("+-------------+------------------------+---------------------------+")
print("| Algorithm   |   Average Waiting Time |   Average Turnaround Time |")
print("+=============+========================+===========================+")
print(f"| FCFS        |                  {fcfs_avg_waiting_time:.2f} |                     {fcfs_avg_turnaround_time:.2f} |")
print("+=============+========================+===========================+")
print(f"| SJF         |                  {sjf_avg_waiting_time:.2f} |                     {sjf_avg_turnaround_time:.2f} |")
print("+=============+========================+===========================+")
print(f"| Priority    |                  {priority_avg_waiting_time:.2f} |                     {priority_avg_turnaround_time:.2f} |")
print("+=============+========================+===========================+")
print(f"| Round Robin |                  {round_robin_avg_waiting_time:.2f} |                     {round_robin_avg_turnaround_time:.2f} |")
print("+-------------+------------------------+---------------------------+")

average_times = {
    "FCFS": (fcfs_avg_waiting_time, fcfs_avg_turnaround_time),
    "SJF": (sjf_avg_waiting_time, sjf_avg_turnaround_time),
    "Priority": (priority_avg_waiting_time, priority_avg_turnaround_time),
    "Round Robin": (round_robin_avg_waiting_time, round_robin_avg_turnaround_time)
}

suitable_algorithm = min(average_times, key=lambda x: (average_times[x][1], average_times[x][0]))

print(f"Suitable Algorithm: {suitable_algorithm}")