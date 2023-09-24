filenames = ["ComoFunciona.txt", 
             "Consideraciones.txt", 
             "QueEsUnFondoDeInv.txt", 
             "Brainwashing.txt", 
             "faqBanorte.txt"]
for i in range(len(filenames)):
    filenames[i] = "datatxt/" + filenames[i]

with open("datatxt/compilation.txt", "w") as new_file:
    for name in filenames:
        with open(name) as f:
            for line in f:
                new_file.write(line)
            
            new_file.write("\n")