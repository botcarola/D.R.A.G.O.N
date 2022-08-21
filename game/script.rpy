# Character

define prisionero = Character("Influencer", color = "#48F3FA")
define ia = Character("D.R.A.G.0.N", color = "#4AFA56")
define hacker = Character("Heral", color = "#A547D6")

init: 

    # backgrounds

    image bgNegro = Image("bgnegro.png")
    image carcel = Image("bgcarcel.jpg")
    image salaHackeo = Image("bghack.jpg")  
    image carcelHack = Image("bglab.jpg") 
    image goodEnding = Image("goodending.jpg")
    image badEnding = Image("badending.png")

    #protagonista    
    image iSerio = Image("iserio2.png")
    image iNeutral = Image("iserio.png")
    image iAsombrado = Image("iasombro.png") 
    image iContento = Image("ifeliz.png")    
    image iMiedo = Image("imiedo.png")
    image iTranquilo = Image("iserio.png")
    image iEnojado = Image("ienojado.png")
    image iPreocupado = Image("ipreocupado.png")
    image iTriste = Image("itriste.png")


    #hacker
        
    image hSeria = Image("hseria.png")  
    image hContenta = Image("hsonrisa.png")
    image hAsombrada = Image ("hsorprendida.png")
    image hAsustada = Image("hsusto.png")
    image hPreocupada = Image("hpreocupada.png")
    image hMolesta = Image("henojada2.png")
    image hEnojada = Image("henojada.png")
    image hAflijida = Image("haflijida.png")

    # holohacker

    image holoSeria = Image("holoseria.png")  
    image holoContenta = Image("holosonrisa.png")
    image holoAsombrada = Image ("holosorprendida.png")
    image holoAsustada = Image("holosusto.png")
    image holoPreocupada = Image("holopreocupada.png")
    image holoMolesta = Image("holoenojada2.png")
    image holoEnojada = Image("holoenojada.png")
    image holookAflijida = Image("holoaflijida.png")

label start:

    scene bgNegro with vpunch

    play sound "audio/sonidosacudon.ogg"

    play music "audio/sonidofondonegro.ogg"

    prisionero "¡¿Dónde estoy?!"

    play sound "audio/sonidocadenas.ogg"

    prisionero "¿Y esto qué es?"
   
    scene carcel with dissolve

    prisionero "Sáquenme de aquí les digo."

    play sound "audio/sonidocadenas.ogg"

    prisionero "¡Me escuchan! Sáquenme de aquí."

    menu:
        "Hay un espejo. Te acercas a el.":
            jump escena2

        "Sigues gritando":
           jump escenaFinal

label escena2: 

    stop music 

    play music "audio/audiocarcel.ogg" # agregar loop

    show iSerio with dissolve

    prisionero "¿Quién eres?"

    hide iSerio

    show iNeutral

    prisionero "¿Hace cuánto que he dormido?"

    hide iNeutral

    show iAsombrado

    prisionero "¿Soy yo?"

    hide iAsombrado with dissolve

    ia "Buenos días Influencer de mil millones de seguidores, estamos teniendo problemas con tu nivel cardio respiratorio. ¿Hay algo en lo que pueda asistirte?"

    show iAsombrado 

    prisionero "¿Y esa voz?"

    hide iAsombrado

    show iMiedo

    prisionero "¡AUXILIO! NO TE ME ACERQUES"

    ia "Influencer404 le administraremos un sedante, por lo visto ha perdido el objetivo de su primera orden."

    play sound "audio/sonidogas.ogg"

    prisionero "Mi primera orden, eh si..."

    hide iMiedo

    show iNeutral   

    prisionero "Es cierto, estamos en la nave Spes3"

    hide iNeutral

    show iContento

    prisionero "Debería estar preparando mi discurso de las redes para todos mis seguidores que están viviendo en el planeta tierra, en las catacumbas."

    hide iContento

    show iTranquilo

    prisionero "Debo informarles que desde aquí todo sigue viéndose muy contaminado para habitarlo  y que no deben salir por ningún motivo."

    hide iTranquilo

    show iContento

    ia "¡Muy bien Influencer404!"

    menu:
        ia "¿Y recuerda quién soy?"
        "Ni idea":
            jump escenaFinal

        "Por supuesto": 
            jump escena3

label escena3:        
    
    hide iContento

    show iNeutral

    prisionero "D.R.A.G.0.N"

    hide iNeutral

    show iTranquilo
  
    prisionero "Eres nuestra esperanza de la humanidad" 

    hide iTranquilo

    show iContento

    prisionero "Una IA creada para proteger nuestra cultura, privándome del contacto de los terrestres, porque moriría con ellos debido al virus que poseen."
    
    hide iContento

    show iTranquilo     

    prisionero "Debo informarles todos los días en mis transmisiones que no deben salir a la superficie."

    hide iTranquilo

    show iContento

    play sound "audio/sonidoexito.ogg"

    ia "¡Felicitaciones! 404 has pado el exámen de conciencia, toma una galletita."

    hide iContento

    show iAsombrado 

    prisionero "¡Qué rico! Amo las galletitas de crema con chocolate"

    hide iAsombrado

    show iContento      

label escena4:  

    stop music 

    play sound "audio/sonidofondonegro.ogg"

    scene bgNegro with dissolve    

    play sound "audio/sonidoteclas.ogg"

    "default__date__((earth))"

    play sound "audio/sonidoteclas.ogg"

    "setting ip = this.IP(10020.000304-0200239.2000)" 

    play sound "audio/sonidoteclas.ogg"   
    
    "SUB_RUTINE(2000030041920)"   

    play sound "audio/sonidoteclas.ogg"

    "setting caducidad = `60 60 24 30`;"   

    play sound "audio/sonidoteclas.ogg"

    "else_if(C00KI3[[`galleta`]]) ==== NOTHING) {{this.cookie(`galleta`, `crema de chocolate`, this.caducidad)}}"  

    play sound "audio/sonidoteclas.ogg" 

    "2000030041920.inProgress()"

    play sound "audio/sonidoteclas.ogg"

    scene bgNegro with fade

    stop sound
   
label escena5:

    play sound "audio/sonidofondonegro.ogg"

    "Debe funcionar, todo lo hemos hecho con el estricto orden para que D.R.A.G.0.N le pase desapercibida la cookie."
    "Es la única posibilidad que tenemos para poder entrar en su consciencia y despertarlo."

    menu: 
        "¿Y tu quién eres":
            jump escena51

        "¿Quieres matar a 404?":
            jump escena52    

label escena51:

    stop sound
    
    play music "audio/confictoActo2.ogg"

    scene salaHackeo with dissolve
    
    show hSeria  

    hacker "¿Es broma?"

    hide hSeria

    show hAsombrada

    hacker "¿Te está afectando la conexión? Soy Heral, liderando la operación para rescatar a 404."

    hide hAsombrada

    show hPreocupada

    hacker "¿Estás bien?"

    menu:
        "¿Y ahora qué hacemos?":
            jump escena61

        "No lo estoy ¿Acaso quieres matar a 404?":
            jump escena52

label escena61:
    
    show hSeria

    hide hSeria

    show hPreocupada   

    hacker "Si han funcionado los meses de trabajo que pusimos en esa galleta y D.R.A.G.0.N le ha dado la correcta, podemos conectarnos mentalmente con 404."

    hide hPreocupada

    show hSeria   

    hacker "La única forma de que rompa las reglas es dándole instrucciones desde afuera y así logre liberarse."

    scene bgNegro with dissolve

label escena7:

    stop music    
    
    scene bgNegro with vpunch

    play sound "audio/sonidosacudon.ogg"

    play sound "audio/sonidofondonegro.ogg"

    prisionero "¡¿Dónde estoy?!"

    show holoPreocupada

    hacker "404 ¿Me escuchas?¿Puedes verme?"

    scene carcel with dissolve  

    show holoPreocupada 

    menu:
        "¿Quién me está hablando?":
            jump escena81
        
        "D.R.A.G.0.N ¿Eres tú?, ¿Acaso estoy soñando?":
            jump escena92

label escena81:

    stop sound

    play music "audio/audiocarcel.ogg"

    show holoPreocupada

    hacker "404 {b}DESPIERTA{/b}"

    hide holoPreocupada

    show holoSeria

    hacker "¡Lo que estás viviendo no es real!"

    hide holoSeria

    show holoPreocupada

    hacker "D.R.A.G.0.N te ha apresado a ti y a toda la humanidad en una {b}mentira.{/b}"   

    hacker "Podemos volver a la superficie."   

    hacker "Necesitamos que se lo digas a todos, solamente tienes que escribirlo en esa computadora que tienes frente a ti, yo te ayudaré a que escapes."

    menu:
        "Todo esto es MENTIRA, pide ayuda a D.R.A.G.0.N":
            jump escena91

        "Averigua más sobre ese holograma":
            jump escena92

label escena91:

    hide holoPreocupada

    show iAsombrado

    prisionero "¿Esto que está a mi lado es real?"

    hide iAsombrado

    show iMiedo    

    prisionero "¡Auxilio, no te me acerques! D.R.A.G.0.N ¡AYÚDAME!"

    hide iMiedo

    show holoEnojada    

    hacker "¡¿Qué haces?!"

    hacker "Soy Heral ¿no me recuerdas?"

    hide holoEnojada

    show holoSeria

    hacker "Somos familia, jugamos juntxs desde pequeños."

    hide holoSeria

    show holoPreocupada

    hacker "{b}No puede ser, no reconoce ni a su semejante.{/b}"

    hide holoPreocupada

    show holoAsombrada    

    hacker "Sácanos ahora, va a colapsar"

    play sound "audio/sonidoalarmafinal.ogg"

    menu: 
        "Tú que lo controlas todo, convence a 404":
            jump escena101

        "Tú que lo controlas todo, rescata a Heral":
            jump escena102 

label escena102:

    hide holoAsombrada

    scene bgNegro with dissolve

    stop music

    play music "audio/audiocarcel.ogg"

    show holoPreocupada   

    hacker "Recibí tu código."

    hide holoPreocupada

    show holoSeria

    play sound "audio/sonidoalarmafinal.ogg"    

    hacker "¡Ya no nos queda tiempo! D.R.A.G.0.N viene por nosotrxs, hay que terminar la simulación e intentarlo de nuevo."

    hide holoSeria

    show iAsombrado    

    prisionero "Esto es una locura."

    hide iAsombrado

    show iMiedo
    
    prisionero "Tu presencia pudo enternecerme, pero no caeré en esta trampa nuevamente."

    hide iMiedo

    show iEnojado   

    prisionero "Aléjate o enfrentarás la muerte."

    hide iEnojado

    show holoAsombrada

    hacker "Sácame ya, está colapsando."

    return

label escena101:

    scene bgcarcel with dissolve

    show iTriste  

    prisionero "Simulación terminada."
    
    prisionero "Cantidad de intentos de rescate: X"  

    prisionero "Navegante, no podemos {b}romper las reglas y salvar a quienes no quieren ser salvados.{/b}"

    prisionero "He puesto mi consciencia en esta simulación para que Heral, mi familia y alguien valiente como tú, de la era post-pandémica y en un lugar como este, la Women Game Jam 2022, me rescate en el futuro de mi prisión mental."

    hide iTriste

    show iPreocupado

    prisionero "La humanidad ha creado esta triste realidad."

    hide iPreocupado

    show iTriste

    prisionero "El exceso de atención de la población, hacia las redes, ha disparado un extremo descuido al planeta tierra."  

    hide iTriste

    show iSerio

    prisionero "Inténtalo de nuevo, no pierdas la oportunidad de cambiar al mundo y romper tus propias reglas. No podemos volver a cometer los mismos errores."

    #escena bad badending

    return  

label escena92:  

    scene bgcarcel with dissolve

    show iSerio

    play music "audio/audiocarcel.ogg"

    prisionero "¿Por qué siento que te conozco de antes?"

    hide iSerio

    show iNeutral

    prisionero "¿Es acaso todo esto una vaga ilusión?"

    hide iNeutral

    show iAsombrado

    prisionero "¿D.R.A.G.0.N está haciendo de las suyas con mi mente?"

    hide iAsombrado

    show iMiedo

    prisionero "¿Y este sabor extraño a crema y galletas, qué es?"

    hide iMiedo

    show holoPreocupada    

    hacker "Sé que no me reconoces pero somos familia."

    hide holoPreocupada

    show holoSeria    

    play sound "audio/sonidoalarmafinal.ogg"

    hacker "Tienes que despertar, ya no nos queda tiempo, el futuro de la humanidad depende de ti."

    hide holoSeria

    ia "Influencer 404 ¿Con quién habla?"

    ia "Identifique su monólogo o ejecutaré el protocolo de emergencia."

    show iAsombrado

    hacker "No tenemos tiempo 404. Por favor, ve a la computadora, solo tú puedes liberar a la humanidad."

    hide iAsombrado

    show iSerio 

    hacker "La clave para librarnos de este entorno en donde estamos sumidos, creado por D.R.A.G.0.N, es: r0mp3rL4sR3gl4s"

    menu:
        "404 ve a la computadora y escribe la clave":
            jump escenario111
        
        "Todo esto es un sueño 404, pide ayuda a D.R.A.G.0.N":
            jump escena101

label escenario111:

    scene carcelHack with dissolve
    
    play sound "audio/sonidoteclas.ogg"

    "Navegante que los suspiros del mar"

    play sound "audio/sonidoteclas.ogg"

    "Humedecen las únicas palabras"

    play sound "audio/sonidoteclas.ogg"

    "Por las que vale vivir"  

    menu:
        "Ingrese password:"
        "romperLasReglas": 
            jump escena92
        
        "pr3s3rv4rL4sR3glas":
            jump escena92
        
        "r0mp3rL4sR3glas":
            jump escenario120

label escenario120:

    stop sound

    stop music

    play music "audio/goodEndingAudio.ogg"

    show holoContenta

    scene bgNegro with dissolve
    
    hacker "¡Navegante, lo hemos logrado!"

    hacker "404 está a salvo, ya podemos salir a la superficie"

    hide holoContenta

    ia "Quizás hayas podido romper las reglas y en el proceso salvar a la humanidad."

    ia "Todos deseamos un final feliz para las malas decisiones que la raza humana crea día a día, entre las redes y el abandono a la tierra."

    ia "Siempre los errores se pueden volver a comenter, inclusive en una simulación tan simple como esta."

    ia "Navegante, nunca lo olvides, depende de ti romper las reclas, ahora ve afuera."

    #godending

return    

label escenaFinal:

    stop music

    show iPreocupado

    play sound "audio/sonidoalarmafinal.ogg"

    ia "¡Atención!"

    ia "Influencer404 da error en el reconocimiento de interfaz de la interfaz de acceso a Dragon"

    hide iPreocupado

    show iAsombrado

    stop music

    play music "audio/ascensorAudio.ogg"

    prisionero "No sé qué pasa, ¿Qué es 'Dragon'? ¿Quién eres?"

    ia "Reiniciando sujeto"

    play sound "audio/sonidogas.ogg"

    hide iAsombrado

    show iMiedo 

    prisionero "¡NO!"   

    #bad ending 

    return

label escena52:

    play music "audio/confictoActo2.ogg"

    scene bglab with dissolve
    
    show hMolesta 

    hacker "Por supuesto que no."

    hide hMolesta

    show hSeria

    hacker "Me importa tanto su vida como a tí."

    hide hSeria

    show hPreocupada

    hacker "A veces tenemos que romper las reglas de esta nave para poder traer esperanza a toda la humanidad."

    scene bgNegro with dissolve

    jump escena7  