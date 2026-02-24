<!-- TITLE AND SHORT DESCRIPTION -->
<div align="center">
  <h1 align="center">Cross-Device-Multiplayer-Tic-Tac-Toe</h1>
</div>
<p align="center">A program that allows you to run a tic-tac-toe game between a client and a host.</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#lessons">Lessons</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## Project Overview
The purpose of this project was to expose myself to sockets and networking with python. Tic-tac-toe was the medium, with the goal being to be able to play a game between a client and a host.
When running the program locally, there must be two seperate files, one for the host server, one for the client. The game runs in terminal. To execute it, run both python files in seperate terminal windows simultaneously. Be sure that there are no other instances of the file running, otherwise, it will not work, saying that the port is occupied. I had to manually terminate my terminal in VScode before running the program on my computer's terminal in order for it to work.
In order to run the program between two devices, make sure each has a copy of the code, and use the host's IP address (found using the terminal) in both the server's `host_game()` and the client's `connect_to_game()` rather than the "localhost" that is written in the files currently. Then, you should be able to connect the two devices to play the game.

### Built with
**Language used:** Python  

**Python libraries:**
* socket
* threading


## Lessons
The goal of this project was to explore sockets and basic networking. I learned:
* How to create a client and a host using sockets
* How to run two threads, one for each member of the connection
* How to facilitate back and forth communication between client and host


## Acknowledgements


