#Task 1 - Motorbike

moterbike_value = 2000

def bike_depreceation(bike_value):
    
    while bike_value > 1000:
        print(round(bike_value, 2))
        bike_value *= 0.9
        
bike_depreceation(moterbike_value)

