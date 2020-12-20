#stall information
Western = "'Singapore-style' Western Cuisine usually\n\
includes chicken chop (topped with black \n\
pepper or mushroom sauce), chicken\n\
cutlet pork chop are available. These \n\
are usually served with fries or mashed\n\
potato, coleslaw and baked beans."

Mixed_Veg_Rice = "Economy rice stalls consist of a case\n\
containing 10-15 troughs of \n\
cooked food, including meat, vegetables,\n\
eggs and tofu dishes. Customers\n\
select any combination of these dishes,\n\
which are served accompanied by a\n\
portion of steamed white rice."

Xin_Mei_Noodle = "Banmian (板麵) is a popular Chinese \n\
noodle dish, consisting of handmade \n\
noodles served in soup. Other type \n\
of handmade noodles include youmian\n\
or mee hoon kueh."

Chicken_Rice = "Hainanese chicken rice is a dish of \n\
poached chicken and seasoned rice, \n\
served with chilli sauce and usually \n\
comes with cucumber garnishes."

#menu items
#categorised Western menu
Western_B_D_item_price = {"French Toast" : "$1.80",
                          "Egg and Cheese Sandwich" : "$2.50",
                          "Eggs Benedict" : "$2.80",
                          "Bacon and Eggs" : "$3.50"}     #prices for Breakfast Weekday menu items in Western food


Western_B_E_item_price = {"French Toast" : "$1.80",
                          "Bacon and Eggs" : "$3.50",
                          "Pancake Sausage" : "$3.50",
                          "Steak and Eggs" : "$3.80"}    #prices for Breakfast Weekend menu items in Western food

Western_L_D_item_price = {"Sausage Rice" : "$5.00",
                          "Chicken Chop" : "$5.80",
                          "Chicken Cutlet" : "$5.80",
                          "Fish & Chips" : "$5.80",
                          "Beef Steak" : "$7.00"}       #prices for Lunch Weekday menu items in Western food

Western_L_E_item_price = {"Chicken Chop" : "$5.80",
                          "Fish & Chips" : "$5.80",
                          "Grilled Fish" : "$5.80",
                          "Grilled Lamb Loin" : "$6.50",
                          "Ribeye Steak" : "$7.00"}        #prices for Lunch Weekday menu items in Western food


#other menus
MVR_item_price = {"3 Veg" : "$2.30",
                  "1 Meat 1 Veg" : "$2.40",
                  "1 Meat 2 Veg" : "$3.00",
                  "1 Fish 1 Meat" : "$4.00",
                  "2 Meat 2 Veg" : "$4.40"}         #prices for menu items in Mixed Veg Rice

XM_item_price = {"Ban Mian" : "$3.00",
                 "U Mian" : "$3.00",
                 "Mee Sua" : "$3.00",
                 "Yi Mian" : "$3.00",
                 "Thin Bee Hoon" : "$3.00"}         #prices for menu items in Xin Mei Noodle Stall

CR_item_price = {"Steamed Chicken Rice" : "$3.00",
                 "Roasted Chicken Rice" : "$3.00",
                 "Lemon Chicken Rice" : "$3.00",
                 "Curry Chicken Noodle" : "$3.00"}        #prices for menu items in Chicken Rice

#breakfast or lunch menu
Western_weekday_menu = {"Breakfast" : Western_B_D_item_price, "Lunch" : Western_L_D_item_price}
Western_weekend_menu = {"Breakfast" : Western_B_E_item_price, "Lunch" : Western_L_E_item_price} #breakfast or lunch

MVR_weekday_menu = {"Breakfast" : MVR_item_price, "Lunch" : MVR_item_price}
MVR_weekend_menu = {"Breakfast" : MVR_item_price, "Lunch" : MVR_item_price}

XM_weekday_menu = {"Breakfast" : XM_item_price, "Lunch" : XM_item_price}
XM_weekend_menu = {"Breakfast" : XM_item_price, "Lunch" : XM_item_price}

CR_weekday_menu = {"Breakfast" : CR_item_price, "Lunch" : CR_item_price}
CR_weekend_menu = {"Breakfast" : CR_item_price, "Lunch" : CR_item_price}


#weekday or weekend
Western_dayorend = {"Weekday" : Western_weekday_menu, "Weekend" : Western_weekend_menu} #weekday or weekend

MVR_dayorend = {"Weekday" : MVR_weekday_menu, "Weekend" : MVR_weekend_menu}

XM_dayorend = {"Weekday" : XM_weekday_menu, "Weekend" : XM_weekend_menu}

CR_dayorend = {"Weekday" : CR_weekday_menu, "Weekend" : CR_weekend_menu}

#store name
NSFC = {"Western" : Western_dayorend, "Mixed Veg Rice" : MVR_dayorend,
        "Xin Mei Noodle Stall" : XM_dayorend, "Chicken Rice" : CR_dayorend}     #North Spine Food Court stalls

