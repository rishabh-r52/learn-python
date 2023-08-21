name = "Rishabh"
date = "02/02/2020"

letter = '''Dear <|NAME|>,
You are selected!
<|DATE|>'''

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)