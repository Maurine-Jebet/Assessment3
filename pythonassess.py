# 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# sudo:In my inputs i will need the author of the book and because the stories are from
# different language i wil need local languages and lastly the age group that
# each story telling book is targeting.
# my process will be creating a class that will therefore have some attributes and then i will
# create methods

class stories:
   def__init__(self,author,local_language,age_group)
   self.author = author
   self.local_language = local_language
   self.age_group= age_group


   def predict_story(self):
      if f"{self.author} wrote the book using {self.language} and is of{self.age_group}":
         return"The story is about the lost monkey in the desert"
      else:
         return"This book do not exist"
   def predict_title_name(self):
      if f"{self.author} wrote this book and has{self.language}":
         return"The title of the book is Blossoms of the savannah"  
      else:
         return"The title of the book is not known"
      
      
      




# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# sudo: inputs= 1.Recipe,country.
#       output= 2.Output which African country uses what type of recipe and at what time.
#       process=3.Create a class,attributes and methods.
class africa:
    def__init__(self,ingredients,time,method,nutritional_information)
    self.ingredients=ingredients
    self.time=time
    self.method = method
    self.nutritional_information =nutritional_information 

    def kenyan_recipe(self):

        if f"{self.ingredients} is cooked at{self.time} and{self.method} is used whereby it has {self.nutrition} then it is Ugali":
          return "Kenyan food which is ugali will be cooked"
        elif f"{self.ingredients}is cooked at{self.time}and {self.method}is not used and does not have {self.nutrition} it is Ethiopian food":
           return"Ethiopian githeri is cooked"
        else:
           return"No food is being cooked"
# africa=Africa(Uganda,ugali)
print(africa)
    
     
# 3. **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

class animals():
   def__init__(self,food,climate,population,)
   self.food= food
   self.climate = climate
   self.population= population

   def migration_specie(self):
      if f" there is {self.population} in the park and the climate is{self.climate} the amount of prey will be{self.population}because predators lack food ":
         return"herbivores will reduce because the carnivore feen on them"
      else:
         return"herbivores will not be eaten by prey"
print(migration_specie);     








# 4. **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.

# Sudo
#I will first take the number of the artist,names of the countries ,and the time
#  that each will be presented as my inputs.My outputs will be at what time which 
# artists will be performing and from which country.My process is to create a class ,
# attriutes and methods that i will use.

class festival():
   def__init__(self,stage,artist,presentations,country_name)
   self.stage=stage
   self.artist=artist
   self.presentations= presentations
   self.country_name= country_name

def predict_country(festival):
   if f"{self.artist} from {self.country} is presenting then he should have{self.presentations} and should perform at {self.stagr}":
      return"The performance should be from Kenya" 


def predict_style(festival):
   self.style
   if f"{self.style} is done by {self.country} at {self.time}":
      return"The performance was awesome"
   




