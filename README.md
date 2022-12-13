# pianoizer : Reconstitute a complete piano "sheet" from a live piano playing video (eg. Synthesia)

This Jupyter Notebook/Python script will reconstitute the full piano "sheet" used on a live playing video (such as the ones available on YouTube), so you can have it on one image, play it offline and eventually print it, to better practice and impress on opportunities with your fraudulent skills :p

## Usage

If the video comes from YouTube, download it with a tool like youtube-dl in MP4 and fill its filename at the 5th script line.
Run it one time without any config and use the preview.png image (taken at 7th second by default) to find the scrolling piano sheet zone's coordinates as it can't be detected automatically, and fill them instead of default ```x1=0, y1=5, x2=640, y2=170```.
Then fill the following parameters:
```
Example: pianoize(6,2.25,200):

start = 6 #when the piano playing starts (seconds)
interval = 2.25 #at what interval the notes in one given frame are finished to be played, can be found by trial (seconds)
length = 200 #how much intermediary sheets (frame files) you would like to be considered for generating the sheet
```
