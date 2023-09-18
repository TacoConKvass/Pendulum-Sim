# Pendulum Simulator

This is supposed to be a program simulating movements of a pendulum.
Works decently.

# What are the differences between versions?

### Python - 'Hardcoded edition' (version 1) 
The pendulum rotates 1 degree per frame, causing it to look like it's accelerating near the end, when the max swing angle is heavily reduced in comparison to the starting angle.

### Python - Version 2
This one was supposed to be a full exploration of forces that affect tge pendulum, but I gave up on using the drag force properly. However, it actually slows down near the end of the simulation.

### C++ - Pendulum-Sim project
This one uses OpenGL to render the simulation. The pendulum is being moved by moving the weight's center of mass by a vector. This with the addition of the inaccuracies caused by manualy calculating the sine and cosine of the angle between the pendulum's arm and the pivot, causes the line to stretch, which has to be manually fixed.