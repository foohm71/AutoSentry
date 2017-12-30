cat capture-* | avconv -y -f image2pipe -c:v mjpeg -i - -r 25 -b 65536k -s vga video.mp4
