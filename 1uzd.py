"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

!)kādus ciparus jūs ziniet? arābu cipari, 10 cipari no 0-9
2) kādus romiešu ciparus jūs ziniet? I V C M X L D   XX1 21
3) kas ir klase? programmesanas struktura kas var definet datu uzvedibu un metodes
4) klase sastāv no konstruktūra vai destruktora un metodem (iekšējam funkcijam)
5) kādas datu struktūras ziniet?
- lsit(saraksts)a=""
-arry(masīvs)
-dict ( vārdnīca) a=() a={} a=dict()
"""
class AAA:



    #jadifinē konstruktors
    def __init__ (self):
        self.roma_sk={
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    #definē nepieciešamās funckijas
    def to_roman(self, num): 
     result = "" 
    for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
    return result

       #piemērs
    skaitlis=2023
    #definējam objektu
    kk+AAA()
    # jaunajam objektam jaizsauc klases metode
    romieshu=kk.to_roman(skaitlis
    
    
    #noformēt izdruku
    print(f"{skaitlis} ar romieshu cipariem ir {romieshu}.')

    