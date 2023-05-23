def schedule_jobs(jobs):
    # Sort jobs based on decreasing order of their durations
    jobs = sorted(jobs, key=lambda x: x[1], reverse=True)

    n = len(jobs)
    result = [None] * n
    slot = [False] * n

    # Iterate through all the jobs
    for i in range(n):
        # Find a slot in the result array starting from the deadline and moving towards the beginning
        for j in range(min(n, jobs[i][2]) - 1, -1, -1):
            if not slot[j]:
                result[j] = jobs[i][0]
                slot[j] = True
                break

    return result


# User input for the number of jobs
num_jobs = int(input("Enter the number of jobs: "))

jobs = []

# User input for the details of each job
for i in range(num_jobs):
    job_id = input(f"Enter the ID of job {i + 1}: ")
    duration = int(input(f"Enter the duration of job {i + 1}: "))
    deadline = int(input(f"Enter the deadline of job {i + 1}: "))
    jobs.append((job_id, duration, deadline))

# Schedule the jobs
scheduled_jobs = schedule_jobs(jobs)

# Print the scheduled jobs
print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(job)
