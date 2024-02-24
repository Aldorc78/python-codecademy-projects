class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "{} menu is available from {} to {}.".format(self.name, self.start_time, self.end_time)
  def calculate_bill(self, purchased_items):
    total = 0 
    for item in purchased_items: 
      total += self.items[item]
     
    return print("Your total from the {} menu is: ".format(self.name)+str(total), "\n") 


#Creating an instance for every menu in the class Menu with name, the items available, start and end time.
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, "11am", "4pm")

early_bird = Menu("Early bird", { 'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli(vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00 }, "3pm", "6pm")

dinner = Menu('Dinner', {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, "5pm", "11pm")

kids = Menu('Kids', {'chiken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11am", "9pm")

#Testing the string representation for some objects of the class
print(brunch)
print(kids, "\n")

#Creating an order from the brunch menu
brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
#Creating an order from the earlu bird menu
early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli(vegan)'])

"Basta Fazoolin' with my Heart has seen tremendous success with the family market, which is fantastic because when you're at Basta Fazoolin' with my Heart with family, that's great! We've decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country."

class Franchise: 
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus 
  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    available_menus = [] #list to be return later
    numbers_global = "1234567890"

    #Method that converts to int and 24hr format
    def int_24hr(hour_string):
        hr_str = " "
        for symbol in hour_string: 
          if symbol in numbers_global:
             hr_str += symbol
        time_int = int(hr_str) 
        if "pm" in hour_string and hour_string != "12pm":
          time_int += 12
        return time_int    
    #End of method   

    time = int_24hr(time) #Calling int_24hr function to convert input to int 24hr 
    
    #--Calling int_24hr function to convert start_time and end_time
    for menu in self.menus:
        '''
          Each menu has 2 time parameter. one is for start time
          the other is for end time, we first will convert start time and then end time. also, we're converting from am/pm format to  24hr.
         '''
        start_time = int_24hr(menu.start_time) #we take start parameter
        end_time = int_24hr(menu.end_time)     #we take end parameter

        #---We now have int variables 'start_hour' and 'end_hour' in 24hr format----
        if time >= start_time and time <= end_time:
            print(menu.name + " is available")
            available_menus.append(menu)#Adding menu to list
        else:
            print(menu.name + " is not available.")
    print(f'Your input was: {time}', "\n")
    return available_menus



     
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids] )
new_installment = Franchise("12 East Mulberry", [brunch, early_bird, dinner, kids])

print(flagship_store)
print(new_installment,"\n")

flagship_store.available_menus("12pm")
flagship_store.available_menus("5pm")

#------------BUSINESS CLASS------------
class Business:

  def __init__(self, name, franchises): #list of franchises
      self.name = name 
      self.franchises = franchises

basta_fazoolin = Business("Basta Fazoolin' with my heart", [flagship_store, new_installment ]) 

arepas_menu = Menu("Take a'Arepa",{'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon':7.50 }, "10am", "8pm")

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
take_Arepa = Business("Take a'Arepa", arepas_place)
