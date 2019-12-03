"""Unit test for force_sensors_code"""
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
