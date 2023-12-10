
#Fun with python function string outputs

#prints title case of name
# f_name = input('What is your first name? \n')
# l_name = input('What is your last name? \n')
def format_name1(f_name, l_name):
    name = f_name + " " + l_name
    return print(name.title())
format_name1("patrick", "faerber")

def format_name2(f_name, l_name):
    frmt_f_name = f_name.title()
    frmt_l_name = l_name.title()
    print(f'{frmt_f_name} {frmt_l_name}')
format_name2("paTRick", "fAErber")

def format_name3(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Please enter valid string input"
    else:
        frmt_f_name = f_name.title()
        frmt_l_name = l_name.title()
    return f"Full Name: {frmt_f_name} {frmt_l_name}"

print(format_name3("paTRICK", "fAErber"))

print(format_name3(input('What is your first name?\n'), input('What is your last name?\n')))