# EC500-HealthMonitorSystem
Our team's implementation of the health monitor system for assignment 1 of EC500.

Architecture Explanation
  - Data has been made into a separate thread from the ui allowing for data collection to be asynchronous from the other functions called from the UI

Pros of Approach:
   - Easy to get data from or sensor modules
   - Sensor module is easily initialized

Cons of Approach:
    - There is still not a lot of asynchronous behavior throughout the entire project

Prerequisites:
   - Python >= 3.0
   - tkinter
   - cryptography
