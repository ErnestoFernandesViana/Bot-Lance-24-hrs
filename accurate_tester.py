import pyautogui as rpa
import time
import lance_functions as ls

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


#main loop
while True:
    #Search for the png image in east_counter_frame

    x1 = rpa.locateOnScreen('lance_8.png', region=nw_box_frame)
    #x2 = rpa.locateOnScreen('l_1_ne.png', region=ne_box_frame)
    #x3 = rpa.locateOnScreen('l_1_nw.png', region=sw_box_frame)
    #x4 = rpa.locateOnScreen('l_1_ne.png', region=se_box_frame)

    #axis_pixel_list = [rpa.pixel(250,171),rpa.pixel(661,169),rpa.pixel(190,817),rpa.pixel(661,819)]

    if x1:
        start = time.time()
        pix_test = (rpa.pixel(182, 248), rpa.pixel(210,246),
        rpa.pixel(238,249),rpa.pixel(271,249),rpa.pixel(299,249))
        time.sleep(0.4)
        pix_last =(rpa.pixel(182, 248), rpa.pixel(210,246),
        rpa.pixel(238,249),rpa.pixel(271,249),rpa.pixel(299,249))
        x1 = rpa.locateOnScreen('lance_8.png', region=nw_box_frame)
        if (pix_last == pix_test) and x1:
            rpa.click(x=500,y=20, interval=0.03)
            end= time.time()
            print('encontrado x1')
            print(end-start)
            north_west_counter += 1
            while x1:
                x1 = rpa.locateOnScreen('lance_8.png', region=nw_box_frame)
                continue
