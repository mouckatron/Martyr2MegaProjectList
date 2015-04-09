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

    def vowelcount(self, split=False):
        vowels = set(('a','e','i','o','u','A','E','I','O','U'))
        if split:
            count = {'a': 0L,'e': 0L,'i': 0L,'o': 0L,'u': 0L}
            for char in self:
                if char in vowels:
                    count[char.lower()] += 1
        else:    
            count = 0L
            for char in self:
                if char in vowels:
                    count += 1
        return count

    def consonantcount(self, split=False):
        consonants = set(('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'))
        if split:
            count = {'b':0L,'c':0L,'d':0L,'f':0L,'g':0L,'h':0L,'j':0L,'k':0L,'l':0L,'m':0L,'n':0L,'p':0L,'q':0L,'r':0L,'s':0L,'t':0L,'v':0L,'w':0L,'x':0L,'y':0L,'z':0L}
            for char in self:
                if char in consonants:
                    count[char.lower()] += 1
        else:    
            count = 0L
            for char in self:
                if char in consonants:
                    count += 1
        return count
    
    def charactercount(self, split=True):
        if split:
            consonants = self.consonantcount(True)
            vowels = self.vowelcount(True)
            consonants.update(vowels)
            return consonants
        else:
            return len(self)
    