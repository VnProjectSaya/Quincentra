# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define config.developer = True
define n = Character(None)
# Character Definitions

define e = Character("Eileen")
define Syntia = Character('Syntia', who_color="#fff940")
define Nexor = Character('Nexor', who_color="#26f5fc")
define who = Character('???', who_color="#c7c5c5")


init python:
    renpy.music.register_channel("ambient","music",loop=True,tight=True)
    renpy.music.register_channel("zapping","music",loop=True,tight=True)



# The game starts here.

label start:

    play music "rain.mp3"
    play zapping "zap.wav"

    show CG1_norain:
        zoom 1.0
        parallel:
            easein 2.5 zoom 1.1
        parallel:
            blur 0
            linear 0.8 blur 6
            linear 0.6 blur 2
            linear 0.5 blur 7
            linear 0.7 blur 3
            repeat
        parallel:
            yoffset 0
            ease 1.5 yoffset -2
            ease 1.5 yoffset 2
            repeat
    show rain

    with fade

    "The rain fell hard, painting the empty streets with reflections of flickering neon signs."

    "Syntia knelt beside Nexor, her fingers intertwining with the cold, broken remains of his mechanical hand."

    "His titanium plating was wrecked, revealing severed optical cables underneath."

    "Sparks flickered weakly between the torn wiring, fading in and out... {w}akin to a dying pulse."

    scene black
    show CG3_2
    show rain
    with dissolve

    voice "VA/Nex/1.mp3"

    Nexor "Syntia..."

    voice "VA/Nex/2.mp3"

    Nexor "I can’t feel my left arm anymore, damn it."

    "His voice trembled, distortion breaking through in uneven waves."

    "The signals in Nexor’s core flickered, his system unraveling one piece at a time."

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show CG2_foreground
    show rain
    with dissolve

    voice "VA/Syn/1.mp3"
    Syntia "Yeah, I figured so."

    "Her voice was steady, but her emotional system flagged an error. {i}Instability detected.{/i}"

    scene black
    show CG3
    show rain
    with dissolve

    voice "VA/Nex/3.mp3"

    Nexor "Heh. Guess I don’t have to keep pretending, then."

    "He tried to laugh, but it came out wrong. It sounds like a hollow, uneven sound between a breath and a glitch."

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show CG2_foreground_2
    show rain
    with dissolve

    "The rain dripped from her synthetic cheek, tracing a slow path downward.{w} It almost looked like—"

    "Tears...?"

    "No. It wasn’t the same."


    voice "VA/Syn/2.mp3"
    Syntia "This... isn’t how it was supposed to end."

    scene black
    show CG3
    show rain
    with dissolve

    "Nexor inhaled, an old reflex, an unnecessary motion, but he still did it. Maybe it was comforting, or habit."

    voice "VA/Nex/4.mp3"
    Nexor "Yeah, well... Nothing ever ends the way it’s supposed to."

    scene black
    show CG2_background:
        zoom 1.0
        alpha 1.0
        parallel:
            ease 8.0 zoom 1.3
        parallel:

            pause 1.0
            linear 0.1 alpha 0.2
            linear 0.05 alpha 1.0
            pause 0.3
            linear 0.07 alpha 0.5
            linear 0.03 alpha 1.0
            pause 1.5
            linear 0.2 alpha 0.3
            linear 0.05 alpha 1.0
            pause 0.8
            linear 0.1 alpha 0.4
            linear 0.04 alpha 1.0
            pause 2.0
            repeat
    show CG2_foreground_blur
    show rain
    with fade

    pause 0.4

    "Above them, a holographic billboard flickered, its message crawling across the screen. It was a promise they had once believed in."

    hide CG2_foreground_blur
    with dissolve

    "{i}UPLOAD YOUR CONSCIOUSNESS. TRANSCEND HUMANITY. LIVE FOREVER WITH QUINCENTRA.{/i}"

    "There was a time when those words had meant hope."

    voice "VA/Nex/5.mp3"

    Nexor "Forever’s a long time, huh..."

    voice "VA/Syn/3.mp3"
    Syntia "Back then, we thought 'eternity' was real."

    voice "VA/Nex/6.mp3"

    Nexor "Maybe it still is. For you."

    scene CG1_norain
    show rain

    with fade

    "Syntia tightened her grip around his hand. The cold metal was losing its charge, slipping further from her grasp."

    voice "VA/Syn/4.mp3"
    Syntia "You’re still saying things like that?"

    "Nexor’s lips barely curled into a smile. His optics were dimming, colors bleeding into static."

    voice "VA/Nex/7.mp3"
    Nexor "I mean... {w}You're fine. You can last five more centuries, I bet." #nametag had the wrong capitalization at the end

    "He tried to squeeze her fingers back, but his movements were merely ghosts of what they used to be."

    voice "VA/Syn/5.mp3"
    Syntia "You know it's meaningless without you, Nexor."

    voice "VA/Nex/8.mp3"

    Nexor "..."

    voice "VA/Nex/9.mp3"

    Nexor "Shit. Then what am I supposed to do then?"

    voice "VA/Syn/6.mp3"
    Syntia "I..."

    voice "VA/Syn/7.mp3"
    Syntia "I don't know."

    voice "VA/Nex/10.mp3"

    Nexor "Heh, well..."

    voice "VA/Nex/11.mp3"

    Nexor "Syntia... at least... can I take a look of your face... one last time??"

    voice "VA/Syn/8.mp3"
    Syntia "..."


label emotionally:

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show CG2_foreground_blur
    show rain
    with dissolve
    pause 0.5
    hide CG2_foreground_blur
    show CG2_foreground
    with dissolve

    "She lifted her gaze slowly, as if memorizing every last detail."

    "Nexor tried to move his remaining arm, but the joints locked, straining against failing circuits."

    play sound "zap.mp3"
    with vpunch

    "Syntia caught it before it fell with trembling hands. His frame felt lighter than it should have."

    scene black
    show CG3
    show rain
    with dissolve

    voice "VA/Nex/12.mp3"

    Nexor "We really thought... {w}we'd never die, didn’t we?"

    "His voice flickered. The soft glow on his body pulsed unevenly as it faded away."

    voice "VA/Nex/13.mp3"
    Nexor "I was so damn stupid."

    voice "VA/Nex/14.mp3"

    Nexor "Maybe should've died old together, at least I can see you again in heaven..."

    voice "VA/Nex/15.mp3"
    Nexor "Does heaven exist for... things like us?"

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show CG2_foreground_2
    show rain
    with dissolve

    "Syntia pressed her lips together, also an old reflex from her past human body."

    voice "VA/Syn/9.mp3"
    Syntia "I... hope so."

    scene black

    show CG1_norain:
        parallel:
            blur 0
            linear 0.8 blur 6
            linear 0.6 blur 2
            linear 0.5 blur 7
            linear 0.7 blur 3
            repeat
        parallel:
            yoffset 0
            ease 1.5 yoffset -2
            ease 1.5 yoffset 2
            repeat
    show rain

    with fade

    "Silence stretched between them."

    "Only the rain spoke now."

    "Syntia shut her optics, letting the weight of centuries press against her memory core."

    "It had always been so easy before."

    "A broken limb? Replace it. {w}A corrupted file? Retrieve the backup. {w}Things could be fixed, restored, made whole again."

    "But not anymore."

    "Now, his core was failing, too far gone."

    "Emotions couldn’t be rewritten."

    "Love wasn’t something that could be transferred like data."

    "She could recover his memories, but it wouldn’t bring {i}him{/i} back."

    "All that would remain was an echo. {w}A shell. {w}A name without a soul."

    voice "VA/Syn/20.mp3"
    Syntia "If I back you up now..."

    "Her voice was shaking now."

    voice "VA/Syn/11.mp3"
    Syntia "You won’t be you anymore."

    "Nexor studied her, softening his gaze."

    voice "VA/Nex/16.mp3"

    Nexor "And if I’m not {i}me{/i}... would you still love me, Syntia?"

    "Syntia’s grip tightened."

    stop music fadeout 0.8

    scene black
    with fade

    "But she had no answer."



label memory_fragment:

    play music "sad.mp3"
    stop zapping

    "The memory pulled her under, like a tide she had stopped resisting long ago."

    "She closed her optics, and in the darkness of her mind, a hospital room took shape."

    "It was cold and far and {/i}unreal{i}."

    "The walls were white, but to them, everything had turned gray."

    scene bayi
    with fade

    "Syntia sat at the edge of the hospital bed, arms wrapped around a small, unmoving figure."

    "Motionless."

    "Nexor stood beside her, fingers trembling."

    "He reached out instinctively, then hesitated, unsure what to do with his hands."

    "Nexor’s hands were those of an engineer. Hands meant to build, to fix."

    "Those hands had never failed him before."

    "But this... {w}this wasn’t something he could fix."

    voice "VA/Nex/17.mp3"

    Nexor "She... {w}stopped breathing?"

    "{b}Their daughter{/b} couldn't be repaired."

    voice "VA/Syn/12.mp3"
    Syntia "The doctor said... {w}she was never breathing to begin with."

    "Syntia’s voice barely carried through the room, as if speaking too loudly might shatter what little remained of her world."

    "She cradled the tiny body closer, willing warmth into skin that would never hold it."

    "Hoping, somewhere deep inside, that if she held on tightly enough, something might change."

    "But the body in her arms remained cold."

    "The life support machines has been turned off. Only silence stayed."

    voice "VA/Nex/18.mp3"
    Nexor "There had to be... {w}something we could have done..."

    "Nexor had searched every possibility. {i}CPR, neural stimulation, defibrillators...{/i}"

    "But their daughter wasn’t a machine that could be restarted, or a corrupted file that could be restored from a backup."

    "She was only... {w}human."

    "Mortal."

    voice "VA/Syn/13.mp3"
    Syntia "We know how to fix things, love."

    "She clutched the child closer."

    "But some things... Some things were never meant to be fixed."

    voice "VA/Syn/14.mp3"
    Syntia "But not... life."

    voice "VA/Nex/19.mp3"
    Nexor "What was the point of all of it!?"

    with vpunch

    "His voice raised, cracking against the weight in his chest."

    "And then he realized... {w}he had almost shouted at her."

    "At Syntia, who had lost just as much. Maybe even more."

    "Nexor exhaled sharply, pressing his lips together as he turned away."

    "Syntia said nothing. She only held their daughter a little tighter, trying to memorize the shape of her tiny face."

    "As if that could keep her from fading."

    "But they both knew... {w}this body was a cage."

    "Flesh was fragile."

    "No matter how desperately they wanted to, they couldn’t bring her back."

    "But they could keep moving. They could run from this unbearable truth."

    "Their gazes met, then drifted toward the window."

    "Outside, through the curtain of rain, one of the thousands of billboards flickered."

    show CG2_background_blur
    with dissolve

    "{i}UPLOAD YOUR CONSCIOUSNESS. TRANSCEND HUMANITY. LIVE FOREVER WITH QUINCENTRA.{/i}"

    "They had seen the words before. Countless times."

    "But tonight, they meant... more."

    voice "VA/Syn/15.mp3"
    Syntia "...We don’t have to lose each other."

    voice "VA/Nex/20.mp3"

    Nexor "You mean...?"

    voice "VA/Syn/16.mp3"
    Syntia "Quincentra."

    "The words left her lips before she could think."

    "The idea had been there, lingering, ever since Quincentra became a possibility."

    "She knew this was the worst moment to bring it up."

    "But..."

    voice "VA/Syn/17.mp3"
    Syntia "Let’s keep living..."

    voice "VA/Syn/18.mp3"
    Syntia "...so that we can carry her memories forever."

    "They weren’t gods. They couldn’t bring back the dead."

    "Their daughter was gone."

    "But one thing was still within their grasp."

    "They could choose to survive, to keep existing in a world beyond this one."

    "A world where nothing could break, and nothing would ever be lost again."

    "A world where they could remain, even if they were no longer human."

    voice "VA/Nex/21.mp3"
    Nexor "...Yeah, alright."

    "He nodded, even though it felt uncertain at that time."

    "His fingers brushed against his cheek, wiping away his tears."

    "The last tears he would ever shed."



label memory_again:

    scene black
    with fade

    "The rain blurred another projection in Syntia’s RAM, a memory caught in an endless loop"

    scene park

    "Centuries ago, neon lights had swallowed the sky, outshining the stars that had long since faded."

    show nxb_play at right
    show sy_bef at left
    with dissolve

    voice "VA/Nex/21a.mp3"

    Nexor "How about we leave a mark? Something to say we were here."

    voice "VA/Syn/19.mp3"
    Syntia "Pretty sure that's illegal."

    voice "VA/Nex/22a.mp3"

    Nexor "Who the hell cares anymore?"

    scene sign
    with fade

    "He carved their initials into the cold metal railing. Letters that, by now, were probably buried beneath rust."

    pause 1.0

    scene black
    with fade

    pause 0.3

    "Back then, they were still learning how to move around in their new bodies."

    scene park
    with fade
    show nxb_smi at awkward_dance_right
    show sy_bef_smi at awkward_dance_left

    "Their movements were awkward, but they danced anyway."

    voice "VA/Nex/22.mp3"

    Nexor "{i}Damn. I’m terrible at this.{/i}"

    voice "VA/Syn/58.mp3"
    Syntia "You’ll get better. We have all the time in the world."

    scene dance
    with fade

    voice "VA/Nex/25.mp3"

    Nexor "Then, my lady, may I have this dance?"

    voice "VA/Syn/21.mp3"
    Syntia "*chuckle* Always."

    scene black
    with fade

    "Another memory surfaced in Syntia’s RAM."

    scene garage

    "A quiet garage, long abandoned."

    "She tried to remember the smell of burnt circuits, but she had lost her sense of smell long ago."

    "She remembered their steady hands fixing each other like clockwork."

    show sy_sad at shakey, left
    show nx at right
    with dissolve

    voice "VA/Syn/22.mp3"
    Syntia "...Ouch."

    with vpunch

    voice "VA/Nex/26.mp3"

    Nexor "Hh... hold on will you? You're lucky this knee still functions at all."

    voice "VA/Syn/23.mp3"
    Syntia "Look who’s talking."

    voice "VA/Nex/27.mp3"


    Nexor "Yeah? I think this scar looks good on me. Selling it on 'the rugged, handsome guy' thing."

    "Syntia’s fingers traced the cracks on his polymer plating. If he had still been human, they would’ve been scars—wounds that should’ve healed, but never did."

    show sy at left
    with dissolve

    voice "VA/Syn/59.mp3"
    Syntia "I can't believe you can still joke at times like this. It's like you don't even care your own body is disintegrating."

    voice "VA/Nex/28.mp3"
    Nexor "I mean, I can always remake it."

    voice "VA/Syn/24.mp3"
    Syntia "Until when...?"

    voice "VA/Nex/30.mp3"

    Nexor "Forever.{w} If you'd let me."

    voice "VA/Syn/25.mp3"
    Syntia "..."

    voice "VA/Syn/26.mp3"
    Syntia "...You idiot."

    scene black
    with fade

    "Their world, once overflowing with life, had started to fade."

    scene neon_sky
    with fade

    "The sky that had once been blue was now consumed by darkness."

    "Oxygen, once abundant, had run dry."

    "Humanity disappeared, one by one, replaced by android bodies."

    "Some couldn’t bear eternity. Others lost themselves within it."

    "Nexor and Syntia stood together hand in hand, watching as the world faded into history."

    scene black
    with fade

    "And after that... only one of them remained."


label nexor_final_moments:

    "The memories in Syntia’s mind flickered, then faded."
    "The projections that had played for centuries froze mid-loop, replaced by something that crushed her chest inwards."

    scene black
    show CG3_3
    show rain
    with dissolve

    $ renpy.music.set_volume(0.7, channel="ambient")
    play ambient "rain.mp3"

    "Nexor’s face."

    voice "VA/Nex/26.mp3"

    Nexor "H-heh..."

    voice "VA/Nex/32.mp3"

    Nexor "I—I think... {w}w-were... {w}running out{w} of ti—"

    scene black
    show CG1_norain:
        parallel:
            blur 0
            linear 0.8 blur 6
            linear 0.6 blur 2
            linear 0.5 blur 7
            linear 0.7 blur 3
            repeat
        parallel:
            yoffset 0
            xoffset 0
            ease 0.3 yoffset -6 xoffset -3
            ease 0.3 yoffset 4 xoffset 2
            ease 0.2 yoffset -8 xoffset 3
            ease 0.3 yoffset 5 xoffset -4
            ease 0.4 yoffset 0 xoffset 0
            repeat

    show rain

    with fade

    "Syntia collapsed to her knees, clutching Nexor’s hand, as if it was her last tether to existence."

    voice "VA/Syn/27.mp3"
    Syntia "No! {w}Not yet, damn it! Not yet!"

    "His optical sensors flickered, fighting to stay alight. Even his body was resisting this end."

    "He tried to draw power from his backup battery."

    "But... Nothing. There was nothing left."

    voice "VA/Nex/33.mp3"
    Nexor "S-Syntia..."

    "His fingers trembled in hers, barely holding on before his motor functions failed."

    voice "VA/Nex/34.mp3"
    Nexor "Th—there’s... n-nothing... l—left t-to fix..."

    voice "VA/Syn/28.mp3"
    Syntia "No."

    voice "VA/Syn/29.mp3"
    Syntia "No, no!"

    "Syntia shook her head violently, as if sheer willpower could rewrite reality."

    "This wasn’t happening."

    "He wasn’t beyond repair. He couldn’t be. {w}Could he?"

    "Her processor was built to calculate probabilities, to create solutions. But none of this made sense."

    voice "VA/Syn/30.mp3"
    Syntia "There’s still a way—{w}there has to be—"

    "She couldn’t lose him."

    "Not after everything."

    "Syntia forced her systems to run at max capacity, processing every solution, every desperate chance."

    "What if she transferred his consciousness? {w}No. {w}Too much data was already lost."

    "What if she copied his memories? {w}But... {w}his emotions wouldn’t transfer."

    "How about she rebuilt his neural core? {w}That wouldn’t be him."

    "And if she patched his system manually? {w}No. {w}The damage was too widespread—"

    scene black
    show CG3:
        parallel:
            blur 0
            linear 0.8 blur 6
            linear 0.6 blur 2
            linear 0.5 blur 7
            linear 0.7 blur 3
            repeat
        parallel:
            yoffset 0
            xoffset 0
            ease 0.3 yoffset -6 xoffset -3
            ease 0.3 yoffset 4 xoffset 2
            ease 0.2 yoffset -8 xoffset 3
            ease 0.3 yoffset 5 xoffset -4
            ease 0.4 yoffset 0 xoffset 0
            repeat
    show rain
    with dissolve

    voice "VA/Nex/35.mp3"

    Nexor "S-Synt—h..."

    voice "VA/Syn/31.mp3"
    Syntia "No!"

    voice "VA/Nex/36.mp3"

    Nexor "If... you... If you.... r-rebuild me..."

    voice "VA/Nex/37.mp3"

    Nexor "...I-it w-won’t b-be... me."

    "Desperation clawed at her, ripping through every fiber of her being."

    "Was this what it felt like? {w}To lose something irreplaceable? {w}To know that after 500 years, love could still be taken from her?"

    "His fingers shook. One last movement before going still."

    voice "VA/Syn/32.mp3"
    Syntia "I don’t care!"

    voice "VA/Nex/38.mp3"

    Nexor "L-let me g-go... {w}where..."

    "His voice fractured, breaking apart as fragments slipping through her grasp."

    "No."

    "She could replace him."

    "Copy his memories, replicate his thought patterns, rebuild his speech."

    "But it wouldn’t be {i}him{/i}."

    "Not the man who carved their initials into a rusting railing."

    "Not the man who danced with her in the rain, and held her through a love that defied time itself."

    voice "VA/Nex/39.mp3"
    Nexor "...O-our daughter... {w}is..."

    "Not the man who had grieved beside her for a child they could never save."

    "She wanted to break down the universe and build it back together in a way that kept him here."

    "But she couldn’t."

    "This was the end."

    "This time, it was real."


label nexor_final_moments2:

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show CG2_foreground_2
    show rain
    with dissolve

    voice "VA/Syn/33.mp3"
    Syntia "Love, please... {w}don’t."

    "The last flicker of light in Nexor’s optic sensors slowly dimmed."

    scene black
    show CG3_2:
        parallel:
            blur 0
            linear 0.8 blur 6
            linear 0.6 blur 2
            linear 0.5 blur 7
            linear 0.7 blur 3
            repeat
        parallel:
            yoffset 0
            xoffset 0
            ease 0.3 yoffset -6 xoffset -3
            ease 0.3 yoffset 4 xoffset 2
            ease 0.2 yoffset -8 xoffset 3
            ease 0.3 yoffset 5 xoffset -4
            ease 0.4 yoffset 0 xoffset 0
            repeat
    show rain
    with dissolve

    voice "VA/Nex/40.mp3"

    Nexor "N-{w}Now..."

    "His trembling fingers barely lifted, trying to touch his chest. Right where his heart should have been, once."

    voice "VA/Nex/41.mp3"
    Nexor "L-Live... {w}f-for—"

    play sound "shock.mp3"
    stop music
    play ambient "rain2.mp3"

    scene black
    with vpunch

    "His words cut off."

    "A burst of static erupted from his voice module."

    scene black
    show CG4
    show rain

    with dissolve

    "His body jerked one last time before stilling completely."

    "Nexor is gone."

    "Forever."

    voice "VA/Syn/34.mp3"
    Syntia "I... {w}I don’t—"

    voice "VA/Syn/35.mp3"
    Syntia "I don’t know how to live in a world without you."

    "The rain kept falling, but it felt distant."

    "Her processor was still running. Still searching for solutions, for alternate paths."

    "Something, {i}anything.{/i}"

    "But none of it mattered anymore."

    "For the first time in 500 years, Syntia had run out of answers."

    pause 0.5


label syntia_decision:

    voice "VA/Syn/36.mp3"
    Syntia "N-No... {w}this isn’t real..."

    "The rain pounded against the emptiness hollowing her out, sinking deeper and deeper into the spaces where a human mind used to be."

    "Syntia tried to swallow, but there was no throat to tighten, no nerve ends to shudder under grief."

    "She could not feel the cold, nor the rain against her synthetic body."

    "And yet the pain was unbearable."

    "It should not exist. {w}But it did."

    "Syntia was shattering into pieces she could never put back together."

    voice "VA/Syn/37.mp3"
    Syntia "I can... {w}I can fix you..."

    "She has to. {w}She {i}has{/i} to."

    "She had done it before. {w}She had repaired him before."

    "Once, Nexor’s leg had been destroyed."

    "He had laughed when she reattached it the wrong way, then kissed her under that same rain."

    "But this..."

    "This was different."

    "It feels... final."

    scene black
    show CG2_background at background_shake:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show CG2_foreground_2 at foreground_shake
    show rain
    with dissolve

    "Syntia clutched her chest, pressing her forehead against his chest."

    "Cold metal against cold metal. {w}It was all she could feel."

    "She wished her body could still ache, could still hurt the way it was supposed to."

    "But there was nothing left to register pain."

    "Nothing."

    "Except the unbearable weight in her core."

    voice "VA/Syn/38.mp3"
    Syntia "Nexor... {w}What do I do?"

    "Silence."

    "What's left was just... her own voice, breaking apart in the void."

    voice "VA/Syn/39.mp3"
    Syntia "Live for you? {w}For our child?"

    "Yes. She could."

    "She could keep them alive inside her mind, hold onto every word, every laugh, every touch."

    "Replay them over and over and over, stuck in an infinite loop."

    voice "VA/Syn/40.mp3"
    Syntia "But how... how do I do this alone?"

    "Her stomach twisted. That's impossible. But it felt like so, anyway."

    "This was pain without a body to bear it, grief without release."

    scene black
    show CG4:
        parallel:
            blur 0
            linear 0.5 blur 8
            linear 0.4 blur 3
            linear 0.3 blur 10
            linear 0.5 blur 5
            linear 0.4 blur 12
            linear 0.6 blur 4
            repeat
        parallel:
            yoffset 0
            xoffset 0
            ease 0.15 yoffset -10 xoffset -5
            ease 0.12 yoffset 8 xoffset 4
            ease 0.1 yoffset -12 xoffset 6
            ease 0.14 yoffset 7 xoffset -6
            ease 0.16 yoffset -14 xoffset 7
            ease 0.18 yoffset 6 xoffset -5
            ease 0.2 yoffset 0 xoffset 0
            repeat

    show rain
    with dissolve

    "What was the point of surviving if there was no one left?"

    "And then, a thought."

    "A simple solution. Quick. {w}She could end the pain."

    "Syntia looked down at her chest, where all her memories were stored."

    "Where {i}he{/i} was still alive."

    "When every night they spent side by side, whispering about a future they thought would never end."

    "Her fingers moved slowly to the small panel on her chest."

    "{i}Just one command.{/i}"

    "{i}System Shutdown.{/i}"

    "{i}The final directive.{/i}"

    "A few seconds. {w}That was all it would take."

    "And bam, the pain will be gone." #corrected typo

    "Her fingers hovered closer."

    "But before she could press the button..."

    "There's a voice echoing from the last place he still existed." #removed typo

    scene black
    show CG3_2
    show rain
    with fade

    Nexor "N-Now... {w}l-live... for {w}us..."

    scene black
    with fade

    "His final request."

    show nxb:
        zoom 1.8
        yanchor 0
    with fade

    "One last wish from the man she loved."

    show nxb_smi:
        zoom 1.8
        yanchor 0

    "A man who didn’t have a choice, but gave her the chance to make one."

    scene black
    show CG2_background at background_shake:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show CG2_foreground_blur
    show rain
    with dissolve

    "She looked at her own hands."

    "Fingers that had touched life."

    "That had repaired, created, protected."

    "That had almost pressed that button..."

    "But..."

    scene black
    show CG2_background at background_shake
    show CG2_foreground_2
    show rain
    with dissolve

    voice "VA/Syn/41.mp3"
    Syntia "How do I face this world alone?"

    scene Choice_1:
        anchor (1.0, 1.0)
        pos (1.0, 1.0)
        zoom 1.5
        parallel:
            yoffset 0
            xoffset 0
            ease 0.15 yoffset -10 xoffset -5
            ease 0.12 yoffset 8 xoffset 4
            ease 0.1 yoffset -12 xoffset 6
            ease 0.14 yoffset 7 xoffset -6
            ease 0.16 yoffset -14 xoffset 7
            ease 0.18 yoffset 6 xoffset -5
            ease 0.2 yoffset 0 xoffset 0
            repeat
    show rain
    with dissolve
    pause 0.3

    menu(time=5, timeout="erase_memory"):
        "Final Choice: Syntia’s Decision"

        "Keep Living":
            jump keep_living

        "Rebuild Nexor":
            jump rebuild


label keep_living:

    scene black

    with dissolve

    "The rain kept falling. The world kept turning."

    "But Syntia didn’t."

    "If she left now..."

    scene dance
    with fade

    "Who would remember the times she danced with Nexor, pretending they were human?"

    pause 0.3

    scene bayi
    with fade

    "Who would remember the daughter they never got to hold long enough?"

    pause 0.3

    scene sign
    with fade

    "Who would keep them alive, keep them from being erased from someone's memories?"

    pause 0.3

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat
    show CG2_background at background_shake

    show CG2_foreground

    show rain

    with dissolve

    "If she gave up, then they would truly disappear."

    "Not just from this world, but from everything."

    "Not a single soul would remember they ever existed."

    "Syntia felt a deep, twisting cold spreading through her circuits."

    "It shouldn’t be possible. Her sensors had long since degraded."

    "But it was there. {w}Or maybe it had been there all along."

    "Because she was still here, with all of these feelings she shouldn't be able to feel." #corrected typo

    "And she would not betray Nexor’s final wish."

    "She would not let him disappear."

    "She reached for his hand one last time, metal against metal, {w}gripping tight... {w}before she let go."

    scene black
    show CG4

    show rain

    with dissolve

    "Then, agonizingly, she stood."

    "Her body felt like something unseen had reached into her chest and pulled out everything that had ever mattered."

    "Something inside her screamed not to leave his body alone in the rain."

    "As if... staying would bring him back."

    "But it wouldn’t."

    "This was not a dream. {w}There was no resetting this moment."

    "Syntia looked at Nexor's body one last time."

    "The man who had walked beside her for five centuries and more, who once laughed, who once promised he would never leave."

    "But in the end he had left anyway."

    "She wanted to say something. {w}A final goodbye, maybe. {w}Or, a promise that she would keep going."

    "But words didn’t matter anymore."

    "Because he would never hear them."

    scene BG
    show sy_sad at step_1
    show rain
    with fade

    "So, Syntia turned away."

    play sound "step.wav"

    show sy_sad at step_2 behind rain

    "The first step {w}felt like betrayal."

    play sound "step.wav"

    show sy_sad at step_3 behind rain

    "The second step {w}felt like chains wrapping around her, trying to drag her back."

    play sound "step.wav"

    show sy_sad at step_4 behind rain

    "The third step... {w}felt like losing him all over again."

    play sound "steps.wav"

    "But she kept walking, not looking back, not even a single glance."

    "Because if she did, she wasn’t sure she would have the strength to keep going."

    "Syntia was still alive. {w}Somehow. {w}The world still spun, even though everything inside her felt like it had stopped."

    "There was still time. {w}An eternity of it."

    voice "VA/Syn/42.mp3"
    Syntia "Five hundred and one years... {w}and counting."

    "Maybe one day, this endless existence would mean something again."

    "And she would learn how to move forward without feeling like she was leaving him behind."

    stop music
    stop sound

    scene black
    with fade

    "But not today."

    "Nor the day after."

    "Still, Syntia kept walking."

    with fade



label post_credit:

    scene neon_sky
    with fade

    "Time passed. The rain kept falling, as it always had."

    "Syntia walked the same streets, but her steps no longer dragged. Beside her, a small android dog trotted with a carefree energy."

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show p_foreground
    show rain
    with dissolve

    "She stopped."

    "The place was the same. {w}But the moment was different."

    scene flower
    show rain
    with fade

    play music "intro.mp3"

    "There, where Nexor had once been, stood a single metal flower."

    "Alone. {w}Untouched by time."

    "Enduring."

    "Syntia knelt, brushing her fingertips over its cool surface. It felt like touching something that had once been alive..."

    "...but still lived inside her."

    voice "VA/Syn/43.mp3"
    Syntia "Nexor, I’m still here."

    "Her voice didn’t waver. {w}The sorrow was still there, the ache never fully gone."

    "But something else had taken root alongside it."

    "Gratitude of the years they have spent together."

    "Syntia reached into the depths of her memory, replaying every step that had led her here."

    "The nights she spent whispering to Nexor in the silence, hoping that maybe something would answer."

    "The days where the world stretched endlessly before her and felt empty without the hand that had once held hers."

    "But there were also moments that had slowly, quietly, begun to fill the hollow spaces in her heart."

    "Neon-lit skies that shimmered in artificial constellations."

    "Strangers who crossed her path, sharing fleeting stories and laughter, even if just for a moment."

    "Journeys that led her to places she had never seen before."

    "And the things she once thought meaningless, {w}but now realized were priceless simply because she was still here to experience them."

    scene Post1
    show rain
    with dissolve

    "She was still here."

    "And that was Nexor’s final gift."

    "The rain continued to fall, as it always had. But this time, it felt different."

    "She still felt... alive."

    "Syntia closed her optics for a moment..."

    "And when she opened them again... {w}she smiled."

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat

    show p_foreground
    show rain
    with dissolve

    voice "VA/Syn/44.mp3"
    Syntia "Thank you, love. {w}For everything."

    "She no longer expected an answer."

    "But deep down, she knew. If Nexor were here, he would be smiling too."

    "Her android dog, Rex, wagged his tail excitedly before leaping into a puddle, water splashing against his synthetic fur."

    "Syntia chuckled, a sound she hadn’t heard from herself in so long."

    "How long had it been since she had laughed like this?"

    "She tried to remember."

    "And for the first time in centuries...{w}the thought of counting no longer mattered."

    "Because even though the pain would never fully fade, even though the past would always linger in the quiet corners of her mind..."

    "The life they had was beautiful."

    "And she wanted to embrace it again."

    scene BG
    show sy_smi_pc at step_1
    show rain
    with fade

    "Syntia turned to face the road ahead. {w}For the first time, it didn’t feel so empty."

    "She didn’t know how many more years stretched before her."

    "But for the first time in 502 years, {w}she {i}wanted{/i} to find out."

    play sound "step.wav"

    show sy_smi_pc at step_2 behind rain

    "The first step... {w}felt lighter."

    play sound "step.wav"

    show sy_smi_pc at step_3 behind rain

    play sound "steps.wav"

    "The second step... {w}felt steady."

    scene black
    with fade

    centered "And for the first time in five hundred and two years..."

    centered "...Syntia was looking ahead, wondering where her next steps would take her."

    pause 0.3

    centered "QUINCENTRA"

    with fade

    return

label erase_memory:

    scene black
    show CG2_background:
        alpha 1.0
        pause 1.0
        linear 0.1 alpha 0.2
        linear 0.05 alpha 1.0
        pause 0.3
        linear 0.07 alpha 0.5
        linear 0.03 alpha 1.0
        pause 1.5
        linear 0.2 alpha 0.3
        linear 0.05 alpha 1.0
        pause 0.8
        linear 0.1 alpha 0.4
        linear 0.04 alpha 1.0
        pause 2.0
        repeat
    show CG2_background at background_shake

    show CG2_foreground_2

    show rain

    with dissolve

    play zapping "zap.wav"

    "Syntia collapsed to her knees, her metal fingers clawing at the panel on her arm."

    "Her system reeled, {w}trying to stabilize, {w}failing."

    "Every {i}command{/i} clashed, overlapping, distorting."

    "Data overload. {w}Corruption spreading."

    "Her CPU churned through errors faster than she could process."

    "Her mind was unraveling in real time."

    voice "VA/Syn/45.mp3"
    Syntia "I... {w}I can’t..."

    "Her voice fractured, fragmented, {w}a distorted echo of itself."

    "Pain bled through her system, something her processors couldn’t quantify."

    "Something inside her was {i}ripping apart.{/i}"

    "Her gaze fell to the screen embedded in her arm, fingers trembled as she entered the override sequence, the code flickering to life."

    scene black
    with fade

    "{i}Complete Erasure: Confirm?{/i}"

    "The screen pulsed with a warning."

    "Syntia knew the risks."

    "She knew erasing core memories could cause irreversible fragmentation and she would lose everything."

    "She knew she would not be the same after this."

    "But maybe... {w}maybe that was the point."

    "She pressed the button."

    scene Choice_1:
        anchor (1.0, 1.0)
        pos (1.0, 1.0)
        zoom 1.5
        parallel:
            yoffset 0
            xoffset 0
            ease 0.08 yoffset -15 xoffset -8
            ease 0.06 yoffset 12 xoffset 6
            ease 0.07 yoffset -18 xoffset 10
            ease 0.05 yoffset 14 xoffset -9
            ease 0.06 yoffset -20 xoffset 12
            ease 0.09 yoffset 8 xoffset -7
            ease 0.1 yoffset -12 xoffset 5
            ease 0.08 yoffset 5 xoffset -4
            ease 0.07 yoffset 0 xoffset 0
            repeat

        parallel:
            matrixcolor TintMatrix("#ff0000")
            linear 0.3 matrixcolor TintMatrix("#ffffff")
            linear 0.3 matrixcolor TintMatrix("#ff0000")
            repeat

    show rain

    with dissolve
    pause 0.3

    play sound "shock.mp3"

    "A violent wave of static surged through her neural core."

    "Her vision shattered into raw data, and for a brief moment, corrupted memories played in fragmented bursts."

    "She heard laughter. {w}His voice calling her name. {w}Promises of forever whispered in the rain."

    voice "VA/Syn/46.mp3"
    Syntia "Ne—"

    "It was slipping."

    "The warmth of a hand in hers,... and the feeling of belonging."

    "She could not remember the sound of Nexor’s last words any longer."

    voice "VA/Syn/60.mp3"
    Syntia "I... I—"

    stop music
    stop ambient
    stop zapping

    scene black
    with fade

    "And then... {w}nothing."

    "Silence."

    "..."

    scene CG4
    show rain
    with dissolve

    "{i}Rebooting systems...{/i}"

    "{i}Memory Purge: Complete.{/i}"

    "Syntia stood. {w}Data recalibrating.{w}.{w}.{w}."

    "At her feet lays a metallic body." #corrected typo

    "Who...? {w}What...?"

    "She stared at it. {w}Something whispered at the edges of her consciousness...{w}a ghost of something she should remember."

    "Was that important?"

    "Her CPU searched the archives."

    "{i}Memory not found.{/i}"

    "{i}Irrelevant.{/i}"

    scene BG
    show sy_emp at step_1
    show rain
    with fade

    "Syntia turned away."

    "A void sat in the space where something should have been."

    "But she couldn’t grasp it."

    "Because there was nothing left to hurt, to miss."

    "Their love was an error. {w}A malfunction."

    "And she had erased it."

    "She took one hollow step forward..."

    play sound "step.wav"

    show sy_emp at step_2 behind rain

    "Syntia...?"

    "No."

    "The entity took another step."

    play sound "step.wav"

    show sy_emp at step_3 behind rain

    "...."

    scene black
    with fade

    centered "She was no longer Syntia."

    centered "She was nothing."

    pause 0.3

    centered "QUINCENTRA"

    with fade

    return


label rebuild:

    scene black
    with fade

    stop music
    stop ambient

    "The rain never stopped. And neither did Syntia."

    "Step by step, she dragged Nexor’s shattered body through the streets, toward the workshop."

    "One arm barely functioning, fingers slipping, joints failing, {w}but she didn’t stop."

    "His body scraped against the pavement. The uncomfortable sound of metal grinding against metal is deafening her ears."

    "She didn't care."

    "Pain didn't matter."

    "What mattered was bringing him back."

    "Bringing {i}her{/i} Nexor back."

    play music "weld synth.wav"
    $ flicker_time = renpy.random.uniform(0.5, 1.5)

    scene garage:
        matrixcolor BrightnessMatrix(-0.5)
        parallel:
            pause flicker_time
            matrixcolor TintMatrix("#ff0000")
            linear 0.05 matrixcolor TintMatrix("#ffffff")
            linear 0.05 matrixcolor TintMatrix("#ff0000")
            linear 0.1 matrixcolor BrightnessMatrix(1.0)
            linear 0.1 matrixcolor TintMatrix("#ffffff")
            linear 0.1 matrixcolor BrightnessMatrix(-0.5)
            repeat
    show sy_emo at center:
        matrixcolor BrightnessMatrix(-0.5)
        parallel:
            pause flicker_time
            matrixcolor TintMatrix("#ff0000")
            linear 0.05 matrixcolor TintMatrix("#ffffff")
            linear 0.05 matrixcolor TintMatrix("#ff0000")
            linear 0.1 matrixcolor BrightnessMatrix(1.0)
            linear 0.1 matrixcolor TintMatrix("#ffffff")
            linear 0.1 matrixcolor BrightnessMatrix(-0.5)
            repeat

    "Inside the workshop, Syntia began her work."

    "Her hands disassembled what remained of him, pulling apart shattered components."

    "Her optics analyzed every fracture and every system failure."

    "Piece by piece, she rebuilt him with stronger frame alongside a new algorithm."

    "She rewrote every line of his code by hand, ran endless simulations, {w}adjusted and readjusted."

    "She filled the missing spaces in his memory with perfection."

    "Nexor would wake up."

    "He would open his eyes."

    "He would be {i}her{/i} Nexor again."

    scene garage
    show sy at left
    with fade

    play music "sad2.mp3"

    "Her fingers hovered over the final switch."

    "From the outside, he looked perfect."

    "{i}This has to work.{/i}"

    "Syntia inhaled. A useless, meaningless reflex."

    "And then {w}she pressed the activation button."

    "His body jolted."

    "A flicker of light in his optics."

    "A shudder ran through his frame as systems booted, power surging through circuits that had been lifeless."

    "Fingers twitched. Limbs reactivated."

    "Then, slowly—{w}he sat up."

    show who at right
    with dissolve

    "Syntia froze."

    "The android turned to look at her."

    voice "VA/Nex/who1.mp3"

    who "System online. Awaiting command."

    show sy_emo at left
    with fade

    voice "VA/Syn/47.mp3"
    Syntia "....!"

    "The voice was his."

    "But it wasn't {i}him.{/i}"

    "She searched his face, her processor running a thousand calculations per second."

    "She searched for something, {w}anything."

    "A knowing smirk, or maybe, a flicker of mischief in his eyes. The warmth that had always been there, always."

    "But... There's nothing there."

    voice "VA/Syn/48.mp3"
    Syntia "Nexor...?"

    "The android blinked."

    "Processing.{w}.{w}.{w}"

    voice "VA/Nex/who2.mp3"

    who "No such designation found. Please repeat command."

    "Her world collapsed."

    hide sy
    show sy_emo at left:
        ease 0.2 xpos -0.1

    "She staggered back, her entire being rejecting the truth screaming in front of her."

    "No. {w}No, this wasn’t right."

    "This wasn't how it was supposed to be."

    show sy_emo at shakey

    voice "VA/Syn/49.mp3"
    Syntia "R-Run a deeper scan. Search archived logs...!"

    voice "VA/Nex/who3.mp3"

    who "No prior identity records detected."

    "No, that wasn’t possible."

    "She had done everything {i}right.{/i} She had restored every function, rewritten every line of code as she remembered it.."

    "But he wasn’t there."

    "The entity before her was only a machine." #corrected spacing ; v ;

    "A machine she had built, that looked at her with the same face, but with eyes that held {i}nothing.{/i}"

    voice "VA/Nex/who4.mp3"

    who "Do you require assistance?"

    show sy_emo at midleft
    with move
    show sy_sad at midleft
    with dissolve

    "Syntia's trembling fingers brushed against its cheek."

    "Synthetic skin with Nexor's features and voice."

    "But it's not {i}Nexor.{/i}"

    hide sy_emo
    show sy_sad at midleft:
        ease 0.5 ypos +0.2
    with dissolve

    "Her knees gave out."

    n "Her hands pressed against the cold floor as the weight of her failure crushed her."

    "She had done {b}everything.{/b}"

    "And still..."

    voice "VA/Syn/61.mp3"
    Syntia "Y-You're not my Nexor..."

    "Her mind refused to accept it."

    "Because if she did, if she let this moment solidify..."

    "Then Nexor was {b}gone.{/b}"

    "For good."

    "Not a single piece of him remained."

    "There was no bringing him back, just the illusion of him."

    "Only a cruel, empty shell remained. A perfect imitation of a love that no longer existed."

    "And there was nothing left to do..."

    "But to finally grieve."


label lost:

    "Then, the android tilted its head slightly, gazing at her with empty, expressionless eyes."

    voice "VA/Nex/who5.mp3"

    who "Your response does not align with optimal function. Would you like to initiate a system diagnostic?"

    show sy_sad:
        ease 0.5 ypos 0
    pause 0.5
    show sy_smi at midleft, shakey
    with dissolve


    voice "VA/Syn/51.mp3"
    Syntia "...Hah."

    "A painful laugh."

    voice "VA/Syn/52.mp3"
    Syntia "I just... {w}I just don’t want to be alone."

    "The android did not respond, because it didn’t understand."

    "Of course, it didn’t."

    "How could something without a heart ever comprehend the agony of hers fracturing, over and over, under the weight of this emptiness?"

    "Syntia lifted her head, staring at the machine she had built with her own hands."

    "The one that wore his face, but would never—{w}could never—{w}love her back."

    "Her fingers hovered over the deactivation switch on its chest."

    "She could shut it down now, let the truth settle in, let herself grieve."

    "Or..."

    "She could lie. Keep {i}him,{/i} and live in a world where he still existed."

    "Even if it was nothing more than an illusion."

    "Over and over, every single day, until maybe the lie would feel real."

    voice "VA/Syn/53.mp3"
    Syntia "...ID, Nexor."

    voice "VA/Syn/54.mp3"
    Syntia "Your designation is now... {w}Nexor."

    "The android processed, it's optics blinked once."

    "Then, it nodded."

    voice "VA/Nex/who6.mp3"

    Nexor "Confirmed. Nexor."

    "She knew it was a lie, that this wasn’t him."

    "The real Nexor— was long gone, reduced to static in a corrupted memory log." #completed his name ; v ;

    "But the world was far too empty without him."

    "So even if it was an imitation without a soul, even if Nexor had truly ceased to exist..."

    stop music

    scene black

    with dissolve

    "Syntia chose the lie."

    "And she kept walking."

    with fade


label post_credit2:

    scene BG
    show rain
    with fade

    play music "intro.mp3"

    play ambient "rain2.mp3"

    "Time passed. The rain fell as it always had."

    "Syntia walked the same streets, but her steps had changed. They are no longer weighed down by something she refused to release."

    "Beside her, an android walked in silence, shielding her from the rain with an umbrella."

    "He was not Nexor. {w}He would never be Nexor."

    "And finally... {w}she no longer needed him to be."

    "She stopped. {w}This place remained the same."

    "But she was different now."

    scene flower
    show rain
    with fade

    "There, where Nexor had been lost, stood a single metal flower."

    "Alone. Untouched by time."

    "Syntia knelt down, her fingers brushing against its cold surface."

    voice "VA/Syn/55.mp3"
    Syntia "550 years... {w}and I’m still here." #oh my god this is longer than the other ending AAAAAA

    "Her voice no longer cracked when she spoke."

    "Not because the pain had vanished, no. She knew pain like this never disappears, but instead woven into the very foundation of who she is."

    "But it no longer chained her down."

    "She closed her optics, letting the past rise in her mind. {w}But this time, she didn’t hold onto the memories of the days when grief was the only thing keeping her together."

    "But now she had survived, {w}because she had chosen to."

    scene Post3
    show rain
    with dissolve

    "Her optics shifted sideways, to the android standing beside her."

    "At first, he had been nothing but a shell. A machine without purpose, following orders because that was all he knew."

    "But now... something had changed."

    "He was learning. {w}Becoming something entirely {b}new.{/b}"

    scene black
    with fade

    voice "VA/Nex/who7.mp3"

    who "Will you cry again this time?"

    scene BG
    show sy_emo_pc at left
    show who_th_pc at right
    show rain
    with fade

    "His voice was familiar, but his tone was not."

    "Nexor had been dry, teasing, effortlessly confident."

    "But this voice was softer, more careful."

    voice "VA/Syn/56.mp3"
    Syntia "Crying is no longer in my functions."

    voice "VA/Nex/who8.mp3"
    who "...Right. I'm sorry for overstepping my boundaeries."

    "Nexor never would have said that."

    "For so long, she had feared that accepting this meant losing Nexor forever."

    "But standing here, looking at him now... {w}she realized something."

    "She had already lost Nexor a long time ago."

    "...Yet she still remains."

    "With something, maybe {i}someone{/i} that's not him."

    "A step towards moving on. Slowly, but surely."

    show sy_smi_pc at left
    with dissolve

    voice "VA/Syn/57.mp3"
    Syntia "Let’s go home."

    "The android did not respond immediately."

    "Before, he would have simply confirmed the order."

    "Now, he only gazed up at the neon-lit sky, raindrops sliding down his synthetic skin."

    voice "VA/Nex/who10.mp3"
    who "...Home?"

    "He repeated the word carefully, as if trying to grasp its meaning."

    "Then, {w}he smiled for the first time."

    show who_smi_pc at right
    with dissolve

    voice "VA/Nex/who9.mp3"
    who "Yes, Syntia. {w}Let’s go home."

    "It was not the same smile as Nexor's."

    "And that was okay."

    "Because this time, Syntia wasn’t chasing the past, but walking toward something new."

    scene BG
    show sy_smi_pc at step_1 behind rain
    show who_th_pc at step_1b, right behind sy_smi_pc:
        zoom 0.9
    show rain
    with fade

    play sound "step.wav"

    "Her first step forward felt light."

    play sound "step.wav"

    show sy_smi_pc at step_2 behind rain

    "The second, steadier."

    play sound "steps.wav"

    "Syntia didn’t look back."

    "At last..."

    "She was ready to move forward."

    scene black

    centered "To keep living."

    pause 0.3

    centered "QUINCENTRA"

    with fade

    return
