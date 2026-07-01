def hanoi_solver(n):

    pioli = [
        list(range(n, 0, -1)),  
        [],                    
        []                      
    ]
    
    mosse_salvate = []
    
    def salva_stato():
        stato = f"{pioli[0]} {pioli[1]} {pioli[2]}"
        mosse_salvate.append(stato)

    salva_stato()

    def muovi_torre(dischi, origine, destinazione, ausiliario):
        if dischi == 1:
            disco = pioli[origine].pop()
            pioli[destinazione].append(disco)
            salva_stato()
        else:
            muovi_torre(dischi - 1, origine, ausiliario, destinazione)
            
            disco = pioli[origine].pop()
            pioli[destinazione].append(disco)
            salva_stato()
            
            muovi_torre(dischi - 1, ausiliario, destinazione, origine)


    muovi_torre(n, 0, 2, 1)
    
    return "\n".join(mosse_salvate)

print(hanoi_solver(3))