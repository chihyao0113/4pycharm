def createDictionary():
    spanish=dict()
    spanish['hello']='halo'
    spanish['yes']='si'
    spanish['one']='uno'
    spanish['two']='dos'
    spanish['red']='rojo'
    spanish['black']='negro'
    spanish['blue']='azul'
    return spanish
def main():
    dictionary=createDictionary()
    print(dictionary['two'])
    print(dictionary['red'])
main()

