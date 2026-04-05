# Activity 1: Algorithms & Complexity 2526

This assignment consists on solving two divide-and-conquer type of problems through efficient implementations in Python.

You will need to use the `algodredd` command line tool to automatically evaluate your solutions over a given set of instances.

**NOTE**: Although you could develop the assignment in any OS, you will need to run **Linux** to evaluate your solutions using `algodredd`.
For any issue, please contact me.

In this document you will find the following information:

- The project structure.
- A description for the problems that you will solve and their score.
- How to use the `algodredd` tool to evaluate your solutions and automatically deliver the project.

The main goal of this project is to provide efficient implementations for the proposed problems, such that **they output correct solutions** and they are **comparatively equals or better** in terms of running time than the provided solutions.

**WARNING!** This assignment will be automatically evaluated using the `algodredd` tool. Make sure you follow all the steps described in this document before submitting your solution.
**A project that cannot be automatically evaluated will receive a score of 0.**

# Project Structure

This project has the following structure:

```
students/
├── assignment.json
├── group.json
├── gen-mut
│   ├── instances
│   │   ├── easy
│   │   │   ├── inst-s10-cluster.txt.bz2
│   │   │   └── ...
│   │   └── hard
│   │       ├── inst-s100000-cluster.txt.bz2
│   │       └── ... 
│   ├── problem.json
│   ├── solution.py
│   ├── solutions
│   │   ├── alg1.bin
│   │   └── alg2.bin
│   └── validator.bin
└── sorting
    ├── instances
    │   ├── easy
    │   │   ├── inst-s100-partial.txt.bz2
    │   │   └── ...
    │   └── hard
    │       ├── inst1-s1000000-partial.txt.bz2
    │       └── ...
    ├── problem.json
    ├── solution.py
    ├── solutions
    │   ├── alg2.bin
    │   └── alg3.bin
    └── validator.bin
```

The problems that you must solve are within the `students/gen-mut` and `students/sorting` directories.

# Problems Descriptions

## Problem 1: The *Sorting* Problem

At this point, you should be already familiar with the sorting problem. Given an array of numbers, the sorting problem asks for a sorted array **in ascending order** of the same numbers.
For more information, you can check the subject slides.

You must implement your solution in the `students/sorting/solution.py` file.
In the following, we describe the instances format and the output format that you must use in your solution.

### Input Format

Instances are located in the `students/sorting/instances` directory.
There are two kinds of *instances sets*: the *easy* ones and the *hard* ones.

Each instance is copressed in the `.bz2` format.
To inspect an instance, you can run:

```bash
bzcat students/sorting/instances/easy/inst-s10-partial.txt.bz2
```

Which should show:

```
[1, 11, 47, 74, 92, 87, 78, 97, 22, 2]
```

### Output Format

Your solution must print an space-separated list corresponding to the sorted version in ascending order of the input array.

For the example above, the output should be:

```
1 2 11 22 47 74 78 87 92 97
```

### Your Implementation

You are provided with the `students/sorting/solution.py` file, where you must implement your solution.
You already have all the necessary imports and a `main` function that reads the input and prints the output using the described formats, so **you should not change anything of this part**.

Instead, you should just implement the `my_sort(arr)` function, which takes a list of numbers as input and returns a sorted list of numbers.

This is the full code that you have available for the `students/sorting/solution.py` file:

```python
import argparse
import bz2
import json
import sys
from pathlib import Path


def my_sort(arr):
    raise NotImplementedError("Implement Me!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=Path,
        help="Path to input .bz2 file containing JSON array of integers",
    )
    args = parser.parse_args()

    # Load instance
    try:
        with bz2.open(args.input, "rb") as f:
            data = json.load(f)
    except Exception as e:
        sys.exit(f"Error loading instance: {e}")

    if not isinstance(data, list):
        sys.exit("Invalid instance format: expected a JSON list")

    sorted_arr = my_sort(data)

    # Print result to standard output (space-separated)
    print(*(sorted_arr))


if __name__ == "__main__":
    main()
```

### Provided Solutions and Validator

There are two provided solutions for this problem, located in the `students/sorting/solutions` directory.
These are Python implementations, but the code is obfuscated, so you should not be able to understand the algorithm used.

Nonetheless, you can easily run any of the algorithms as shown:

```
./students/sorting/solutions/alg2.bin students/sorting/instances/easy/inst-s10-partial.txt.bz2 
```

Which should output:

```
1 2 11 22 47 74 78 87 92 97
```

This way, you can easily compare your solution with the provided solutions and *visually* check if they are correct.

Aside, you are provided with a `students/sorting/validator.bin` file, which is a validator for the sorting problem. You can use it to check if your solution is correct as shown:

```bash
# First, we need to store the output of the algorithm in a file
./students/sorting/solutions/alg2.bin students/sorting/instances/easy/inst-s10-partial.txt.bz2 > solution.txt

# Then, we can use the validator to check if the solution is correct
./students/sorting/validator.bin students/sorting/instances/easy/inst-s10-partial.txt.bz2 solution.txt
```

This should output the following:

```
Correctness verified via manual property check (sorted and valid permutation).
```

Instead, if the provided instance is incorrect, the validator will output the following:

```bash
cat wrong.txt

2 11 22 47 74 78 87 92 97 1
```

```bash
./students/sorting/validator.bin students/sorting/instances/easy/inst-s10-partial.txt.bz2 wrong.txt
```

This should output the following:

```
Incorrect: The array is not sorted.
```

**NOTE**: You can replace `alg2.bin` by any of the algorithms in the `students/sorting/solutions` directory, or by the execution of your own solution.

### Scoring

This exercise has an score of **5 points**, which will be obtained under the following conditions:

- Your solution outputs a correct solution **for all the instances**.
- You did not use any of the `sort` methods implemented in Python (i.e., that's cheating).
- Your solution is efficient enough to pass the time limits **for all the instances**.
- Your solution is general, i.e., it does not use any hardcoded values for the instances.

If any of the previous conditions is not met, **your score for this part will be 0**.
Otherwise, your score will be calculated as follows:

- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg2.bin` for the *hard* instances.
- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg3.bin` for the *hard* instances.
- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg2.bin` for a *private holdout* set of instances.
- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg3.bin` for a *private holdout* set of instances.

At the end, we will normalize your score over 5 points.

**NOTE:** We understand *comparatively equals or better* if there is a difference of at most 10% in the running time w.r.t. the provided solutions.

## Problem 2: The *Genetic Mutation Similarity* Problem

We are working in a biotech company that is interested in studying the effects of mutations in the DNA of a certain species.
To this end, we will study data points containing the *binding affinity* ($ba$) of the mutation, which is a measure of how strongly the mutation binds to a certain protein, as well as the *expression level* ($el$) of the gene, which is a measure of how much the gene is expressed.

For us, future computer scientiest whose latest class of biology was about the parts of the cell, both $ba$ and $el$ are just numbers.
Our boss, who is a biologist, is interested in finding the two most similar mutations in terms of these two factors.
She tells us that the *distance* of two mutations is given by the following formula:

$$dist(m_1, m_2) = \sqrt{(ba_1 - ba_2)^2 + (el_1 - el_2)^2}$$

The *lower* this distance is, the *closer* the two mutations are.

Our goal is to design and implement and **efficient** algorithm that finds the two most similar mutations.

### Input Format

As in the *Sorting* problem, instances are located in the `students/gen-mut/instances` directory, and there are two kinds of *instances sets*: the *easy* ones and the *hard* ones.

Each instance is also copressed in the `.bz2` format.
To inspect an instance, you can run:

```bash
bzcat students/gen-mut/instances/easy/inst-s4.txt.bz2
```

Which should show:

```
170.82180461559483 395.0827754293611
171.2889071849961 61.80807262855603
522.2135689105876 598.035723180015
43.83998991411775 11.272338430249995
```

Each line contains two numbers corresponding to a mutation.
The first number is the binding affinity ($ba$) and the second one is the expression level ($el$).

### Output Format

You will need to output the minimal distance between any two mutations, and the two mutations that achieve this minimal distance.

For example, if the input is:

```
170.82180461559483 395.0827754293611
171.2889071849961 61.80807262855603
522.2135689105876 598.035723180015
43.83998991411775 11.272338430249995
```

The output should be:

```
137.10246877602546
171.2889071849961 61.80807262855603
43.83998991411775 11.272338430249995
```

The first line corresponds to the minimal distance, and the second and third lines to the two mutations that achieve this minimal distance.

### Your Implementation

You are provided with the `students/gen-mut/solution.py` file, where you must implement your solution.
As with the *Sorting* problem, you already have all the necessary imports and a `main` function that reads the input and prints the output using the described formats, so **you should not change anything of this part**.

Instead, you should just implement the `my_gen_mut_algorithm(points)` function, which takes a list of points as input and returns the minimal distance between any two points, and the two points that achieve this minimal distance.

This is the full code that you have available for the `students/gen-mut/solution.py` file:

```python
import argparse
import bz2
import sys
import math
from pathlib import Path


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def my_gen_mut_algorithm(points):
    raise NotImplementedError("Implement Me!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Input .bz2 file")
    args = parser.parse_args()

    try:
        with bz2.open(args.input, "rb") as f:
            content = f.read().decode("utf-8")
    except Exception as e:
        sys.exit(f"Error loading instance: {e}")

    points = []
    for line in content.splitlines():
        if line.strip():
            points.append(list(map(float, line.split())))

    if len(points) < 2:
        print(0.0)
    else:
        d, pair = my_gen_mut_algorithm(points)
        print(d)
        print(f"{pair[0][0]} {pair[0][1]}")
        print(f"{pair[1][0]} {pair[1][1]}")


if __name__ == "__main__":
    main()
```

### Provided Solutions and Validator

There are two provided solutions for this problem, located in the `students/gen-mut/solutions` directory.
As with the *Sorting* problem, these are Python implementations, but the code is obfuscated, so you should not be able to understand the algorithm used.

Nonetheless, you can easily run any of the algorithms as shown:

```
./students/gen-mut/solutions/alg2.bin students/gen-mut/instances/easy/inst-s4.txt.bz2 
```

Which should output:

```
137.10246877602546
43.83998991411775 11.272338430249995
171.2889071849961 61.80807262855603
```

This way, you can easily compare your solution with the provided solutions and *manually* check if they are correct.

Aside, you are provided with a `students/gen-mut/validator.bin` file, which is a validator for the *gen-mut* problem. You can use it to check if your solution is correct as shown:

```bash
# First, we need to store the output of the algorithm in a file
./students/gen-mut/solutions/alg2.bin students/gen-mut/instances/easy/inst-s4.txt.bz2 > solution.txt

# Then, we can use the validator to check if the solution is correct
./students/gen-mut/validator.bin students/gen-mut/instances/easy/inst-s4.txt.bz2 solution.txt
```

This should output the following:

```
Correct: Verified distance 137.10246877602546 in O(n) using spatial grid.
```

Instead, if the provided instance is incorrect, the validator will output the following:

```bash
cat wrong.txt

640.8496012506822
171.2889071849961 61.80807262855603
522.2135689105876 598.035723180015
```

```bash
./students/gen-mut/validator.bin students/gen-mut/instances/easy/inst-s4.txt.bz2 wrong.txt
```

This should output the following:

```
Incorrect: Found closer pair (171.2889071849961, 61.80807262855603), (170.82180461559483, 395.0827754293611) with distance 333.27503013543526.
```

**NOTE**: You can replace `alg2.bin` by any of the algorithms in the `students/gen-mut/solutions` directory, or by the execution of your own solution.

### Scoring

This exercise has an score of **5 points**, which will be obtained under the following conditions:

- Your solution outputs a correct solution **for all the instances**.
- Your solution is efficient enough to pass the time limits **for all the instances**.
- Your solution is general, i.e., it does not use any hardcoded values for the instances.

If any of the previous conditions is not met, **your score for this part will be 0**.
Otherwise, your score will be calculated as follows:

- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg1.bin` for the *hard* instances.
- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg2.bin` for the *hard* instances.
- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg1.bin` for a *private holdout* set of instances.
- 1 point for each instance where your solution is **comparatively equals or better** in terms of running time than `alg2.bin` for a *private holdout* set of instances.

At the end, we will normalize your score over 5 points.

**NOTE:** We understand *comparatively equals or better* if there is a difference of at most 10% in the running time w.r.t. the provided solutions.

# The `algodredd` Tool

You will receive within the assignment files a binary called `algodredd`. This tool will be used to evaluate and deliver your solutions.

As we stated before, `algodredd` **only works in a Linux system**. In case you are not using Linux, you can use a virtual machine, a Docker container, a *devcontainer* or WSL (Windows Subsystem for Linux) to run `algodredd`.

If you run `algodredd` without passing any parameters you will obtain a help message with the available commands and options:

```
Usage: algodredd <command> [arguments]
Commands:
  run     <solution.py> [set] [-p N]   Run solution against public instances (or a specific set) with N parallel workers
  deliver <assignment_dir>             Package solutions into a delivery zip
```

## Evaluating Your Solutions

The `algodredd run` command allows you to run your solution against the public instances. 
Its parameters are:

- `<solution.py>`: The path to your solution file.
- `[set]`: The set of instances to run against. If not specified, it runs against all the public instances.
- `[-p N]`: The number of parallel workers to use. If not specified, it uses 1 worker.

For example, to run your *Sorting* solution against the *easy* set of instances with 4 parallel workers, you would use the following command:

```bash
./algodredd run students/sorting/solution.py easy -p 4
```

This should output something similar to this:

```
Running solution: students/sorting/solution.py

RESULTS for Problem: sorting
Total Score: 0

[inst-s10-partial.txt] Status: RTE
  Time: 0.030s, Memory: 13024KB
  Reference Comparison:
    alg2.bin: Time=0.074s, Mem=23948KB
    alg2.bin_mem_ratio: 0.5438449974945716
    alg2.bin_time_ratio: 0.40509284249163335
    alg3.bin: Time=0.063s, Mem=23876KB
    alg3.bin_mem_ratio: 0.5454850058636288
    alg3.bin_time_ratio: 0.4746237035163167

  ...

SUMMARY
============================================================
Solution                  Avg Time   Min Time   Max Time   Success   
------------------------------------------------------------
solution.py               0.028     s 0.022     s 0.032     s 0.0       %
alg2.bin                  0.072     s 0.064     s 0.077     s 100.0     %
alg3.bin                  0.062     s 0.040     s 0.070     s 100.0     %
============================================================
```

Notice that these numbers may change depending on your PC.

In this case, the **Status** for the *inst-s10-partial.txt* instance is **RTE** (Runtime Error). This is expected, as the provided solution is not correct.
The list of possible statuses is:

- **AC**: Accepted
- **WA**: Wrong Answer
- **TLE**: Time Limit Exceeded
- **RTE**: Runtime Error
- **ERR**: Internal Error
- **THE**: Threshold Exceeded

Only **AC** means that your solution is correct and efficient enough to pass the time limits.
Otherwise, the execution will be considered a failure.

**NOTE:** `algodredd` uses a cache to store the execution results for the reference solutions (i.e., `alg1.bin`, `alg2.bin`...) to speed up the evaluation process. 
You might find that the first execution of the `algodredd run` command is slower than the subsequent ones. This is expected behavior.
In case you have any issues with this cache, you can remove the `.ref_cache.json` file, which is contained at each of the problems' folders.

## Automatic Project Delivery

`algodredd` also provides an utility to pack your solutions into a zip file, which will be used to deliver your solutions to the grading system in the proper expected format, so you will not need to create it by yourself.

Before running this command, you must complete the `group.json` file with your group information.
In particular, you must provide:

- "name": Your name and surnames.
- "id": Your student ID as it appears in the Virtual Campus.
- "dni": You DNI number (including the letter).

If you are a group of 2 students, you must fill the information for both students in the `group.json` file.
In case you are a group of 1 student, you must fill the information for only one student in the `group.json` file, leaving blank the information for the second student.

Once completed, you can run the `algodredd deliver` command. Its parameters are:

- `<assignment_dir>`: The path to the assignment directory.

This will create a `.zip` file in the `<assignment_dir>` folder, which you will have to submit through the Virtual Campus platform.

In case you are a group of 2 students, **only one of the members** should deliver the solution.
Make sure to include **both** students' information in the `group.json` file.

