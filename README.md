# Pendulum Simulator

This is supposed to be a program simulating movements of a pendulum.
Works decently.

# What are the differences between versions?

### 'Hardcoded edition' (version 1) 
The pendulum rotates 1 degree per frame, causing it to look like it's accelerating near the end, when the max swing angle is heavily reduced in comparison to the starting angle.

### Version 2
This one was supposed to be a full exploration of forces that affect tge pendulum, but I gave up on using the drag force properly. However, it actually slows down near the end of the simulation.

[explanation](https://github.com/TacoConKvass/Pendulum-Sim/assets/128845692/3e912005-595d-452a-b8d4-1af9f8e8218c)

This image is here to explain the naming of angles in the calculateDistanceToFloor method, as well as show, where did the math come from
Note after version 1: It turned out to be basically useless
Note after version 2: It is basically useless. I could use it to display the gravitational potential energy of the pendulum, but it's not needed.
