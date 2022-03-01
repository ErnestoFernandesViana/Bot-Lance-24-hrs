import pyautogui as rpa
import time
import lance_functions as ls


answer = input('What region? (nw,ne,sw,se)')
possible_answers = {'nw':0,'ne':0,'sw':0,'se':0}
possible_answers[answer] = 1

down_arrow = 950,1031  #had to click 27 times
#boxes to be localized
nw_box = ls.box(177,159,295,218)
ne_box = ls.box(646,158,766,220)
sw_box = ls.box(179,808,294,868)
se_box = ls.box(647,808,765,865)
#recognitions's frames to locate
nw_box_frame = ls.box_frame(nw_box)
ne_box_frame = ls.box_frame(ne_box)
sw_box_frame = ls.box_frame(sw_box)
se_box_frame = ls.box_frame(se_box)
warning_frame = (380, 600, 150, 100)
#stake buttons(lance)
nw_stake = 235,331
ne_stake = 709,328
sw_stake = 234,979
se_stake = 704,979

print('Celo activated')
north_west_counter = 0
north_east_counter = 0
south_west_counter = 0
south_east_counter = 0
x1 = 0; x2=0; x3=0; x4=0
rpa.moveTo(460,460, 0.1)
rpa.scroll(5000)
rpa.scroll(-1290)
#main loops
if possible_answers['nw']:
    while True:
        #Search for the png image in east_counter_frame
        x = rpa.locateOnScreen('l_1_nw.png', region=nw_box_frame)
        if x:
            pix_test = (rpa.pixel(182, 248), rpa.pixel(210,246),
            rpa.pixel(238,249),rpa.pixel(271,249),rpa.pixel(299,249))
            time.sleep(0.4)
            x = rpa.locateOnScreen('l_1_nw.png', region=nw_box_frame)
            pix_last =(rpa.pixel(182, 248), rpa.pixel(210,246),
            rpa.pixel(238,249),rpa.pixel(271,249),rpa.pixel(299,249))
            if (pix_last == pix_test) and x:
                rpa.click(x=nw_stake[0],y=nw_stake[1], interval=0.03)
                north_west_counter += 1
                print('Lance em produto North_west: ' + str(north_west_counter))
                while x:
                    x = rpa.locateOnScreen('l_1_nw.png', region=nw_box_frame)
                    continue

        warning = rpa.locateOnScreen('SIM.png', region=warning_frame)
        if warning:
            time.sleep(0.3)
            rpa.click(x=warning[0]+40, y=warning[1]+29,interval=0.3)


if possible_answers['ne']:
    while True:
        #Search for the png image in east_counter_frame
        x = rpa.locateOnScreen('l_1_ne.png', region=ne_box_frame)
        if x:
            pix_test = (rpa.pixel(644,249), rpa.pixel(672,249),
            rpa.pixel(704,248),rpa.pixel(735,248),rpa.pixel(769,248))   ##change pixel readers
            time.sleep(0.4)
            x = rpa.locateOnScreen('l_1_ne.png', region=ne_box_frame)
            pix_last = (rpa.pixel(644,249), rpa.pixel(672,249),
            rpa.pixel(704,248),rpa.pixel(735,248),rpa.pixel(769,248))
            if (pix_last == pix_test) and x:
                rpa.click(x=ne_stake[0],y=ne_stake[1], interval=0.03)
                north_east_counter += 1
                print('Lance em produto North_east: ' + str(north_east_counter))
                while x:
                    x = rpa.locateOnScreen('l_1_ne.png', region=ne_box_frame)
                    continue

        warning = rpa.locateOnScreen('SIM.png', region=warning_frame)
        if warning:
            time.sleep(0.3)
            rpa.click(x=warning[0]+40, y=warning[1]+29,interval=0.3)


if possible_answers['sw']:
    while True:
        #Search for the png image in east_counter_frame
        x = rpa.locateOnScreen('l_1_nw.png', region=sw_box_frame)
        if x:
            pix_test = (rpa.pixel(188,894), rpa.pixel(212,894),
            rpa.pixel(237,896),rpa.pixel(261,896),rpa.pixel(290,894))   ##change pixel readers
            time.sleep(0.4)
            x = rpa.locateOnScreen('l_1_nw.png', region=sw_box_frame)
            pix_last = (rpa.pixel(188,894), rpa.pixel(212,894),
            rpa.pixel(237,896),rpa.pixel(261,896),rpa.pixel(290,894))
            if (pix_last == pix_test) and x:
                rpa.click(x=sw_stake[0],y=sw_stake[1], interval=0.03)
                south_west_counter += 1
                print('Lance em produto Southth_east: ' + str(south_west_counter))
                while x:
                    x = rpa.locateOnScreen('l_1_nw.png', region=sw_box_frame)
                    continue
        warning = rpa.locateOnScreen('SIM.png', region=warning_frame)
        if warning:
            time.sleep(0.3)
            rpa.click(x=warning[0]+40, y=warning[1]+29,interval=0.3)


if possible_answers['se']:
    while True:
        #Search for the png image in east_counter_frame
        x = rpa.locateOnScreen('l_1_ne.png', region=se_box_frame)
        if x:
            pix_test = (rpa.pixel(648,896), rpa.pixel(671,894),
            rpa.pixel(701,894),rpa.pixel(731,895),rpa.pixel(757,895))   ##change pixel readers
            time.sleep(0.4)
            x = rpa.locateOnScreen('l_1_ne.png', region=se_box_frame)
            pix_last = (rpa.pixel(648,896), rpa.pixel(671,894),
            rpa.pixel(701,894),rpa.pixel(731,895),rpa.pixel(757,895))
            if (pix_last == pix_test) and x:
                rpa.click(x=se_stake[0],y=se_stake[1], interval=0.03)
                south_east_counter += 1
                print('Lance em produto Sowth_east: ' + str(south_east_counter))
                while x:
                    x = rpa.locateOnScreen('l_1_ne.png', region=se_box_frame)
                    continue
        warning = rpa.locateOnScreen('SIM.png', region=warning_frame)
        if warning:
            time.sleep(0.3)
            rpa.click(x=warning[0]+40, y=warning[1]+29,interval=0.3)


    #make sure the page is active
