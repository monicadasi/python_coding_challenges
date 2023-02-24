# if y comes before x in english alphabet then transform x to upper case
# if x comes before y then transform x to lower case
# if x and y are equal then no change

sentence = "a Blue MOON" 
exp_result = "a BLUe MOOn"
#sentence = "coOL dog" #result : "cOOl dOg"
_res = ""
def transformSentence(sentence):
    _length = len(sentence) + 1
    _res_str = sentence
    for i in range(_length):
        if i + 1 < len(sentence):
            s2 = sentence[i]
            s1 = sentence[i+1]
            if s1 == " " or s2 == " ":
                pass
            else:
                print(f's1 : {s1}, s2 " {s2}')
                _idx = sentence.index(s1)
                if s1.lower() == s2.lower():
                    print("Both chars are same no change")
                elif ord(s2.lower()) < ord(s1.lower()):
                    print(f'{s2} comes before {s1}, transform {s1} to upper')
                    _res_str = _res_str.replace(sentence[_idx], sentence[_idx].upper())
                elif ord(s1.lower()) < ord(s2.lower()):
                    print(f'{s1} comes before {s2}, transform {s1} to lower')
                    _res_str = _res_str.replace(sentence[_idx], sentence[_idx].lower())
    print(f'{_res_str} , program executed -> {_res_str == exp_result}')
transformSentence(sentence)