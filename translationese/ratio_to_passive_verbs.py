"""\
Implementation of Ration to passive verbs to all verbs hypothesis.

Origin: On the Features of Translationese, VV, NO & SW
        4.5 Miscellaneous, Ration of passive forms to all verbs
"""
attributes = [ "ration_to_passive_verbs" ]

def quantify(analysis):
    def is_verb(pos_tag):
        return pos_tag[0] == 'V' and pos_tag[1] == 'B'
    
    def is_VBN_verb(pos_tag):
        return pos_tag == 'VBN'
    
    def count_all_verbs():
        result =  float(len([x for (x,y) in analysis.pos_tags() if is_verb(y)]))
        return result
   
    def count_all_passive_verbs():
        passive_verbs = 0
        text = analysis.pos_tags()
        for i in range(len(text)):
            if (text[i][0] == 'be') and (is_VBN_verb(text[i+1][1])):
                passive_verbs += 1
        
        print passive_verbs
        return float(passive_verbs)
    
    result = float(count_all_passive_verbs() / count_all_verbs())
    return { "ratio_to_passive_verbs" : result }