print ("----------BUSCA LETRAS DE CANCIONES--------")
print("- Taylor Swift \n- Selena Gomez \n- Lana del Rey \n- Adele \n- Lady Gaga \n- LP")
artista = input("Ingresa el nombre del artista: ")

match artista:
    case "Taylor Swift":
        print ("1- Getaway Car - Taylor Swift \n2- Exile - Taylor Swift \n3- Shake it Off - Taylor Swift \n4- No body no crime - Taylor Swift")
        cancion = int(input("\nSelecciona una de las canciones anteriores: "))
        match cancion:
            case 1:
                print("Getaway Car - Taylor Swift ----------")
                print("Think about the place where you first met me \nRidin in a getaway car \nThere were sirens in the beat of your heart \nShouldve known Id be the first to leave \nThink about the place where you first met me \nIn a getaway car, oh-oh-oh \nNo, they never get far, oh-oh-ah \nNo, nothin good starts in a getaway car")

            case 2:
                print("Exile - Taylor Swift ----------")
                print("I think I've seen this film before \nAnd I didn't like the ending \nYou're not my homeland anymore \nSo what am I defending now? \nYou were my town \nNow I'm in exile, seein' you out \nI think I've seen this film before")
            
            case 3:
                print("Shake it Off - Taylor Swift ----------")
                print("But I keep cruising \nCan't stop, won't stop moving \nIt's like I got this music in my mind \nSaying it's gonna be alright \nI never miss a beat \nI'm lightning on my feet \nAnd that's what they don't see \nThat's what they don't see")
        
            case 4:
                print("No body no crime - Taylor Swift -----------")
                print("I think he did it but I just can't prove it \nI think he did it but I just can't prove it \nI think he did it but I just can't prove it \nNo, no body, no crime \nBut I ain't letting up until the day I die \nNo, no \nI think he did it \nNo, no \He did it")

    case "Selena Gomez":
        print("1- Who Says? - Selena Gomez")
        cancion = int(input("\nSelecciona una de las canciones anteriores: "))
        match cancion:
            case 1:
                print("Who Says? - Selena Gomez ----------")
                print("I wouldn't wanna be anybody else \nYou made me insecure \nTold me I wasn't good enough \nBut who are you to judge \nWhen you're a diamond in the rough \nI'm sure you got some things \nYou'd like to change about yourself \nBut when it comes to me \nI wouldn't want to be anybody else")

    case "Lana del Rey":
       print ("1- Radio - Lana del Rey \n2- Cinnamon Girl - Lana del Rey")
       cancion = int(input("\nSelecciona una de las canciones anteriores: "))
       match cancion:
            case 1:
                print("Radio - Lana del Rey ----------")
                print("Not even they can stop me now \nBoy, I'll be flying overhead \nTheir heavy words can't bring me down \nBoy, I've been raised from the dead \nNo one even knows how hard life was \nI don't even think about it now because \nI finally found you \nOh, sing it to me")
            
            case 2:
                print("Cinnamon Girl - Lana del Rey ---------")
                print("There's things I wanna say to you, but I'll just let you leave \nLike if you hold me without hurting me \nYou'll be the first who ever did \nThere's things I wanna talk about, but better not to keep \nBut if you hold me without hurting me \nYou'll be the first who ever did")
        
    case "Adele":
        print ("1- Rooling in the Deep - Adele")
        cancion = int(input("\nSelecciona una de las canciones anteriores: "))
        match cancion:
             case 1:
                print("Rooling in the Deep - Adele -----------")
                print("There's a fire starting in my heart \nReaching a fever pitch, it's bringing me out the dark \nFinally I can see you crystal clear \nGo ahead and sell me out and I'll lay your ship bare \nSee how I'll leave with every piece of you \nDon't underestimate the things that I will do \nThere's a fire starting in my heart \nReaching a fever pitch and it's bringing me out the dark")
   
    case "LP":
       print ("1- Lost on You - LP")
       cancion = int(input("\nSelecciona una de las canciones anteriores: "))
       match cancion:
           case 1:
                print("Lost on You - LP ----------")
                print("When you get older, plainer, saner \nWill you remember all the danger we came from? \nBurnin' like embers, fallin' tender \nLong before the days of no surrender years ago \nAnd will you know? \nSo smoke 'em if you got 'em, 'cause it's goin' down \nAll I ever wanted was you \nI'll never get to heaven 'cause I don't know how")

    case "Lady Gaga":
        print ("1- Paparazzi - Lady Gaga")
        cancion = int(input("\nSelecciona una de las canciones anteriores: "))
        match cancion:
            case 1:
                 print("Paparazzi - Lady Gaga ----------")
                 print("I'm your biggest fan \nI'll follow you until you love me \nPapa-Paparazzi \nBaby, there's no other superstar \nYou know that I'll be \nYour Papa-Paparazzi \nPromise I'll be kind \nBut I won't stop until that boy is mine \nBaby, you'll be famous \nChase you down until you love me \nPapa-Paparazzi")
    

       



