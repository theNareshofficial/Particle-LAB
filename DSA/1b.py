# 1b) Smallest number in list

def smallest_num_in_list(list):

            min = list[0]

            for a in list:
                    if a < min:
                        min = a
            return min

print("Smallest Number", smallest_num_in_list([1, 2, -8, 0]))

"""
Output : 
Smallest Number -8
"""