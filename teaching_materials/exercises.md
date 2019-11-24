# Exercises for tutorial attendees

## Exercise 1: Merge conflict

### Person 1

In order to build some unit tests for code, you've decided to add a dummy force sensor to the devices at `calibrations.py`. Please add the following code to the beginning of the force sensors block (starting at line 5).

```python
    'DUMMY': {
        'forces':   [1, 2, 3, 4, 5],
        'voltages': [1, 2, 3, 4, 5]
    },
```

Instructor will then try to add his own version of a dummy sensor at the same place, creating a merge conflict.

## Exercise 2: Opening a branch

We're going to try to take a similar approach for the microphone code, but this time we will create a branch to add a new sensor to as to be more careful against merge conflicts. Create a branch on your system, give it a good name (we'll all get to see it, so keep it professional...), and please add the following code block at line 28 of `calibrations.py`.

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

Taking the branch opened in exercise 2, create a Pull Request for the branch back to master. Tag me (user name `anzelpwj`) in it.

## Exercise 4: Doing code review

I'm going to submit a pull request (copying the code from `./teaching_materials/sample_microphone_code.py`), and we're going to do code review of this together.

## Exercise 5a: Creating an issue

Our instrument lab control code is complete untested! This will not do. Please submit a ticket that we need to fix this problem.

## Exercise 5b: Fixing the problem

Create a unit test for `force_sensor_code.py:get_force_for_voltage`, put it in a branch, and open a pull request for the code. An example may be a file with:

```python
import numpy as np
from force_sensors_code import get_force_for_voltage

def test_get_force_for_voltage():
    voltages = np.array([1.5, 2.5])

    expected_forces = np.array([1.5, 2.5])
    forces = get_force_for_voltage(voltages, 'DUMMY')
    np.testing.assert_allclose(forces, expected_forces)

if __name__ == '__main__':
    test_get_force_for_voltage()
    print("TESTS COMPLETE!")
```
