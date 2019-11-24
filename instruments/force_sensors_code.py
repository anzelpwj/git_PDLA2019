"""Some basic routines for working with the force sensors."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.interpolate import CubicSpline
import sys
from calibrations import force_sensors as FORCE_SENSORS


def plot_force_sensor(sensor_id):
    """Generates a plot of the force/voltage response curve for a force sensor.

    Inputs:
        sensor_id (str): Serial number of force sensor.
    """
    try:
        data = FORCE_SENSORS[sensor_id]
    except:
        raise ValueError(
            "Unknown sensor ID %s provided, available sensors in calibrations.py"
            % sensor_id)
    forces = np.array(data['forces'])
    voltages = np.array(data['voltages'])
    slope, _, _, _, _ = linregress(voltages, forces)

    spline_x = np.linspace(0, max(voltages))
    spline_y = get_force_for_voltage(spline_x, sensor_id)

    plt.figure(figsize=(5, 5), dpi=150)
    plt.scatter(forces, 1000*voltages, color='k', marker='o')
    plt.plot(spline_x, 1000*spline_y, color='k', linewidth=2, linestyle="--")
    plt.title("Sensor {device}, {factor:.2e} N/V".format(device=sensor_id, factor=slope), fontsize=16)
    plt.xlabel("Force [N]", fontsize=16)
    plt.ylabel("Voltage [mV]", fontsize=16)


def get_force_for_voltage(voltages, sensor_id):
    """Gets the force for a given voltage with a particular device. Uses cubic interpolation.
    
    Inputs:
        voltage (float or float array): Voltage response.
        sensor_id (str): Device serial number.
    Outputs:
        force (float or float array): Estimated force.
    """
    try:
        data = FORCE_SENSORS[sensor_id]
    except:
        raise ValueError(
            "Unknown sensor ID %s provided, available sensors in calibrations.py"
            % sensor_id)
    spline = CubicSpline(data['voltages'], data['forces'], bc_type='not-a-knot')
    return spline(voltages)


if __name__ == '__main__':
    sensor = sys.argv[1]
    plot_force_sensor(sensor)
