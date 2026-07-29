#imports
from PIL import Image
import numpy as np
import mido
from mido import MidiFile, MidiTrack, Message
from io import BytesIO

#Turns the image into 500x500 resolution and turns it into greyscale
def format_image(image_path):

    image = Image.open(image_path)

    resized_image = image.resize((500, 500), Image.LANCZOS)
    final_modified_image = resized_image.convert('L')

    return final_modified_image

#Turns that image data into a mid file by turning the pixel value divided by 2 into the note and the remainder into the velocity + 50 (+ 50 is there to make sure you can hear it)
def turn_to_music(image_data):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)
    track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(140)))

    note = 0
    velocity = 50
    for y in range(500):
        turn_off = []
        for x in range(500):
            if x == 0:
                time = 50
            else:
                time = 0
            pixel_value = image_data[y][x]
            velocity = (pixel_value % 2) + 50
            note = pixel_value // 2
            track.append(Message('note_on', note=note, velocity=velocity, time=time))
            turn_off.append({'note': note, 'velocity': velocity})

        for index, value in enumerate(turn_off):
            if index == 0:
                time = 50
            else:
                time = 0
            track.append(Message('note_off', note=value['note'], velocity=value['velocity'], time=time))

    buffer = BytesIO()
    midi.save(file=buffer)
    buffer.seek(0)

    return buffer

#Decodes the .mid file by turning the notes and velocity value back into the pixel value and making the image with it
def decode_midi_file(mid_file):
    reconstructed_image_data = []
    midi = MidiFile(file=mid_file)
    for track in miditracks:
        for msg in track:
            if msg.type == 'note_on':
                reconstructed_image_data.append((msg.note *2) + (msg.velocity - 50))

    reconstructed_image = Image.new("L", (500, 500), color=0)
    image_pixels = reconstructed_image.load()
    sublists = np.array_split(reconstructed_image_data, 500)
    rows = [list(arr) for arr in sublists]
    column = 0

    for row in rows:
        for index, pixel_value in enumerate(row):
            image_pixels[index, column] = int(pixel_value)
            
        column +=1

    return reconstructed_image

# Final image to music function
def image_to_music(file_path):

    formatted_image = format_image(file_path)
    return turn_to_music(np.array(formatted_image))
