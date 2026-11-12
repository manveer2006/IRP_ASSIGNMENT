
# Task 5: Short Analysis

## (a) Operating System Process States

When a program is launched, its process enters the New state. After creation, it moves to the Ready state, where it waits for CPU allocation. When the CPU is assigned, it enters the Running state and executes instructions. When the program uses input(), it moves to the Waiting or Blocked state because it must wait for the user to enter data. After receiving input, it returns to the Ready state and then to the Running state. Once execution is completed, the process enters the Terminated state.

## (b) Suitable Cloud Service Model

Platform as a Service (PaaS) is suitable for a web-based Placement Readiness Tracker used by approximately 200 students. It provides a managed environment to deploy applications without manually managing servers, operating systems and runtime environments. The Python application can be converted into a web application using Flask and deployed on a PaaS platform. This makes deployment, maintenance and scaling easier when many students access the application simultaneously. IaaS requires more infrastructure management, while SaaS generally provides ready-made software rather than a platform for hosting our own application.
