def arithmetic_arranger(calculos, results=False):
    first_row = ''
    second_row = ''
    underline = ''
    total_rows = ''

    if len(calculos) > 5:
        erro = 'Error: Too many problems.'
        return erro

    for calc in calculos:
        n1 = []
        n2 = []
        operator = []
        spacing_top = ''
        spacing_bottom = ''
        for n in calc:
            if n == ' ':
                n.replace(' ', '')
            elif n == '\\' or n == '*':
                erro_1 = "Error: Operator must be '+' or '-'."
                return erro_1
            elif not n.isdigit() and not n == '+' and not n == "-":
                erro_2 = 'Error: Numbers must only contain digits.'
                return erro_2
            elif n == '+' or n == "-":
                operator.append(n)
            elif n.isdigit:
                if len(operator) == 1:
                    n2.append(n)
                else:
                    n1.append(n)

            if len(n1) > 4 or len(n2) > 4:
                erro_3 = 'Error: Numbers cannot be more than four digits.'
                return erro_3

        # underline
        if len(n1) > len(n2):
            maior = len(n1)
            menor = len(n2)
            size = len(n1) + 2
            space = maior - menor
            for i in range(space):
                spacing_bottom += ' '
        else:
            size = len(n2) + 2
        unders = ''
        for i in range(size):
            unders += "-"

        n1, n2, operator = ''.join(n1), ''.join(n2), ''.join(operator)

        # calculating the results
        if results:
            soma = 0
            if operator == "+":
                soma = int(n1) + int(n2)
            else:
                soma = int(n1) - int(n2)
            soma = str(soma)

            # espacing results
            space_reslt = ''
            space_needed = len(unders) - len(soma)
            for i in range(space_needed):
                space_reslt += ' '

        space_needed = len(unders) - len(n1)
        for i in range(space_needed):
            spacing_top += ' '

        four_spaces = '    '

        if len(first_row) >= 1 and len(second_row) >= 1:
            first_row += four_spaces + spacing_top + n1
            second_row += four_spaces + operator + ' ' + spacing_bottom + n2
            underline += four_spaces + unders

        else:
            first_row += spacing_top + n1
            second_row += operator + ' ' + spacing_bottom + n2
            underline += unders

        if results:
            if len(total_rows) >= 1:
                total_rows += four_spaces + space_reslt + soma
            else:
                total_rows += space_reslt + soma

    final = '\n'.join((first_row, second_row, underline, total_rows))
    return final
