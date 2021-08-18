import random
import time

flag = "UAH{Qu1cK_m4tH5_f0R_tHE_w1n!}"

print("flashback to frantically completing homework for canvas submission at 11:58 PM")
print("answer Blue's math homework problems! be quick, you only have 20 seconds!\n")

def generate_eq():
    op1 = random.randrange(1,100000)
    op2 = random.randrange(1,100000)
    operator = random.choice(['*','-','+'])
    eq = f"{str(op1)} {operator} {str(op2)}"
    ans = eval(eq)
    return eq, str(ans)

end = time.time() + 20 # 20 seconds to solve 200 equations

for i in range(200):
    eq, ans = generate_eq()
    user_input = input(eq + " = ")
    if time.time() >= end:
        print("time's up! Blue will have to take a late grade.")
        exit(-1)
    if ans == user_input:
        print("Great work!")
        continue
    else:
        print("wrong! Blue has failed his class!")
        exit(-1)
print(f"Thank you! Here is your flag: {flag}")