from random import random, randint, choice
from time import sleep

class Pet():
    def __init__(self, name, rarity, damage):
        self.name = name
        self.rarity = rarity
        self.damage = damage

class Coins():
    def __init__(self, name, health, cashout, gemsout):
        self.name = name
        self.health = health
        self.cashout = cashout
        self.gemsout = gemsout

class Game():
    def __init__(self, name, hp, cash, inventory, totalDamage, damagePotion, coinPotion, leveldmgpotion, levelcoinpotion, gems, multiple, lvl, custom):
        self.name = name
        self.hp = hp
        self.cash = cash
        self.inventory = inventory
        self.pets = []
        self.totalDamage = totalDamage
        self.damagePotion = damagePotion
        self.coinPotion = coinPotion
        self.leveldmgpotion = leveldmgpotion
        self.levelcoinpotion = levelcoinpotion
        self.gems = gems
        self.multiple = multiple
        self.lvl = lvl
        self.custom = custom

    def tutorial(self):
        print('Добро ласкаво до гри Pet Simulator!\n')
        sleep(1)
        print('В тебе на балансі 100 монеток першим ділом піди купи пета а потім йди збирай монетки Потім ти піймеш як грати\n')
        plr.menu()

    def menu(self):
        print('')
        print('Меню:')
        print('1. Піти в магазин')
        print('2. Піти збирати монетки/геми')
        print('3. Подивитись інвентар')
        print('4. Подивитись баланс')
        print('5. Подивитись загальний урон петів')
        print('6. Вийти\n')
        choice = input('Оберіть опцію: ')
        if choice == '1':
            sleep(0.75)
            self.shop()
        elif choice == '2':
            sleep(0.75)
            self.collectCoins()
        elif choice == '3':
            sleep(0.75)
            print('')
            print('Пети гравця:', [(pet.name, pet.rarity, pet.damage) for pet in plr.pets])
            print('')
            sleep(0.75)
            plr.menu()
        elif choice == '4':
            sleep(0.75)
            print(f'Ваш баланс грошей: {self.cash}$')
            print(f'Ваш баланс гемів: {self.gems} гемів\n')
            sleep(0.75)
            plr.menu()
        elif choice == '5':
            sleep(0.75)
            print(f'Загальний урон петів: {plr.totalDamage} ДМГ\n')
            sleep(0.75)
            plr.menu()
        elif choice == '6':
            sleep(0.75)
            print('До побачення!')
        elif choice == '09000111221':
            sleep(2)
            plr.secretShop()
        elif choice == 'LogikaTheBest':
            sleep(2)
            plr.adminPanel()
        else:
            print('Невірний вибір.')
            sleep(0.75)
            plr.menu()

    def collectCoins(self):
        Coin = [Coins('Маленька Монетка',245,65,3), Coins('Середня Монетка',500,120,7), Coins('Велика Монетка',1000,245,12), Coins('Скриня з монетками',5000,650,20), Coins('Маленька жила гемів',120,0,15), Coins('Середня жила гемів',240,0,30), Coins('Середня жила гемів',240,0,30), Coins('Велика жила гемів',900,0,50), Coins('Скриня з гемами',3000,0,175)]
        setCoin = choice(Coin)
        print(f'Ти помітив {setCoin.name}!\nВін має {setCoin.health} Здоровя\nЗа знищення дає {setCoin.cashout}$ і {setCoin.gemsout} гемів!')
        self.attackCoin(setCoin)

    def attackCoin(self, setCoin):
        actionchoice = input('Чи хочеш атакувати цю монетку/гем? (1. Так 2. Ні 3. Авто майнинг 4. Вийти в головне меню)')
        if actionchoice == '1':
            while setCoin.health >= 0:
                setCoin.health -= plr.totalDamage
                sleep(0.5)
                if plr.totalDamage == 0:
                    print('У вас нема петів! Ви не зможете атакувати цю монетку або гем, будьласка купіть собі пета в магазині\n')
                    sleep(0.6)
                    plr.menu()
                else:
                    print(f'{setCoin.name} має {setCoin.health} хп!\n')
            self.cash += setCoin.cashout * self.coinPotion
            self.gems += setCoin.gemsout
            print(f'Ти знищив цю монетку/гем тепер твій баланс: {self.cash}$, А гемів: {self.gems}\n')
            plr.menu()
        elif actionchoice == '2':
            print('Ви вирішили скіпнути цю монетку/гем...\n')
            plr.collectCoins()
        elif actionchoice == '3':
            autoFarm = int(input('Скільки раз ви б хотіли фармити монети/геми (Введіть число наприклад 3, тоді пети зламають 3 рази монетки)'))
            i = 1
            totalcash = 0
            totalgems = 0
            if autoFarm > 10000:
                for i in range(autoFarm):
                    Coin = [Coins('Маленька Монетка',245,65,3), Coins('Середня Монетка',500,120,7), Coins('Велика Монетка',1000,245,12), Coins('Скриня з монетками',5000,650,20), Coins('Маленька жила гемів',120,0,15), Coins('Середня жила гемів',240,0,30), Coins('Середня жила гемів',240,0,30), Coins('Велика жила гемів',900,0,50), Coins('Скриня з гемами',3000,0,175)]
                    setCoin = choice(Coin)
                    print(f'Ви помітили {setCoin.name}\nВ нього {setCoin.health} здоровя\nЗа знищення дає {setCoin.cashout}$ і {setCoin.gemsout} гемів!\n')
                    while setCoin.health >= 0:
                        setCoin.health -= plr.totalDamage
                        sleep(0.5)
                        if plr.totalDamage == 0:
                            print('У вас нема петів! Ви не зможете атакувати цю монетку або гем, будьласка купіть собі пета в магазині\n')
                            sleep(0.6)
                            plr.menu()
                        else:
                            print(f'{setCoin.name} має {setCoin.health} здоровя!')
                    self.cash += setCoin.cashout
                    self.gems += setCoin.gemsout
                    totalcash += setCoin.cashout
                    totalgems += setCoin.gemsout
                print(f'За цей час ви назбирали: {totalcash} грошей і {totalgems} гемів!\nТепер ваш баланс: {self.cash}$ і {self.gems} гемів!\n')
                sleep(0.4)
                plr.menu()
            else:
                print("Занадто багато спроб")
                plr.menu()
        elif actionchoice == '4':
            plr.menu()
        else:
            print('Я не розумію що ти написав')
            plr.attackCoin(setCoin)

    def shop(self):
        print('Ви у магазині. Що бажаєте придбати? (1. Петів 2. Зілля)')
        shopchoice = input('')
        if shopchoice == '1':
            plr.buyEgg()
        elif shopchoice == '2':
            plr.potionShop()
        else:
            print('Напишіть точніше')
            plr.menu()

    def buyEgg(self):
        commonEgg = [Pet('Кіт', 'Коммон', 10), Pet('Собака', 'Коммон', 15), Pet('Качка', 'Рідка', 20)]
        commonEggPrice = 100
        RareEgg = [Pet('Гусь', 'Рідка', 21), Pet('Змія', 'Рідка', 24), Pet('Миша', 'Сверхрідка', 30)]
        RareEggPrice = 500
        EpicEgg = [Pet('Пень', 'Сверхрідка', 34), Pet('Тарілка', 'Епік', 40), Pet('Банка', 'Епік', 55)]
        EpicEggPrice = 1500
        LegendaryEgg = [Pet('Камінь', 'Епік', 67), Pet('Вилка', 'Епік', 75), Pet('Шина від колеса', 'Легендарний', 80)]
        LegendaryEggPrice = 5000

        choiceEgg = input('Яке яйце ви хочите відкрити?\n1. Common Egg\nЦіна: 100$\n2. Rare egg\nЦіна: 500\n3. Epic Egg\nЦіна: 1500$\n4. Legendary Egg\nЦіна: 5000$\n')
        if choiceEgg == '1' and self.cash >= commonEggPrice:
            self.cash -= commonEggPrice
            pet = self.getRandomPet(commonEgg)
            if pet:
                self.addPet(pet)
                print('Яйце відчиняється...\n')
                sleep(2)
                print(f'Ви отримали пета: {pet.name}!\n')
                plr.totalDamage += pet.damage
                plr.menu()
            else:
                print('На жаль, вам не вдалося отримати нового пета.\n')
                plr.menu()
        elif choiceEgg == '2' and self.cash >= RareEggPrice:
            self.cash -= RareEggPrice
            pet = self.getRandomPet(RareEgg)
            if pet:
                self.addPet(pet)
                print('Яйце відчиняється...\n')
                sleep(2)
                print(f'Ви отримали пета: {pet.name}!\n')
                plr.totalDamage += pet.damage
                plr.menu()
            else:
                print('На жаль, вам не вдалося отримати нового пета.\n')
                plr.menu()
        elif choiceEgg == '3' and self.cash >= EpicEggPrice:
            self.cash -= EpicEggPrice
            pet = self.getRandomPet(EpicEgg)
            if pet:
                self.addPet(pet)
                print('Яйце відчиняється...\n')
                sleep(2)
                print(f'Ви отримали пета: {pet.name}!\n')
                plr.totalDamage += pet.damage
                plr.menu()
            else:
                print('На жаль, вам не вдалося отримати нового пета.\n')
                plr.menu()
        elif choiceEgg == '4' and self.cash >= LegendaryEggPrice:
            self.cash -= LegendaryEggPrice
            pet = self.getRandomPet(LegendaryEgg)
            if pet:
                self.addPet(pet)
                print('Яйце відчиняється...\n')
                sleep(2)
                print(f'Ви отримали пета: {pet.name}!\n')
                plr.totalDamage += pet.damage
                plr.menu()
            else:
                print('На жаль, вам не вдалося отримати нового пета.\n')
                plr.menu()
        else:
            print('Будь ласка зайдіть в магазин ще раз і введіть точніше.\n')
            plr.menu()

    def getRandomPet(self, petList):
        if random() < 1:
            return petList[randint(0, len(petList) - 1)]
        else:
            return None

    def addPet(self, pet):
        self.pets.append(pet)

    def potionShop(self):
        print('Ви в магазині зілля! Що бажаєте купити?(1. Зілля на монетки 2. Зілля на силу 3. Вийти з магазину)')
        potionChoice = input('')
        if potionChoice == '1':
            if self.levelcoinpotion == 5:
                print('Ви досягли максимального рівня зілля! Ви не зможете купити ще\n')
                plr.potionShop()
            else:
                coinprice = 200 * self.levelcoinpotion
                self.gems -= coinprice
                buyChoice = input(f'Ваш коефіціент множителя зілля {self.coinPotion} чи бажаєте його оновити за {coinprice} гемів?(1. Купити 2. Не купувати)\n')
                if buyChoice == '1' and self.gems >= coinprice:
                    self.levelcoinpotion += 1
                    self.coinPotion += 0.25
                    print('Ваша покупка обробляється...\n')
                    sleep(2)
                    print('Вітаю з покупкою!\n')
                    plr.menu()
                elif buyChoice == '2':
                    print('\nВи вирішили не купувати це зілля...\n')
                    plr.menu()
                else:
                    print('Напишіть будьласка точніше.')
                    plr.potionShop()
        elif potionChoice == '2':
            if self.leveldmgpotion == 5:
                print('Ви досягли максимального рівня зілля! Ви не зможете купити ще\n')
                plr.potionShop()
            else:
                dmgprice = 125 * self.leveldmgpotion
                buyChoice = input(f'Ваш коефіціент множителя зілля {self.damagePotion} Чи бажаєте його оновити за {dmgprice} гемів?')
                if buyChoice == '1' and self.gems >= dmgprice:
                    self.gems -= dmgprice
                    self.leveldmgpotion += 1
                    self.damagePotion += 0.5
                    print('Ваша покупка обробляється...\n')
                    sleep(2)
                    print('Вітаю з покупкою!\n')
                    plr.menu()
                elif buyChoice == '2':
                    print('\nВи вирішили не купувати це зілля...\n')
                    plr.potionShop()
        elif potionChoice == '3':
            print('Переносимо вас в меню...\n')
            sleep(1)
            plr.menu()
        else:
            sleep(1)
            plr.menu()
            
    def secretShop(self):
        print('Як ти дізнався про секретний код? Добре тут самі вигодні сділки для тебе но дорогі! Є секретне яйце в котрому самі ліпші пети в грі також є саме секретне зілля котре дає x100 множитель! Що ти купиш?\n(1. Секретне яйце 2. Секретне зілля)')
        secretChoice = input('')
        if secretChoice == '1':
            secretEgg = [Pet('Великий Кіт', 'Секретний', 999), Pet('Велика собака', 'Секретний', 999), Pet('Пет Розробника', 'Секретний', 9999)]
            secretEggPrice = 1 * self.multiple
            buySecretChoice = input(f'Яйце коштує {secretEggPrice} с кожним разом як ти його купиш ціна підвоїться!(1. Купити 2. Не купувати)')
            if buySecretChoice == '1' and self.gems >= secretEggPrice:
                pet = self.getRandomPet(secretEgg)
                plr.gems -= secretEggPrice
                if pet:
                    self.gems -= secretEggPrice
                    self.addPet(pet)
                    plr.totalDamage += pet.damage
                    print('Секретне Яйце відчиняється...\n')
                    sleep(2)
                    print(f'Ви вибили {pet.name}!\n')
                    sleep(0.8)
                    plr.menu()
                else:
                    print('Нажаль ви не вибили нового пета...\n')
                    plr.menu()
            else:
                print('Недостатньо гемів на рахунку\n')
                plr.menu()
        elif secretChoice == '2':
            if self.lvl == True:
                print('Ви вже маєте це зілля!')
                plr.menu()
            else:
                secretPotionPrice = 25000
                secretBuyChoice = input(f'Секретне Зілля коштує {secretPotionPrice} гемів, чи бажаєте його придбати?(1. Так 2. Ні)')
                if secretBuyChoice == '1' and self.gems >= secretPotionPrice:
                    plr.gems -= secretPotionPrice
                    plr.coinPotion += 100
                    plr.damagePotion += 100
                    print('Ваша покупка обробляється...\n')
                    sleep(2)
                    print('Вітаю з покупкою!\n')
                    self.lvl = True
                    plr.menu()
                elif secretBuyChoice == '2':
                    print('Ви вирішили не купляти це зілля.\n')
                    plr.menu()
                else:
                    print('Зайдіть в секретний магазин знову і введіть точніше.\n')
                    plr.menu()
        else:
            print('Зайдіть в секретний магазин знову і введіть точніше.\n')
            plr.menu()

    def adminPanel(self):
        print('Ти потрапив у адмін панель! Тут ти можеш добавити собі Гроші/Геми навіть створити власного пета!(1. Добавити гроші 2. Добавити геми 3. Створити кастомного пета 4. Вийти в головне меню')
        adminChoice = input('')
        if adminChoice == '1':
            addcash = input('Скільки грошей ти б хотів добавити на свій баланс?(Цифрами наприклад 100000 або 9999999)\n')
            print('Зачекайте секунду...\n')
            sleep(1.25)
            plr.cash += int(addcash)
            print('Ваші гроші вже на рахунку!\n')
            plr.menu()
        elif adminChoice == '2':
            addgems = input('Скільки гемів ти б хотів добавити на свій баланс?(Цифрами наприклад 100000 або 9999999)\n')
            print('Зачекайте секунду...\n')
            sleep(1.25)
            plr.gems += int(addgems)
            print('Ваші геми вже на рахунку!\n')
            plr.menu()
        elif adminChoice == '3':
            if self.custom == False:
                namepet = input('Яке імя буде в пета?(Текст)\n')
                sleep(0.3)
                rarirypet = input('Яка рідкість буде в пета?(Текст)\n')
                sleep(0.3)
                dmgpet = int(input('Скільки урона буде наносити пет?(Число)\n'))
                sleep(0.3)
                customPet = [Pet(namepet, rarirypet, dmgpet)]
                pet = self.getRandomPet(customPet)
                if pet:
                    self.addPet(pet)
                    print('Ваш кастомний пет в інвентару!\n')
                    self.totalDamage += pet.damage
                    self.custom = True
                    plr.menu()
                else:
                    print('Спробуйте ще раз зробити Кастомного пета.\n')
                    plr.menu()
            else:
                print('Ви вже зробили кастомного пета!\n')
                plr.menu()
        else:
            print('Зайдіть ще раз в адмін паель і введіть точніше.\n')
            sleep(0.4)
            plr.menu()

plr = Game('Гравець', 100, 100, 'Поприколови', 0, 1, 1, 1, 1, 0, 1, False, False)
plr.tutorial()
