# *GmE 205 Laboratory 2 — Simple Spatial Object in Python*

The main objective of this laboratory activity is to develop a simple object-oriented spatial model in Python that represents spatial entities through their geometry, attributes, and behavior, while applying principles of abstraction, separation of responsibilities, and reproducible spatial analysis.

### Objectives

The objectives of this laboratory are to:

- Model spatial entities as objects with state and behavior, not just geometry.
- Distinguish between data (geometry) and meaning (rules and responsibilities).
- Implement basic Python classes and methods to support spatial reasoning.
- Produce reproducible outputs that reflect abstraction, representation, responsibility, and scale.

### Tools and Technologies

The following tools were used:

- *Python 3.x*
- *Visual Studio Code*
- *Git*
- *GitHub*
- *Pandas*
- *Matplotlib*

### How to set up the virtual environment

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

## Reflection

### Object VS Geometry

Thinking of points as objects transformed how I approached spatial data, since they stopped being mere rows in a table holding longitude and latitude values. Instead, each point became a full-fledged object with its own identity, position, meaning, and behavior. A Point, for instance, could hold an ID, longitude, latitude, name, and tag, while also being capable of validating its own coordinates and computing its distance to another point. This shift showed me that spatial data isn't just about geometry, it's equally about what each point represents and what actions it can perform.

> **Key idea:** A spatial point is more than just coordinates—it has **identity, meaning, and behavior**.

### Responsibility

Responsibilities were split according to what each object or script was meant to do. The `Point` class took care of individual point-level behavior, including validating coordinates, converting its coordinates into a tuple, and calculating its distance from another point. The `PointSet` class handled behavior involving a collection of points, such as counting points, finding the bounding box, and filtering points by tag. The `runner script` managed the overall workflow, including loading the PointSet, generating the scatter plot, and writing the JSON report.

One concrete example is coordinate validation. This responsibility belongs in `Point` because each individual point must confirm that its own longitude and latitude are valid. Calculating the bounding box, on the other hand, belongs in `PointSet` since it requires examining multiple points at once. Plotting and saving the results belong in the runner script rather than in Point or PointSet, since they involve the overall process rather than the behavior of a single object or collection.

> **Responsibility rule:** `Point` handles **one point**, `PointSet` handles **a collection of points**, and the `runner script` handles **the overall workflow and outputs**.

### Modeling Insight

Separating geometry, meaning, and behavior made the spatial logic easier to understand because each part had a clear purpose. The coordinates represent the geometry, while the name and tag provide meaning, such as identifying a point as a POI. The methods provide the behavior, such as checking whether the coordinates are valid, calculating distance, or determining if a point is a POI. This separation also made the code easier to organize because Point handled individual points, PointSet handled groups of points, and the runner script handled outputs.

Separating these features also helps avoid creating a **"God Object,"** where everything is mixed together, which can make the code messy and hard to follow. It also makes debugging easier, since errors can be traced back to a specific, well-defined piece of functionality rather than searched for across a tangle of mixed responsibilities. Overall, this approach helped me understand that spatial programming is not just about storing coordinates, it's about giving spatial data meaning and appropriate behavior.

> **Modeling insight:** Keeping geometry, meaning, and behavior separate makes the code **clearer, less messy, and easier to debug**.
