import pyautogui as rpa
from lance_functions import box, box_frame


nw_box = box(177,159,295,218)
ne_box = box(646,158,766,220)
sw_box = box(179,808,294,868)
se_box = box(647,808,765,865)

ax = rpa.screenshot('lance_4_nw.png', region=nw_box)
