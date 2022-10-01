# conversor dlls
def conversor_money_dlls():
    money_input = float(input("Ingresa la cantidad a convertir "))
    if(money_input < 0):
        print("ingrese un número válido")
    else:
        dlls_money = 20.15
        total_dlls = money_input * dlls_money
        print(total_dlls)  

        # main function
        select_type_money()      


def conversor_money_cop():
    cop_money = 0.0045
    money_cop = float(input("ingresa pesos a convertir "))
    if money_cop < 0:
        print("ingresa un número válido")
    else:
        total_cup = money_cop * cop_money
        print(total_cup)

        # main function
        select_type_money()      


def conversor_money_vol():
    vol_money = 40.666,1
    money_vol = float(input("ingresa pesos a convertir "))
    if money_vol < 0:
        print("ingresa un número válido")
    else:
        total_vol = money_vol * vol_money
        print(total_vol)

        # main function
        select_type_money()      


# input type money
def select_type_money():
    type_money = ["dlls", "cop", "vol"]

    money_type = input("Ingresa el tipo de moneda a convertir ")
    if money_type == type_money[0]:
        conversor_money_dlls()

    elif money_type == type_money[1]:
        conversor_money_cop()

    elif money_type == type_money[2]:
        conversor_money_vol()

    else:
        print("escribe algo valido: ")
        for types_money in type_money:
            print(types_money)

# start!
select_type_money()