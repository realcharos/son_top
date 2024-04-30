import random
def play(x):
    word = random.randint(1,x)
    print(f'''Men 1 dan {x} gacha son o'yladim.Uni toping!''')
    taxminlar = 0
    while True:
        taxminlar+=1
        number = int(input('''Son kiriting:'''))
        if word < number:
            print('''Men o'ylgan son kichikroq!''')
        elif word > number:
            print('''Men o'ylagan son kattaroq!''')
        else:
            break
    print(f'Tabriklaymiz! {taxminlar} ta taxmin bilan yutdinggiz!')
    return taxminlar

def men_topaman(x):

    input(f'''1 dan {x} gacha bo'lgan son o'ylang. Men
taxmin qilib ko'raman!''')
    urinishlar = 0
    yuqori = x
    quyi = 1
    while True:
        urinishlar+=1
        number = random.randint(quyi, yuqori)
        if 1 != yuqori:
            number = random.randint(quyi, yuqori)
        else:
            quyi ==yuqori
        javob = input(f'''Siz o'ylagan son {number} mi ? 
                    Men o'ylagan son kichikroq == '-', kattaroq=='+', 
                    agar to'g'ri bo'lsa =='t' >>>''')
        if javob == '-':
            yuqori = number - 1
        elif javob == '+':
            quyi = number + 1
        else:
            break
    print(f'''{urinishlar} urinishda topdim!''')
    return urinishlar


def oyin(x):
    yana = True
    while yana:
        taxminlar_user = play(x)
        taxminlar_pc = men_topaman(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))


oyin(13)
























