import unittest
class error(Exception):
    pass

class StringVide(error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
class StringHelper:
    def __init__(self):
        return 0

    def nb_occur(self, String, Mot):
        c = 0
        if len(String) == 0:
            raise StringVide
        list = StringHelper.fractionner(0, String, ' ')
        for w in list:
            if w == Mot:
                c += 1
        return c

    def incr_char(self, String):
        str = ""
        for c in String:
            if c.isalpha():
                str += chr(ord(c) + 1)
            else:
                str += c
        return str
    def Magiscule(self,String):

     cap = True
     for c,i in enumerate(String) :
         if cap and String[c] != ' ':
             String = String[:c] +String[c:].capitalize()
             cap = False
         if String[c] == '.' :
             cap = True
     return String





class TP_Test(unittest.TestCase):

    def test_nboc(self):
        str=" penser a acheter 3 kilo pomme de tere , 2 kilo tomate et 1 kilo courgette ."
        self.assertEqual(StringHelper.nb_occur(0,str,'kilo'),3)

    def test_Mag(self):
        str1="bonJour . ce Message a Ete fais dans le BUT de tester la fonction . Enjoy it !"
        str2="Bonjour . Ce message a ete fais dans le but de tester la fonction . Enjoy it !"
        self.assertEqual(StringHelper.Magiscule(0,str1),str2)

        str="asde poij"
        str2="btef qpjk"
        self.assertEqual(StringHelper.incr_char(0,str),str2)

unittest.main()