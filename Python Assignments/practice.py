def money(salary, tax_rate, expenses):
    answer = (salary - ((salary * tax_rate))// 1 - expenses)
    print(answer)
    return answer
money(10000, .004, 3000)
money(30000, 0.013,2200)
