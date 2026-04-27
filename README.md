Discrete-Event Simulation of a Production System

1. Overview
This project implements a discrete-event simulation of a single-machine production system using Python and SimPy.

Jobs arrive randomly, are queued, and processed by a machine. The simulation captures key production dynamics such as machine utilization, waiting time, and the impact of breakdowns and repairs.

2. Features
a. Discrete-event simulation using SimPy
b. FIFO (First-In-First-Out) job queue
c. Stochastic job arrivals and processing times
d. Machine states: IDLE, PROCESSING, BROKEN, REPAIRING
e. Performance metrics:
    1. Machine utilization
    2. Average waiting time
    3. Total jobs processed


3. Requirements
a. Python 3.11 or higher
b. uv (Python package manager)


4. Setup Instructions
    A. Install dependencies:
        uv sync

5. Run Simulation
    uv run python main.py

6. Example Output

The simulation prints:

a. Job arrivals
b. Queue updates
c. Machine processing events
d. Breakdown and repair events
e. Final results including utilization and waiting time


7. Project Structure
    simulation-project/
    │
    ├── main.py           # Simulation logic
    ├── pyproject.toml   # Project dependencies (managed with uv)
    ├── README.md        # Project documentation
    ├── REPORT.md        # Detailed explanation and analysis


8. Notes:
A. The simulation uses random values for arrivals, processing times, and breakdowns.
B. Results may vary between runs.
C. This project is a simplified prototype and can be extended to real-world applications.


9. Possible Extensions
A. Integration with MQTT for real-time data exchange
B. Use of real-world log data for parameter estimation
C. Expansion to multi-machine systems
D. Visualization of system performance