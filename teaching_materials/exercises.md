# Exercises for tutorial attendees

## Exercise 1: Merge conflict

In order to build some unit tests for code, you've decided to add a dummy force sensor to the devices at `calibrations.py`. Please add the following code to the beginning of the force sensors block (starting at line 5).

```python
    'DUMMY': {
        'forces':   [1, 2, 3, 4, 5],
        'voltages': [1, 2, 3, 4, 5]
    },
```

Instructor will then try to add his own version of a dummy sensor at the same place, creating a merge conflict.

## Exercise 2: Opening a branch

We're going to try to take a similar approach for the microphone code, but this time we will create a branch to add a new sensor to as to be more careful against merge conflicts. Create a branch on your system, give it a good name (we'll all get to see it, so keep it professional...), and please add the following code block the beginning of the microphones dictionary in `calibrations.py`.

```python
    'DUMMY': {
        'frequency': [2, 4, 6, 8],
        'response':  [1, 1, 1, 1],
        'phase':     [0, 0, 0, 0],
        'base_response': 1
    },
```

Once you're done, please push your branch to GitHub (command `git push origin BRANCHNAME`).

## Exercise 3: Opening a Pull Request

Taking the branch opened in exercise 2, create a Pull Request for the branch back to master. Tag me (username `anzelpwj`) in it.

## Exercise 4: Doing code review

We'd like to add some code that plots a transfer function for our microphones, much like our force-voltage plots for the force sensors. We're going to create a PR for the branch `exercises/microphone_code` together. I will make the PR, we will do review in the tutorial.

## Exercise 5a: Creating an issue

Our instrument lab control code is completely untested! This will not do. Please submit a issue in the repo that we need to fix this problem.

## Exercise 5b: Fixing the issue

A branch to fix our issue has been created at `exercises/force_sensors_unit_test`. Please open a pull request, refer to the issue number, and tag me as a reviewer.
