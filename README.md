# Custom Image to Music Steganography

Hi! My name is Aryan; I'm 14 years old, and I made this project for fun and [this](https://ispy.hackclub.com/)
program where the primary goal is to make a project and have fun. The theme of this project is some sort of 
spyware, hence this. 

The primary base of the website is that it can convert an image into music, and reverse it.
This is a type of steganography which can be used to hide info. 

You can check out the website [here](https://image-to-music-steganography.streamlit.app/)

---

# How it works :)

If you are curious about how this works, here's how:

Encoding:

First, it formats the image to a 500x500 resolution and turns it into grayscale. 
Now, to turn it into music, we make a .mid file. We get each pixel's value, divide it by 2, and get the remainder,
since it needs to be between 0 and 127 for the note value. The remainder + 50 (+50 to be able to actually hear it) 
is the value of the velocity for the .mid file. Now we just start each row's notes at once, 
with a slight delay between each row.
That's how I encoded the image data into music.

Decoding:

First I made a black 500x500 canvas using Pillow.
Next, I get the .mid file and read it using mido. I get the note value and velocity value for each note. Then I just reverse the process of encoding. I get the velocity value and subtract 50 from it, then add it to the note value, which has been multiplied by 2. This gives me the pixel value for that note. I get the x and y coordinates by just seeing where it's in the file,e like at the start or at the end. 

Then finally I split the pixel values list into 500 lists of 500 values each, and then I use Pillow to draw the image on the canvas.


That's how I did it! This way seemed the easiest and the best method to me, so yeah! That's how it works, and maybe star this repo if you liked it! I would really appreciate it!
