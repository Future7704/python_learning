weight_input = input('Weight: ')
l_or_k = input('(L)bs or (K)g: ')
if l_or_k == 'L' or l_or_k == 'l':
    weight_output = int(weight_input) * 0.45
    print(f'You are {weight_output} kilos')
elif l_or_k == 'K' or l_or_k == 'k':
    weight_output = int(weight_input) / 0.45
    print(f'You are {weight_output} pounds')