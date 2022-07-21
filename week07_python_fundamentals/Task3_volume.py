def box_volume(width, depth, height):
    volume = width * depth *height
    return volume

def box_volume_rounded(width, depth, height):
    volume = width * depth *height
    return round(volume,2)

#There is need to specify the input type. If a float is entered as a paramater the output will
#be a float. It will be an int if all paramaters are ints.

box_volume(10.12, 14.5, 41)
box_volume_rounded(11,5,6)
