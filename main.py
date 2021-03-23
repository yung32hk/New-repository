x="aeAI xcvV"
vowel=["a","e","i","o","u"]
vowel_list=[i for i in x if i.lower() in vowel]
consonant_list=[i for i in x if i.lower() not in vowel]
print(vowel_list)
print(consonant_list)