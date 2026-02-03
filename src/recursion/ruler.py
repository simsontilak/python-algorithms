def print_ruler(length, div_level):
    to_print = 0
    print_unit(to_print, length, div_level)


def print_unit(to_print, length, div_level):
    print()
    print(to_print)
    print_div(div_level - 1)
    if(to_print == length):
        return
    else:
        print_unit(to_print + 1,length)


def main():
    length = int(input("Enter length in inches: "))
    div_level = int(input("Enter scale divider level: "))
    print_ruler(length,div_level)
    
if __name__ == "__main__":
    main()
    