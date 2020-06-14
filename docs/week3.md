### Week 3 Meeting 9

#### Readings
1.[Design Challenges for Secure Implantable Medical Devices](Readings/week3_1.pdf)

2.[A Lightweight Cryptographic System forImplantable Biosensors](Readings/week3_2.pdf)

#### Lecture notes
1. How is the heat control for the bio-sensor implant device?

2. IMD encryption can be really inexpensive. 

### Week 3 Meeting 10

#### Reading
[Introduction to differential power analysis](Readings/week3_3.pdf)

#### Lecture notes
1. Side-Channel Analysis is power analysis on circuit to get secret information.

2. SPA vs DPA

3. Place to learn some basic logit circuit? Lecture 17:27

4. Chip Power pad plot reveals the running clock of the chip. Time divided by fluctuation is the one running time. Take the invert of the time, you get the running clock speed. Lecture 21:25

5. DPA to reduce the possiblity of the key. Originally, it's 2^8. After a few analysis, it can go to 2^5. Then we can brute force search.

6. dpacontest.org

#### Power analysis assignment
[exploring side-channel attack](../Code/PowerAnalysis/DPA assignment.pdf)
