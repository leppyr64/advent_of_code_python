
a = 'ooooooooooooobooooooooooooo$ooooooooooooooooooooooooooo$ooboooooooooobooooooooooooo$oooooboboobobooooboobobbooo$ooobbobobboobobbbbobboobooo$ooobobobobobooooobobboboooo$obobooooobooooobboooooooboo$ooobbobobbobboobobobooboooo$ooobobobobobobboobbobbooboo$oooobobobooooboooboobbobooo$ooobooooobobboobbooooooobbb$ooooooobbbbooobobboobbobbob$oobobooboooooobooobbooooobo$ooooobbboobobboooboobbobobb$ooboboobbobbooobooooooboobb$ooobobbbbooobboboobbbbooobo$ooooobboooooobboobobobobobb$ooooboobboobbboobobobobbobb$oobboooobboobobooooboooboob$ooooooboobobooobobboooooobb$bbboobbooboobboooboobbbbobb$obbboobooobobbboboooboboobo$boooooooboooboooobboboobobb$booboooooobooboooobboooobbo$bobobbbboboobbbbbbboobboobo$booobbbbbbbobbobboobbbbbbbo$oobooboooobbbboobbboboboobb$'
x = ''
n = 0
s = ''
for c in a:
    if x != c:
        if n != 1:
            s = s + str(n)
        s += x
        x = c
        n = 1
    else:
        n += 1
print(s)
        

