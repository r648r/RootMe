Forensic : 

ch21
tshark -r "$PCAP_FILE" -Y "dns" -T fields -e frame.time_epoch -e dns.id -e dns.qry.name | awk '!seen[$2]++ { print $3 }' | tr -d '.' | sed 's/^.\{18\}//' | sed 's/.*89504e470d0a1a0a/89504e470d0a1a0a/' | xxd -r -p | pngcheck -v
File: stdin (187650507276352 bytes)
  chunk IHDR at offset 0xfffffffffffffffb, length 13
    640 x 480 image, 32-bit RGB+alpha, non-interlaced
  chunk bKGD at offset 0xfffffffffffffffb, length 6
    red = 0x00ff, green = 0x00ff, blue = 0x00ff
  chunk pHYs at offset 0xfffffffffffffffb, length 9: 2835x2835 pixels/meter (72 dpi)
  chunk tIME at offset 0xfffffffffffffffb, length 7: 27 Jun 2017 08:56:06 UTC
  chunk tEXt at offset 0xfffffffffffffffb, length 25, keyword: Comment
  chunk IDAT at offset 0xfffffffffffffffb, length 6777
    zlib: deflated, 32K window, maximum compression
  chunk IEND at offset 0xfffffffffffffffb, length 0
No errors detected in stdin (7 chunks, 190844989.6% compression).
