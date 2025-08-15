deposit = eval(input(" Enter amount to deposit --> ", )) 
print("Here is a breakdown of the deposited amount: ") 

thousand1 = (deposit // int(1000)) 
thousand2 = (deposit % int(1000))
print(thousand1, "- 1,000")

fivehundred1 = (thousand2 // int(500))
fivehundred2 = (thousand2 % int(500))
print(fivehundred1, "- 500") 

twohundred1 = (fivehundred2 // int(200))
twohundred2 = (fivehundred2 % int(200))
print(twohundred1, "- 200")

onehundred1 = (twohundred2 // int(100))
onehundred2 = (twohundred2 % int(100))
print(onehundred1, " 100") 

fifty1 = (onehundred2 // int(50))
fifty2 = (onehundred2 % int(50))
print(fifty1, "- 50") 

twenty1 = (fifty2 // int (20))
twenty2 = (fifty2 % int (20))
print(twenty1, "- 20") 

ten1 = (twenty2 // int(10))
ten2 = (twenty2 % int(10))
print(ten1, "- 10") 

five1 = (ten2 % int(5))
five2 = (ten2 // int(5))
print(five2, "- 5")

one1 = (five1 // int(1))
print(one1, "- 1")