import subprocess

in_use = True

while in_use:
    # Alarm to be altered
    to_be_spaced = input("Paste alarm here: ")
    final = ""

    #Scans alarm for comas and replaces them with '||'
    if "," in to_be_spaced:
        commas = to_be_spaced.replace(',', ' || ')
        final = commas.replace('  ', ' ')
        
    
    #Scans alarm for 'and' word and replaces with '||'
    if "and" in to_be_spaced:
        and_replace = to_be_spaced.replace('and', ' || ')
        final = and_replace.replace('  ', ' ') 

    #Gets rid of the word "alarm"
    if 'alarm' or 'alarms' or 'Alarm' or 'Alarms' in final:
        forbidden_words = {'Alarms': ' ', 'alarms': ' ', 'alarm': ' ', 'Alarm': ' '}
        for key, value in forbidden_words.items():
            final = final.replace(key, value)

    print("")
    #Copies the modified alarm to clipboard
    subprocess.run("pbcopy", text=True, input=final)
    print(final)

    cont = (input("\nMore alarms? ")).lower()

    #Breaks out of loop if no more alarms to be altered
    if cont in ["no", "n"]:
        in_use = False





