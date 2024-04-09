END_OF_TRACK = "end_of_track"
NOTE_ON = 'note_on'
NOTE_OFF = 'note_off'

# MAGENTA MAPPING
ROLAND_REDUCED_MAPPING = {
    "KICK": [36],
    "SNARE": [38, 37, 40],
    "HH_CLOSED": [42, 22, 44],
    "HH_OPEN": [46, 26],
    "TOM_3_LO": [43, 58],
    "TOM_2_MID": [47, 45],
    "TOM_1_HI": [50, 48],
    "CRASH": [49, 52, 55, 57],
    "RIDE":  [51, 53, 59]
}

PERC_VOICES_MAPPING = {
    'KICK' : ROLAND_REDUCED_MAPPING["KICK"] + [35],
    'SNARE' : ROLAND_REDUCED_MAPPING["SNARE"],
    'HH' : ROLAND_REDUCED_MAPPING["HH_CLOSED"] + ROLAND_REDUCED_MAPPING["HH_OPEN"],
    'TOM' : ROLAND_REDUCED_MAPPING["TOM_3_LO"] + ROLAND_REDUCED_MAPPING["TOM_2_MID"] + ROLAND_REDUCED_MAPPING["TOM_1_HI"],
    'CRASH' : ROLAND_REDUCED_MAPPING["CRASH"],
    'RIDE' : ROLAND_REDUCED_MAPPING["RIDE"] + [56]
}
