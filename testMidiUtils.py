from helpers import *
from constants import *

import mido

def testMergeTracks():
    mid1 = mido.MidiFile(f"{TEST_SOURCE_DIR}/test0.mid")
    mid2 = mido.MidiFile(f"{TEST_SOURCE_DIR}/test1.mid")
    mid3 = mido.MidiFile(f"{TEST_SOURCE_DIR}/test2.mid")
    mid4 = mido.MidiFile(f"{TEST_SOURCE_DIR}/test3.mid")
    track1 = mid1.tracks[0]
    track2 = mid2.tracks[0]
    track3 = mid3.tracks[0]
    track4 = mid4.tracks[0]

    tracks = [track1, track2, track3, track4]
    
    newMid = mido.MidiFile(ticks_per_beat=mid1.ticks_per_beat)
    newMid.tracks.append(mergeMultipleTracks(tracks))
    newMid.save(f"{TEST_OUTPUT_DIR}/merge.mid")

def testSplitIntoBars():
    mid = mido.MidiFile(f"{TEST_SOURCE_DIR}/whole.mid")
    track = mid.tracks[0]       
            
    sliceLen = mid.ticks_per_beat * 4 * 1

    newTrack = getMidiSlice(track=track, startTime=sliceLen*1, endTime=sliceLen*2)

    newMid = mido.MidiFile(ticks_per_beat=mid.ticks_per_beat)
    newMid.tracks.append(newTrack)      
    newMid.save(f"{TEST_OUTPUT_DIR}/split.mid")       

def testSeparateIntoPitches():
    mid = mido.MidiFile(f"{TEST_SOURCE_DIR}/test0.mid")
    track = mid.tracks[0]


    pitches = [51, 44, 36]
    newTrack = separateIntoPitches(track, pitches)

    newMid = mido.MidiFile(ticks_per_beat=mid.ticks_per_beat)
    newMid.tracks.append(newTrack)
    newMid.save(f"{SPLIT_DIR}/separatePitches.mid")

def testDeletePitches():
    mid = mido.MidiFile(f"{TEST_SOURCE_DIR}/test0.mid")
    track = mid.tracks[0]

    pitches = [36,42]

    newTrack = deletePitches(track, pitches)
    mid = mido.MidiFile(ticks_per_beat=mid.ticks_per_beat)
    mid.tracks.append(newTrack)
    mid.save(f"{TEST_OUTPUT_DIR}/deletePitches.mid")

def testGetTrackWithoutBeginningMetadata():
    mid = mido.MidiFile(f"{TEST_SOURCE_DIR}/test0.mid")
    track = mid.tracks[0]
    print(track)

    newTrack = getTrackWithoutBeginningMetaData(track)
    print(newTrack)
    
def testConcatenateTracks():
    mid0 = mido.MidiFile(f"{TEST_SOURCE_DIR}/test0.mid")
    mid1 = mido.MidiFile(f"{TEST_SOURCE_DIR}/test1.mid")

    track0 = mid0.tracks[0]
    track1 = mid1.tracks[0]

    newTrack = concatenateTracks(track0, track1)
    mid = mido.MidiFile(ticks_per_beat=mid0.ticks_per_beat)
    mid.tracks.append(newTrack)
    mid.save(f"{TEST_OUTPUT_DIR}/concatenate.mid")

def testEndTime():
    mid = mido.MidiFile(f"{TEST_SOURCE_DIR}/1_rock_110_beat_4-4_slice_208.mid")
    track = mid.tracks[0]
    
    beats = 4
    bars = 2

    expectedEndTime = (mid.ticks_per_beat * beats * bars) - 1
    actualEndTime = getEndTime(track)

    assert expectedEndTime == actualEndTime, f"expectedEndTime = {expectedEndTime}, actualEndTime = {actualEndTime}"
    
    print(f"Success!! expectedEndTime: {expectedEndTime}, actualEndTime: {actualEndTime}")

if __name__ == "__main__":
    # testMergeTracks()
    # testSplitIntoBars
    # testSeparateIntoPitches()
    # testDeletePitches()
    # testGetTrackWithoutBeginningMetadata()
    # testConcatenateTracks()
    testEndTime()