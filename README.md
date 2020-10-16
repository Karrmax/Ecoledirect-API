# Ecoledirect-API
python module which make requests to Ecoledirect API

usage :

<code> cn = EcoleDirect("username", "password")
  
  
    notes = cn.getNotes()['notes']
    for i in range(len(notes)):
        print(notes[i]['valeur'],"/", notes[i]['noteSur'], notes[i]['libelleMatiere'], "au coef", notes[i]['coef'])



    print(cn.getSL())

    print(cn.getHW())

    print(cn.getCloud())
