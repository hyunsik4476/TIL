a, b, c = map(int, input().split(','))

quadform_ans = [(-b - (b**2 - 4*a*c)**0.5) / (2*a), 
(-b + (b**2 - 4*a*c)**0.5) / (2*a)]

print('The answer is {0} and {1}'.format(quadform_ans[0], quadform_ans[1]))