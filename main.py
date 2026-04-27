import simpy
import random


RANDOM_SEED = 42
SIM_TIME = 50


# MACHINE PROCESS
def machine_process(env, machine, queue, stats):
    while True:
        if len(queue.items) == 0:
            # No jobs : machine idle
            yield env.timeout(1)
            continue

        # Get next job from queue
        job = yield queue.get()

        print(f"Time {env.now}: Machine STARTS {job['name']} (Queue: {len(queue.items)})")

        start_time = env.now

        processing_time = job["processing_time"]
        yield env.timeout(processing_time)

        finish_time = env.now

        print(f"Time {env.now}: Machine FINISHES {job['name']}")

        # stats
        stats["busy_time"] += processing_time
        stats["jobs"].append({
            "name": job["name"],
            "arrival": job["arrival"],
            "start": start_time,
            "finish": finish_time,
            "waiting_time": start_time - job["arrival"]
        })


# JOB GENERATOR
def job_generator(env, queue):
    job_id = 0

    while True:
        yield env.timeout(random.randint(1, 5))

        job_id += 1

        job = {
            "name": f"Job {job_id}",
            "arrival": env.now,
            "processing_time": random.randint(2, 6)
        }

        print(f"Time {env.now}: {job['name']} ARRIVES (Queue before: {len(queue.items)})")

        yield queue.put(job)

        print(f"Time {env.now}: {job['name']} ENTERS queue (Queue now: {len(queue.items)})")



# RUN SIMULATION
def run_simulation():
    random.seed(RANDOM_SEED)

    env = simpy.Environment()

    # queue (FIFO)
    queue = simpy.Store(env)

    stats = {
        "busy_time": 0,
        "jobs": []
    }

    # start processes
    env.process(machine_process(env, None, queue, stats))
    env.process(job_generator(env, queue))

    env.run(until=SIM_TIME)

    
    # RESULTS
    print("\n--- RESULTS ---")
    print(f"Total busy time: {stats['busy_time']}")
    print(f"Machine utilization: {stats['busy_time'] / SIM_TIME:.2f}")

    avg_wait = sum(j["waiting_time"] for j in stats["jobs"]) / len(stats["jobs"])
    print(f"Average waiting time: {avg_wait:.2f}")

    print(f"Total jobs processed: {len(stats['jobs'])}")



# ENTRY POINT
if __name__ == "__main__":
    run_simulation()