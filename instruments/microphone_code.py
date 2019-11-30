"""Some basic routines for working with microphones."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.interpolate import CubicSpline
import sys
from calibrations import microphones as MICROPHONES
def plot_microphone_transfer_function(microphone_id):
    try:
        data = MICROPHONES[sensor_id]
    except:
        raise ValueError(
            "Unknown microphone ID %s provided, available devices in calibrations.py"
            % sensor_id)
    frequencies=np.array(data['frequency'])
    responses=np.array(data['response'])
    phase= np.array(data['phase'])

    XVals = np.linspace(min(frequencies), max(frequencies))
    spline_yr = CubicSpline(frequencies, responses, bc_type='not-a-knot')
    spline_yp = CubicSpline(frequencies, phase, bc_type='not-a-knot')
    yvals_resp = spline_yr(XVals)
    yvals_resp = spline_yp(XVals)

    fig, ax = plt.subplots(nrows=2, ncols=1, figsize(5, 5), dpi=150)
    ax[0].scatter(frequencies, responses,color="k",marker='o')
    ax[0].plot(XVals, yvals_resp, color="k", linewidth=2, linestyle="--")
    ax[0].ylabel("Response [mV/Pa]", fontsize=16)
    ax[0].scatter(frequencies, responses, color="k", marker='o')
    ax[0].plot(XVals, yvals_phase, color="k", linewidth=2, linestyle="--")
    ax[0].ylabel("Phase [rad]", fontsize=16)
    ax[0].xlabel("Frequency [Hz]", fontsize=16)
    fig.suptitle("Transfer function for mic %s" % microphone_id, fontsize=16)
    plt.show()


if __name__ == '__main__':
    sensor = sys.argv[1]
    plot_force_sensor(sensor)
