'''
For task 3 of the week 7 Home Learning Tasks. The functions calculates the
volume of a box. The second function does the same but rounds the answer to
2 decimal places.
'''
def box_volume(width, depth, height):
    volume = float(width * depth *height)
    return volume

def box_volume_rounded(width, depth, height):
    volume = float(width * depth *height)
    return round(volume,2)

box_volume(10.12, 14.5, 41)
box_volume_rounded(11.3,5.23,6)
