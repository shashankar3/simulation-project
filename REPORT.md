Discrete-Event Simulation of a Production System

1. Scope of the Prototype

This project implements a discrete-event simulation of a simplified production system consisting of a single machine and a queue of incoming jobs. The objective of the prototype is to model the dynamic behavior of a production environment over time and evaluate key performance metrics such as machine utilization, job waiting time, and system throughput.

The simulation is developed using Python and the SimPy library, which enables event-driven modeling of time-based processes. The system captures stochastic behavior through randomly generated job arrival times, processing durations, and machine breakdown events.

While simplified, this prototype reflects fundamental characteristics of real-world production systems and serves as a foundation for more advanced digital twin applications.


2. Chosen Machine States

The machine is modeled using explicit operational states to reflect realistic behavior:

a. IDLE: The machine is not processing any job due to an empty queue.
b. PROCESSING: The machine is actively processing a job.
c. BROKEN: A failure has occurred during operation, interrupting processing.
d. REPAIRING: The machine is undergoing repair before returning to operation.

These states allow the simulation to capture productive time and the inefficiencies such as downtime and failures, which are critical for performance evaluation in production environments.


3. Evaluation Approach and Findings

A. Simulation Setup:

The system is evaluated under stochastic conditions:
a. Job interarrival time: Uniform random distribution between 1 and 5 time units
b. Processing time: Uniform random distribution between 2 and 6 time units
c. Machine breakdown probability: 10% during processing
d. Repair time: Random between 3 and 6 time units
e. Total simulation time: 50 time units

B. Performance Metrics:

The following metrics are computed:
a. Machine utilization: Ratio of productive (busy) time to total operational time
b. Idle time: Time during which the machine is not processing jobs
c. Average waiting time: Average time jobs spend waiting in the queue before processing
d. Throughput: Total number of jobs processed during the simulation

C. Findings

The simulation demonstrates how variability in arrival and processing times affects system performance. When job arrivals are frequent relative to processing capacity, queue lengths increase, resulting in higher waiting times.

Machine breakdown events introduce additional variability and reduce overall utilization. The inclusion of repair time highlights the impact of downtime on system efficiency.

The system behavior aligns with expected queueing dynamics, where performance is highly sensitive to load conditions and machine reliability.



4. MQTT Extension

The current simulation can be extended into a real-time system through integration with MQTT.

In such an extension:
a. The simulation could subscribe to real-time data streams from machines (eg.: job arrivals, machine states, sensor readings)
b. It could publish predictions or system insights, such as expected delays or queue buildup
c. Machine state transitions (IDLE, PROCESSING, BROKEN) could be synchronized with physical systems

This integration would transform the simulation into a digital twin, enabling continuous alignment between the virtual model and the physical production environment.



5. Parameter Estimation (System Identification)

Simulation parameters can be derived from real-world data:

a. Statistical analysis of historical job processing times to determine appropriate probability distributions
b. Estimation of arrival rates based on timestamps of incoming jobs
c. Failure rate modeling using machine maintenance and breakdown logs
d. Regression or distribution fitting methods to align simulation behavior with observed data



6. Required Real-World Log Data

a. Job arrival timestamps (when jobs enter the system)
b. Processing start and completion times (to determine service duration)
c. Machine state logs (IDLE, PROCESSING, BROKEN, REPAIRING)
d. Failure and repair records (including duration and frequency of breakdowns)



7. Assumptions and Limitations

Assumptions:

a. The system consists of a single machine
b. Jobs are processed in a First-In-First-Out (FIFO) order
c. Processing and arrival times follow uniform random distributions
d. Machine breakdown probability is constant
e. No setup times or resource constraints are considered

Limitations:

a. The model does not include multiple machines or parallel processing
b. It assumes simplified failure behavior without detailed root-cause modeling
c. External factors such as operator interaction or supply delays are not considered
d. The simulation is not yet connected to real-time data sources
