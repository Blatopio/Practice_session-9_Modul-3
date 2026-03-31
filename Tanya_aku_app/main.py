from chains.explain_chains import chains

while True:
    print('''
   XXXXX XXXX XXXXXXX                      X            XX                                                                     
   XXXXX XXXX XXXXXXX                      X            XX                      
          XXX                              XX          XXX                      
         XXX            XXXXX    XXXXXXXXX  XX       XXXX        XXXXXXX        
         X X      XXXXXXX  XX    XX     XX    XX   XXXX       XXXXXX  XX        
         XXX     XXXX      X     X      XX     XXXXX        XXXX      XX        
         XXX    XX         X     XX     XX       XX       XXXX       XX         
         XXXX   X         XX     XX     XX      XXX       XXX        XXX        
         XXXX   X       XXXX     XX     XX     XX          X        XX XX       
          XXX   XXXX XXXX  XXXXX XX     XX    XX           XXXX   XXX   XX      
                   XXX                                         XXXX             
                                                                                
                           XXX  XX          XX       XX                         
                          XX X  XX   XXXX  XXX       XXX                        
                        XX  XX  XX XXXX    X X       XXX                        
                      XXX   XX  XXXXX      X X      XXXX                        
                     XXXXXXXXX  XX  XXX    X X      XXXX                        
                   XXX    XXXX  XX    XX   XXX      XXX                         
                  XX        XX  XX     XX   XXXXXXXXXXX                         
                 XX         X    X      X    XXXXXXXXX                                                                        
          
          ''')
    print('''
        ╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗
        ╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢
        ╟┤Type "exit/quit" to exit the program├╢
        ╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢
        ╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝     
          ''')

    input_user = input("Masukkan pertanyaan Anda: ")
    if input_user.lower() in ['exit', 'quit']:
        print("Terima kasih telah menggunakan Tanya Aku! Sampai jumpa!")
        break
    else:
        response = chains.invoke({'input_user': input_user})
        print("Jawaban:", response.content)
        print("\n --------------------------------------------------\n")
        print("Apakah Anda ingin bertanya lagi? (ya/tidak)")
        again = input().lower()
        if again != 'ya':
            print("Terima kasih telah menggunakan Tanya Aku! Sampai jumpa!")
            break
