import tables
import os

MSD = './MillionSongSubset'

def dig(path):
    """
    returns list of all HDF5 files in every recursive subdirectory in a given parent dir
    """
    files = []
    for _, _, files in os.walk(path):
        files += [f for f in files if f.endswith(".h5")]
    return files

# Function to extract audio features from an HDF5 file
def get_features(h5_file):
    with tables.open_file(h5_file, mode='r') as h5:
        # Access different data fields within the HDF5 file
        audio_features = h5.root.analysis.songs.cols
        # Extract the features you need (e.g., loudness, tempo)
        loudness = audio_features.loudness[0]
        tempo = audio_features.tempo[0]
        # You can extract more features as required

        return loudness, tempo

def main():
    files = dig(MSD)
    loud, temp = get_features(files[0])
    print(loud, temp)
# h5_files = [os.path.join(msd, f) for f in os.listdir(msd) if f.endswith('.h5')]
# print(h5_files)
# loudness, tempo = extract_audio_features(h5_files[0])
# print(f'Loudness: {loudness}, Tempo: {tempo}')
