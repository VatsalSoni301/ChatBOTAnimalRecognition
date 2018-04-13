
# from builtins import print
import datetime
import pprint
import time

import telebot
from telebot import types
import os

API_TOKEN = '469509215:AAHCAF2jI5CsEpJFUzG6WhRKLbpJIuVN9vw'
bot = telebot.TeleBot(API_TOKEN)

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
hideBoard = types.ReplyKeyboardRemove()


@bot.message_handler(content_types='photo')
def photo(message):
    bot.send_message(message.chat.id,"Wait for 35 seconds")
    fileId=message.photo[-1].file_id
    name=fileId+".jpg"
    file_info = bot.get_file(fileId)
    print('file.file_path =', file_info.file_path)
    downloaded_file=bot.download_file(file_info.file_path)
    with open("data/"+name,'wb') as new_file:
        new_file.write(downloaded_file)
    ans='./darknet detect cfg/yolo.cfg yolo.weights'+' '+'data/'+name
    result=os.popen(str(ans)).read()
    i=-1
    n=0
    name=''
    final_per=''
    while 'seconds' not in result.split()[i]:
	per=result.split()[i]
        no=per.split("%")
        print no[0]
	if no[0] > n:
	   n=no[0]
           final_per=per
           name=result.split()[i-1]
	   print(name+final_per)
        i=i-2
    ans_ans=name+final_per
    #per=result.split()[-1]
    #test=result.split()[-3]
    #result=result.split()[-2]+result.split()[-1]
    #if 'animal' in result:
	#result='Not Animal'+':'+per
    
    bot.send_message(message.chat.id,ans_ans)


@bot.message_handler(commands=['Help', 'help'])
def start(message):
    ans = '/dog : Get info about dog \n' \
          '/cat : Get info about cat \n' \
          '/sheep : Get info about sheep \n' \
          '/cow : Get info about cow \n' \
          '/horse : Get info about horse \n' \
          '/elephant : Get info about elephant \n' \
          '/bear : Get info about bear \n' \
          '/zebra : Get info about zebra \n' \
          '/giraffe : Get info about giraffe'
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Dog', 'dog'])
def dog_method(message):
    ans = 'Dogs have four legs and make a "bark," "woof," or "arf" sound. Dogs often chase cats, and most dogs will fetch a ball or stick.' \
          'Dogs can smell and hear better than humans, but cannot see well in color because they are color blind. Due to the anatomy of the eye, ' \
          'dogs can see better in dim light than humans. They also have a wider field of vision. ' \
          'Like wolves, wild dogs travel in groups called packs. Packs of dogs are ordered by rank, ' \
          'and dogs with low rank will submit to other dogs with higher rank. The highest ranked dog is called the ' \
          'alpha male. A dog in a group helps and cares for others. Domesticated dogs often view their owner as the alpha male.'
    bot.send_photo(message.chat.id,open('Sample/dog.jpg','rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Cat', 'cat'])
def cat_method(message):
    ans = 'Cats are similar in anatomy to the other felids, with a strong flexible body, quick reflexes, ' \
          'sharp retractable claws and teeth adapted to killing small prey. Cat senses fit a crepuscular ' \
          'and predatory ecological niche. Cats can hear sounds too faint or too high in frequency for' \
          ' human ears, such as those made by mice and other small animals. They can see in near darkness. ' \
          'Like most other mammals, cats have poorer color vision and a better sense of smell than humans.' \
          ' Cats, despite being solitary hunters, are a social species, and cat communication includes the ' \
          'use of a variety of vocalizations (mewing, purring, trilling, hissing, growling and grunting) as ' \
          'well as cat pheromones and types of cat-specific body language.'
    bot.send_photo(message.chat.id, open('Sample/cat.jpg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Horse', 'horse'])
def horse_method(message):
    ans = 'Most breeds of horses are able to perform work such as carrying humans on their backs' \
          ' or be harnessed to pull objects such as carts or plows. However, horse breeds were ' \
          'developed to allow horses to be specialized for certain tasks. Lighter horses were bred' \
          ' for racing or riding, heavier horses for farming and other tasks requiring pulling power.' \
          ' Some horses, such as the miniature horse, can be kept as pets.The horse plays a prominent' \
          ' role as a figure in the ideals of religion and art and plays an important role in' \
          ' transportation, agriculture and warfare. '
    bot.send_photo(message.chat.id, open('Sample/horse.jpeg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['sheep', 'sheep'])
def sheep_method(message):
    ans = 'Domestic sheep are relatively small ruminants, typically with horns forming a lateral' \
          ' spiral and crimped hair called wool. A sheep is an animal which has a thick coat of ' \
          'fleece on its body. Another trait unique to sheep are their wide variation in colour.' \
          ' Wild sheep are largely variations of brown hues. Colours of domestic sheep range from pure' \
          ' white to dark chocolate brown and even spotted or piebald. Selection for easily dyeable' \
          ' white fleeces began early in sheep domestication and as white wool is a dominant trait' \
          ' it spread quickly. However, coloured sheep do appear in many modern breeds and may even' \
          ' appear as a recessive trait in white flocks.Depending on breed, sheep show a range of' \
          ' heights and weights. Their rate of growth and mature weight is often selected for in' \
          ' breeding. Ewes typically weigh between 100 and 225 pounds (45 - 100 kg), with the larger' \
          ' rams between 100 and 350 pounds (45 - 160 kg). Mature sheep have 32 teeth. As with other' \
          ' ruminants, the eight incisors are in the lower jaw and bite against a hard, toothless' \
          ' pad in the upper jaw, picking off vegetation. Sheep have no canines, instead there' \
          ' is a large gap instead between the incisors and the premolars. Until the age of four' \
          ' (when all the adult teeth have erupted), it is possible to see the age of sheep' \
          ' from their front teeth, as a pair of incisors erupts each year.'
    bot.send_photo(message.chat.id, open('Sample/sheep.jpeg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Cow', 'cow'])
def cow_method(message):
    ans = 'Cows are raised for many reasons including: milk, cheese, other dairy products, also' \
          ' for meat such as beef and veal and materials such as leather hide. In older times they ' \
          'were used as work animals to pull carts and to plow fields.In some countries such as' \
          ' India, cows were classed as sacred animals and were used in religious ceremonies and' \
          ' treated with much respect.Today, cows are domesticated ungulates (hoofed animals with' \
          ' two toes on each hoof) that we see very often chewing the grass in farmers fields as' \
          ' we walk or drive through the countryside.There is an estimated 1.3 billion head of' \
          ' cattle and 920 breeds of cow in the world today. Cows are referred to as the fosters' \
          ' mothers to the human race because they produce most of the milk that people drink.'
    bot.send_photo(message.chat.id, open('Sample/cow.jpg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Elephant', 'elephant'])
def elephant_method(message):
    ans = 'Elephants are scattered throughout sub-Saharan Africa, South Asia, and Southeast Asia. ' \
          'Elephantidae is the only surviving family of the order Proboscidea; other, now extinct, ' \
          'members of the order include deinotheres, gomphotheres, mammoths, and mastodons. ' \
          'All elephants have several distinctive features, the most notable of which is a long trunk ' \
          '(also called a proboscis), used for many purposes, particularly breathing, lifting water, ' \
          'and grasping objects. Their incisors grow into tusks, which can serve as weapons and as tools' \
          ' for moving objects and digging. Elephants large ear flaps help to control their body ' \
          'temperature. Their pillar-like legs can carry their great weight. African elephants have ' \
          'larger ears and concave backs while Asian elephants have smaller ears and convex or level backs. ' \
          'Elephants are herbivorous and can be found in different habitats including savannahs, forests, ' \
          'deserts, and marshes. They prefer to stay near water. They are considered to be keystone ' \
          'species due to their impact on their environments. Other animals tend to keep their distance ' \
          'from elephants while predators, such as lions, tigers, hyenas, and any wild dogs, usually ' \
          'target only young elephants (or "calves"). Elephants have a fission-fusion society in which ' \
          'multiple family groups come together to socialise.'
    bot.send_photo(message.chat.id, open('Sample/elephant.jpeg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Bear', 'bear'])
def bear_method(message):
    ans = 'Bears are found on the continents of North America, South America, Europe, and Asia.' \
          ' Common characteristics of modern bears include large bodies with stocky legs, long snouts,' \
          ' small rounded ears, shaggy hair, plantigrade paws with five nonretractile claws, and short' \
          ' tails.While the polar bear is mostly carnivorous, and the giant panda feeds almost' \
          ' entirely on bamboo, the remaining six species are omnivorous with varied diets. With' \
          ' the exception of courting individuals and mothers with their young, bears are typically' \
          ' solitary animals. They may be diurnal or nocturnal and have an excellent sense of smell.' \
          ' Despite their heavy build and awkward gait, they are adept runners, climbers, and swimmers.' \
          ' Bears use shelters, such as caves and logs, as their dens; most species occupy their dens' \
          ' during the winter for a long period of hibernation, up to 100 days.Bears have been hunted' \
          ' since prehistoric times for their meat and fur; they have been used for bear-baiting and' \
          ' other forms of entertainment, such as being made to dance. With their powerful physical' \
          ' presence, they play a prominent role in the arts, mythology, and other cultural aspects' \
          ' of various human societies. In modern times, bears have come under pressure through ' \
          'encroachment on their habitats and illegal trade in bear parts, including the Asian bile' \
          ' bear market. The IUCN lists six bear species as vulnerable or endangered, and even least' \
          ' concern species, such as the brown bear, are at risk of extirpation in certain countries.' \
          ' The poaching and international trade of these most threatened populations are prohibited,' \
          ' but still ongoing.'
    bot.send_photo(message.chat.id, open('Sample/bear.jpeg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Zebra', 'zebra'])
def zebra_method(message):
    ans = 'Zebras are equids - members of the horse family (Equidae) and are medium sized, odd-toed' \
          ' ungulates. Zebras are native to southern and central Africa. Although zebras are very' \
          ' adaptable animals as far as their habitats are concerned, most zebras live in grasslands' \
          ' and savannas. The Grevy zebra (Equus grevyi) prefers to live in sub desert and arid' \
          ' grasslands.Zebras were the second species to diverge from the earliest proto-horses,' \
          ' after the asses, around 4 million years ago. The Grevy zebra is believed to have' \
          ' been the first zebra species to emerge.'
    bot.send_photo(message.chat.id, open('Sample/zebra.jpeg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['Giraffe', 'giraffe'])
def giraffe_method(message):
    ans = 'The Giraffe (Giraffa camelopardalis meaning fast walking camel leopard) is an African' \
          ' even-toed ungulate mammal, the tallest of all land-living animal species.The giraffe is ' \
          'related to deer and cattle, however, it is placed in a separate family, the Giraffidae,' \
          ' consisting only of the giraffe and its closest relative, the okapi.The giraffes range' \
          ' extends from Chad to South Africa. Although the Okapi is much shorter than the giraffe,' \
          ' it also has a long neck and eats leaves and both animals have long tongues and skin-covered' \
          ' horns. The giraffes ancestors first appeared in central Asia about 15 million years ago,' \
          ' however, the earliest fossil records of the giraffe itself, from Israel and Africa, date' \
          ' back about 1.5 million years.Male giraffes are called Bulls, female giraffes are called' \
          ' Cows and baby giraffes are called Calves.'
    bot.send_photo(message.chat.id, open('Sample/giraffe.jpeg', 'rb'))
    bot.send_message(message.chat.id, ans)


@bot.message_handler(content_types='text')
def additional(message):
    ans = 'Command does not recognized. Please enter valid command or use /help command to know about commands.'
    bot.send_message(message.chat.id, ans)


bot.polling()
