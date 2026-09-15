# assignment
**Name:** Charu Choudhary
**Phone:** 8875694600

## Part 1: Coding

**Q1: What happens to the average when 50°C is introduced?**  
The average increases a lot (from 31.40 to 33.60) even though only one value changed. This shows the average is very sensitive to outliers.

**Q2: Why is detecting high sensor readings useful in a robotic system?**  
It helps catch problems early, like overheating or a faulty sensor, so the robot can shut down or cool itself before damage happens.

## Part 2: Control Systems (Simulink)

**Q1: What happens to the motor response as Kp is increased?**  
The response becomes faster and gets closer to the desired speed of 10 as Kp increases.

**Q2: Does the output reach exactly 10? Explain.**  
No. With proportional control only, there is always some error left. As the output gets closer to 10, the error becomes very small, so the controller's push also becomes small — the motor settles just below 10 instead of exactly reaching it.
