import unittest
class StringHelper:
    def __init__(self):
        return 0
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

    def test_Mag(self):
        str1="bonJour . ce Message a Ete fais dans le BUT de tester la fonction . Enjoy it !"
        str2="Bonjour . Ce message a ete fais dans le but de tester la fonction . Enjoy it !"
        self.assertEqual(StringHelper.Magiscule(0,str1),str2)

