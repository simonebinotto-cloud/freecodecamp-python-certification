class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
             
    def get_balance(self):
        money = 0
        for tmp in self.ledger:
            money += tmp['amount']
        return money

    def transfer(self, amount, category):
        tmp = self.withdraw(amount, f'Transfer to {category.name}')
        if tmp:
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
        

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

    def __str__(self):
        output = ""
        total = 30

        for i in range(0, round((total - len(self.name)) / 2)):
            output += '*'
        output += self.name
        for i in range(0, (total - (len(self.name) + round((total - len(self.name)) / 2)))):
            output += '*'
        output += '\n'

        for i in range(0, len(self.ledger)):

            descrizione = self.ledger[i]['description'][:23]

            importo_str = f"{self.ledger[i]['amount']:.2f}"
            
            output += descrizione

            inizio_spazi = len(descrizione)
            fine_spazi = total - len(importo_str)
            
            for z in range(inizio_spazi, fine_spazi):
                output += ' '
                
            output += importo_str + '\n'

        output += f'Total: {self.get_balance():.2f}'

        return output
       

def create_spend_chart(categories):
    output2 = ""
    output2 += "Percentage spent by category\n"
    
    total_spent = 0
    spent = []
    
    for i in range(0, len(categories)):
        categoria_subtotal = 0  
        for z in range(0, len(categories[i].ledger)):
            if categories[i].ledger[z]['amount'] < 0:
                categoria_subtotal += abs(categories[i].ledger[z]['amount'])
                total_spent += abs(categories[i].ledger[z]['amount'])
        spent.append(categoria_subtotal)
    
    percentages = []
    for i in range(0, len(categories)):
        if total_spent > 0:
            percentages.append((((spent[i] / total_spent) * 100) // 10) * 10)
        else:
            percentages.append(0)
    
    initial = 100
    for i in range(0, 11):
        valore = initial - (i * 10)
        output2 += f"{valore:>3}|"

        for z in range(0, len(categories)):
            if percentages[z] >= valore:
                output2 += " o "
            else:
                output2 += "   "
        
        output2 += " \n"
    
    output2 += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    length = []
    for i in range(0, len(categories)):
        length.append(len(categories[i].name))

    for i in range(0, max(length)):
        output2 += "    "
        for z in range(0, len(categories)):
            if i < len(categories[z].name):
                output2 += " " + categories[z].name[i] + " "
            else:
                output2 += "   "
        output2 += " \n"
        
    return output2.rstrip("\n")
