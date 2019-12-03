# Forces in Newtons, voltages in Volts.
# To test, run
# $ python force_sensors_code.py SENSOR_ID
force_sensors = {
    'DUMMY': {
        'forces':   [1, 2, 3, 4, 5],
        'voltages': [1, 2, 3, 4, 5]
    },
    'C300510': {
        'forces':   [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
        'voltages': [0.65, 1.31, 2.01, 2.80, 3.79, 4.92]
    },
    'C300511': {
        'forces':   [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
        'voltages': [0.64, 1.37, 2.03, 2.84, 3.75, 4.97]
    },
    'C401423': {
        'forces':   [1.01, 2.00, 3.05, 3.98, 5.03, 6.04],
        'voltages': [0.53, 1.07, 1.62, 2.14, 2.78, 3.57]
    },
    'C401424': {
        'forces':   [1.01, 2.00, 3.05, 3.98, 5.03, 6.04],
        'voltages': [0.65, 1.32, 2.00, 2.74, 3.39, 4.25]
    },

}

# Response is scaled at lowest frequency. See base response for mV/Pa.
# To test, run
# $ python microphone_code.py MIC_ID
microphones = {
    'NGY0543': {
        'frequency': [100,   200,   300,   400,   500,   600,   700,   800,   900,  1000],
        'response':  [  1,  1.05,  1.07,  1.25,  5.04,  2.21,  0.93,  0.63,  0.27,  0.11],
        'phase':     [  0, -0.01, -0.05, -0.17, -0.54, -1.45, -2.56, -3.00, -3.05, -3.12],
        'base_response': 0.276
    }
}
