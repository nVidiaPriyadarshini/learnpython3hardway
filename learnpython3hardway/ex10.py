formatter = "{} {} {} {}"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

#fat_cat = """
#I'll do a list:
#\t* Cat food
#\t* Fishies
#\t* Catnip\n\t* Grass
#"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(formatter.format(
"I'll do a list:\n",
"\t* Cat food\n",
"\t* Fishies\n",
"\t* Catnip\n\t* Grass"
))
