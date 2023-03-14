"""
Main module for game
"""
import my_game_6

peremohy = my_game_6.Street('мікрорайон Перемоги')
peremohy.set_description('Один з нових мікрорайон міста, де розташований твій дім')

juvileinyi = my_game_6.Street('мікрорайон Ювілейний')
juvileinyi.set_description('Найновіший мікрорайон міста')

budivelnikiv = my_game_6.Street('мікрорайон Будівельників')
budivelnikiv.set_description('Настарший та найнебезпечніший район')

varash = my_game_6.Street('мікрорайон Вараш')
varash.set_description('Найбільший район міста')

dachi = my_game_6.Street('Дачі')
dachi.set_description('Заміський район з приватними будинками')

peremohy.available_streets(juvileinyi, 'північ')
peremohy.available_streets(budivelnikiv, 'південь')
juvileinyi.available_streets(peremohy, 'південь')
budivelnikiv.available_streets(peremohy, 'північ')
juvileinyi.available_streets(varash, 'схід')
varash.available_streets(juvileinyi, 'захід')
dachi.available_streets(budivelnikiv, 'захід')
budivelnikiv.available_streets(dachi, 'схід')

poisonous_carrot = my_game_6.Enemy('Отруйна морква')
poisonous_carrot.set_description('Отруйна морква заражає усіх, кого торкнеться, \
тож ось-ось вона наблизиться до тебе...')
poisonous_carrot.talking("Мою отруту можна нейтралізувати, здогадайся як:)")
poisonous_carrot.set_weakneas('вода')
juvileinyi.set_character(poisonous_carrot)

radioactive_hedgehog = my_game_6.Enemy('Радіоактивний їжак')
radioactive_hedgehog.set_description('Радіоактивний їжак опромінений великою дозою радіаціїї, \
доторкнувшись до нього ти можеш заразитися.')
radioactive_hedgehog.talking("Я рааааааадіаційний їжак")
radioactive_hedgehog.set_weakneas('калій йодид')
budivelnikiv.set_character(radioactive_hedgehog)

friend = my_game_6.BestFriend('Вітя')
friend.set_description('Вітя - твій накращий друг, який допоможе у боротьбі проти \
жахливих монстрів')
friend.set_power('Я можу дати тобі води, адже у місті вона вся заражена')
friend.talking('Не переживай, я допоможу!')
varash.set_character(friend)

water = my_game_6.Item('вода')
water.set_description('Очищена джерельна вода')
budivelnikiv.set_item(water)

pills = my_game_6.Item('калій йодид')
pills.set_description('Таблетки проти радіації')
dachi.set_item(pills)

pack = []
current_street = peremohy

HELP = 0
FAILURE = False
while not FAILURE:
    # actions in current room
    print("\n")
    if current_street is not None:
        current_street.information()
    else:
        print("Неправильно зазначена вулиця")
        break
    hero = current_street.get_character()
    if hero is not None:
        hero.get_description()
    if (hero == friend) and (HELP == 0):
        print(hero.get_power())
    item = current_street.get_item()
    if item is not None:
        item.get_description()

    answer = input(">>> ")
    if answer in ["північ", "південь", "захід", "схід"]:
        current_street = current_street.step(answer)
    elif answer == "поговоримо":
        if hero is not None:
            hero.get_talking()
    elif answer == "боротися":
        if hero is not None:
            print("Що ти хочеш застосувати, щоб перемогти монстра?")
            subject = input()
            if subject in pack:
                if hero.fight(subject):
                    print("Ти переміг цього монстрика!")
                    current_street.character = None
                    if hero.number_of_wins() == 2:
                        print("Вітаю! Ти виграв!!!")
                        FAILURE = True
                else:
                    print("Ти програв, тебе заразив монстр")
                    FAILURE = True
            else:
                print("У наплічнику немає " + subject)
        else:
            print("Тут немає монстрів, тож побережи свої сил для наступної боротьби")
    elif answer == "взяти":
        if item is not None:
            print("Тепер у твоєму наплічнику є " + item.get_name())
            pack.append(item.get_name())
            current_street.set_item(None)
        elif current_street == varash:
            print("Тепер у твоєму наплічнику є вода")
            pack.append("вода")
            HELP = 1
        else:
            print("На цій вулиці для тебе немає нічого")
    else:
        print("Ти впевнений, що мав на увазі " + answer + '?')
