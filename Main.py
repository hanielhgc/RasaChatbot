

import hunspell

spellchecker = hunspell.Hunspell('C:/Users/Haniel/PycharmProjects/RasaChatbot/dicts/pt_BR')


palavra = ''

print(spellchecker.spell(palavra))
print(spellchecker.suggest(palavra))

#caso false, pegar a primeira suggestion desde que não seja ""