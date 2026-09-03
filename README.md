# Project Title

*GmE 205 Laboratory 2 — Simple Spatial Object in Python*

The main objective of this laboratory activity is to develop a simple object-oriented spatial model in Python that represents spatial entities through their geometry, attributes, and behavior, while applying principles of abstraction, separation of responsibilities, and reproducible spatial analysis.


# Objectives

The objectives of this laboratory are to:

- Model spatial entities as objects with state and behavior, not just geometry.
- Distinguish between data (geometry) and meaning (rules and responsibilities).
- Implement basic Python classes and methods to support spatial reasoning.
- Produce reproducible outputs that reflect abstraction, representation, responsibility, and scale.


# Tools and Technologies

The following tools were used:

- *Python 3.x*
- *Visual Studio Code*
- *Git*
- *GitHub*
- *Pandas*
- *Matplotlib*

# How to set up the virtual environment

1. Open the project folder (gme205-lab1) in VS Code.
2. Open the terminal (Terminal -> New Terminal) and create the virtual environment:
    py -m venv .venv 
    .\.venv\Scripts\activate 
3. Confirm the terminal prompt shows (.venv).
4. Select the interpreter inside .venv via Ctrl + Shift + P -> Python: Select Interpreter.
5. Install the required packages:
    pip install --upgrade pip
    pip install pandas matplotlib
    pip freeze > requirements.txt