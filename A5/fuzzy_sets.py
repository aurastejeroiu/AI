# left and right boundaries

theta_ranges = {
    'NVB': (None, -25, -40),
    'NB': (-40, -10),
    'N': (-20, 0),
    'Z': (-5, 5),
    'P': (0, 20),
    'PB': (10, 40),
    'PVB': (25, None, 40)
}

omega_ranges = {
    'NB': (None, -3, -8),
    'N': (-6, 0),
    'Z': (-1, 1),
    'P': (0, 6),
    'PB': (3, None, 8)
}

force_ranges = {
    'NVVB': (None, -24, -32),
    'NVB': (-32, -16),
    'NB': (-24, -8),
    'N': (-16, 0),
    'Z': (-4, 4),
    'P': (0, 16),
    'PB': (8, 24),
    'PVB': (16, 32),
    'PVVB': (24, None, 32)
}

weights = {  # b values
    'NVVB': -32,
    'NVB': -24,
    'NB': -16,
    'N': -8,
    'Z': 0,
    'P': 8,
    'PB': 16,
    'PVB': 24,
    'PVVB': 32}

rules_table = {
    'PVB': {'NB': 'P', 'N': 'PB', 'Z': 'PVB', 'P': 'PVVB', 'PB': 'PVVB'},
    'PB': {'NB': 'Z', 'N': 'P', 'Z': 'PB', 'P': 'PVB', 'PB': 'PVVB'},
    'P': {'NB': 'N', 'N': 'Z', 'Z': 'P', 'P': 'PB', 'PB': 'PVB'},
    'Z': {'NB': 'NB', 'N': 'N', 'Z': 'Z', 'P': 'P', 'PB': 'PB'},
    'N': {'NB': 'NVB', 'N': 'NB', 'Z': 'N', 'P': 'Z', 'PB': 'P'},
    'NB': {'NB': 'NVVB', 'N': 'NVB', 'Z': 'NB', 'P': 'N', 'PB': 'Z'},
    'NVB': {'N': 'NVVB', 'Z': 'NVB', 'P': 'NB', 'PB': 'N', 'NB': 'NVVB'}}
