# Probability Distributions and Dice Simulation Project 🎲

This project demonstrates the application of various probability distributions using Python. It covers the generation of random data from different distributions, the visualization of these distributions with histograms, and the simulation of dice rolls using both uniform and non-uniform (weighted) methods. The project also serves as an introductory exploration to reinforcement learning concepts, particularly the multi-armed bandit problem.

---

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
  - [Section 1: Probability Distributions](#section-1-probability-distributions)
  - [Section 2: Dice Simulation](#section-2-dice-simulation)
  - [Section 3: Increasing the Probability of Six](#section-3-increasing-the-probability-of-six)
- [Results](#results)
- [Reinforcement Learning Connection](#reinforcement-learning-connection)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [License](#license)

---

## Overview

This project uses Python to explore and compare different probability distributions:
- **Normal Distribution**: Data is symmetrically distributed around a mean.
- **Poisson Distribution**: Models the number of events in a fixed interval.
- **Exponential Distribution**: Models the time between events.
- **Binomial Distribution**: Represents the number of successes in a series of independent experiments.
- **Pareto Distribution**: Often used to model the 80-20 rule where a small number of events contribute to the majority of the effect.

In addition, the project simulates dice rolls:
- **Uniform Dice Roll**: Simulates a fair dice where each face has an equal probability.
- **Non-Uniform Dice Rolls**: Uses normal and Poisson distributions to simulate dice rolls, illustrating how changing the underlying distribution can affect outcomes.
- **Weighted Dice (Cheating Dice)**: Demonstrates how to increase the probability of a specific outcome (rolling a 6) using weighted random choice.

---

## Project Structure

### Section 1: Probability Distributions 📊

- **Objective**: Generate random data using various probability distributions and visualize the data using histograms.
- **Implementation**:
  - **Normal Distribution**: Generated with `numpy.random.normal()`.
  - **Poisson Distribution**: Generated with `numpy.random.poisson()`.
  - **Exponential Distribution**: Generated with `numpy.random.exponential()`.
  - **Binomial Distribution**: Generated with `numpy.random.binomial()`.
  - **Pareto Distribution**: Generated with `numpy.random.pareto()`.

The project computes the mean and variance for each distribution, for example:
- **Normal Distribution**: Mean ≈ 0.02, Variance ≈ 0.96
- **Poisson Distribution**: Mean ≈ 2.97, Variance ≈ 2.84
- **Exponential Distribution**: Mean ≈ 1.00, Variance ≈ 1.09
- **Binomial Distribution**: Mean ≈ 4.97, Variance ≈ 2.44
- **Pareto Distribution**: Mean ≈ 0.87, Variance ≈ 3.18

### Section 2: Dice Simulation

- **Objective**: Simulate 1000 dice rolls using different methods and analyze the outcomes.
- **Simulations**:
  - **Uniform Dice Roll**: Using `numpy.random.randint(1, 7, 1000)` to simulate fair dice rolls.
  - **Normal Distribution Dice Roll**: Using `numpy.random.normal(3.5, 1, 1000)`, rounding and clipping the results to fall between 1 and 6.
  - **Poisson Distribution Dice Roll**: Using `numpy.random.poisson(3, 1000)`, then clipping the values to be between 1 and 6.

### Section 3: Increasing the Probability of Six 🎯

- **Objective**: Create a biased (cheating) dice where the face '6' has a higher probability of appearing.
- **Implementation**:
  - Uses `numpy.random.choice()` with specified weights.
  - Example weights: `[0.1, 0.1, 0.15, 0.15, 0.2, 0.3]`
  - **Output**: Percentage distribution of outcomes:
    - 1: 10.50%
    - 2: 10.50%
    - 3: 12.80%
    - 4: 16.60%
    - 5: 19.20%
    - 6: 30.40%

---

## Results

The project outputs include:
- **Histograms** for each probability distribution along with calculated mean and variance values.
- **Dice Roll Simulations**:
  - Uniform dice rolls showing an approximately equal distribution among the 6 faces.
  - Non-uniform dice rolls (using Normal and Poisson distributions) showing variations in frequency.
  - A biased dice simulation where the face '6' appears with a significantly higher probability (30.40%).

---

## Reinforcement Learning Connection

The biased dice simulation is a simplified demonstration related to the **Multi-Armed Bandit Problem** in reinforcement learning:
- **Multi-Armed Bandit Problem**: An agent must choose between multiple options (slot machines) to maximize reward.
- **Relevance**: By altering the probability distribution (or "reward" mechanism) of dice outcomes, one can simulate a scenario where certain actions (choosing a particular face) yield better rewards.
- This foundational understanding is critical in designing and understanding algorithms in reinforcement learning, where the balance between exploration and exploitation is key.

---

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install numpy matplotlib

---

## Requirements

- **Python 3.x**
- **Libraries:**
  - **NumPy**
  - **Matplotlib**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

