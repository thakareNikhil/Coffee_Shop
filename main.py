while True:
    print('>'*50)
    print('WELCOME TO STAR-BUCKS'.center(50))
    print('<'*50)
    print("""
    1.View Coffee Menu&Price 
    2.Exit""")
    a=int(input('Entre Option: '))
    match a:
        case 1:
            print('>'*50)
            print("""
            1.Espresso:        ₹100
            2.Americano:       ₹120
            3.Cappuccino:      ₹150
            4.Cafe Latte:      ₹160
            5.Mocha:           ₹180
            6.Cold Coffee:     ₹150
            7.Iced Americano:  ₹130
            8.Caramel Latte:   ₹190
            9.Exit""")
            print('<'*50)
            a=int(input('Choose Coffee: '))
            match a:
                case 1:
                    print('*'*40)
                    print('Great Choice : Espresso ')
                    print('*'*40)
                    a=int(input('Entre Qyt:'))
                    print('*'*40)
                    print("""
                    a.Chaco-Chips:          ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*'*40)
                    b=input("Add extra or press 'e':").lower()
                    print('*'*40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a*100)+(a*30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a*100)+(a*20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a*100)+(a*25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a*100)+(a*30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a*100}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a*100}.0')
                case 2:
                    print('*' * 40)
                    print('Great Choice : Americano ')
                    print('*' * 40)
                    a = int(input('Entre Qyt:'))
                    print('*' * 40)
                    print("""
                    a.Chaco-Chips:     ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*' * 40)
                    b = input("Add extra or press 'e':").lower()
                    print('*' * 40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 120) + (a * 30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 120) + (a * 20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 120) + (a * 25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 120) + (a * 30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 120}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 120}.0')
                case 3:
                    print('*' * 40)
                    print('Great Choice : Cappuccino')
                    print('*' * 40)
                    a = int(input('Entre Qyt:'))
                    print('*' * 40)
                    print("""
                    a.Chaco-Chips:     ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*' * 40)
                    b = input("Add extra or press 'e':").lower()
                    print('*' * 40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 150}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 150}.0')
                case 4:
                    print('*' * 40)
                    print('Great Choice : Cafe Latte ')
                    print('*' * 40)
                    a = int(input('Entre Qyt:'))
                    print('*' * 40)
                    print("""
                    a.Chaco-Chips:     ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*' * 40)
                    b = input("Add extra or press 'e':").lower()
                    print('*' * 40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 160) + (a * 30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 160) + (a * 20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 160) + (a * 25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 160) + (a * 30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 160}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 160}.0')
                case 5:
                    print('*' * 40)
                    print('Great Choice : Mocha ')
                    print('*' * 40)
                    a = int(input('Entre Qyt:'))
                    print('*' * 40)
                    print("""
                    a.Chaco-Chips:     ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*' * 40)
                    b = input("Add extra or press 'e':").lower()
                    print('*' * 40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 180) + (a * 30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 180) + (a * 20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 180) + (a * 25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 180) + (a * 30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 180}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 180}.0')
                case 6:
                    print('*' * 40)
                    print('Great Choice : Cold Coffee ')
                    print('*' * 40)
                    a = int(input('Entre Qyt:'))
                    print('*' * 40)
                    print("""
                    a.Chaco-Chips:     ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*' * 40)
                    b = input("Add extra or press 'e':").lower()
                    print('*' * 40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 150) + (a * 30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 150}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 150}.0')
                case 7:
                    print('*' * 40)
                    print('Great Choice : Iced Americano ')
                    print('*' * 40)
                    a = int(input('Entre Qyt:'))
                    print('*' * 40)
                    print("""
                    a.Chaco-Chips:     ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*' * 40)
                    b = input("Add extra or press 'e':").lower()
                    print('*' * 40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 130) + (a * 30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 130) + (a * 20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 130) + (a * 25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 130) + (a * 30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 130}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 130}.0')
                case 8:
                    print('*' * 40)
                    print('Great Choice : Caramel Latte ')
                    print('*' * 40)
                    a = int(input('Entre Qyt:'))
                    print('*' * 40)
                    print("""
                    a.Chaco-Chips:     ₹30
                    b.Extra milk:      ₹20
                    c.Chocolate syrup: ₹25
                    d.Whipped cream:   ₹30
                    e.Proceed Order Without Add Extra Item""")
                    print('*' * 40)
                    b = input("Add extra or press 'e':").lower()
                    print('*' * 40)
                    match b:
                        case 'a':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 190) + (a * 30)}.0')
                        case 'b':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 190) + (a * 20)}.0')
                        case 'c':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 190) + (a * 25)}.0')
                        case 'd':
                            print('Chaco-Chips Added')
                            print(f'Total Amt: ₹{(a * 190) + (a * 30)}.0')
                        case 'e':
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 190}.0')
                        case _:
                            print('Proceed Without Add Extra')
                            print(f'Total Amt: ₹{a * 190}.0')

                case 9:
                    print('Thanks For Visit')
                    print('Visit Again')
                    exit()
                case _:
                    print('Invalid Option')
        case 2:
            print('Thanks For Visit')
            exit()
        case _:
            print('Invalid Option')