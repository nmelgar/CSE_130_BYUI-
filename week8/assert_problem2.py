array = []

def linear_search(array, search):
    assert len(array) > 0, "Array is empty"
    for index in range(0, len(array)):
        
        if array[index] == search:
            return True
    
    return False
    

print(linear_search(array, 2))