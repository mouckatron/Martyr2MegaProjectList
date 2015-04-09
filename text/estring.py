#! /usr/bin/python2.7

class estring(str):
    
    def reverse(self):
        return self[::-1]
    
    def piglatin(self):
        import re
        vowels = set(('a','e','i','o','u','A','E','I','O','U'))
        #vowel_re
        consonant_re = re.compile(r'([bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+)([a-zA-Z]*)(.*)?')
        piglatin = []
        for word in self.split():
            # there are different rules if it starts with a vowel
            if word[0] in vowels:
                piglatin.append(word+'way')
            else:
                piglatin.append(consonant_re.sub(r'\2\1ay\3', word))
        
        # output the translated text
        return ' '.join(piglatin)

    