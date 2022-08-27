import winsound
import time

    
bpm = input ('Please enter tempo')
bps = int(bpm) / 60
spb = 1/bps
time_beep = spb * 0.25
time_next = spb * 0.75

while True:
   
    
    winsound.Beep(1000, round(time_beep*1000))  
   
    time.sleep (time_next )
    

#reactor.callLater(0 / bps, beat, bpm / 4, beat_start)
#reactor.callLater(1 / bps, beat, bpm / 4, beat_start)
#reactor.callLater(2 / bps, beat, bpm / 4, beat_start)
#reactor.callLater(3 / bps, beat, bpm / 4, beat_end)

#reactor.run()