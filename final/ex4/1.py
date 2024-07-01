print("Abd")
print('hello "Abd" bha')
print("hello 'Abd' bha")
# print("hello "h" bha") (error)
# print('abd 'bha' a') (error)
import re

class MyClass:
    def replace_content(self, text):
        pattern = r"\{\{([^}]+)\}\}"
        counter = 1
        replacements = []

        def replace(match):
            nonlocal counter
            nonlocal replacements
            replacement = "{{" + str(counter) + "}}"
            counter += 1
            replacements.append(match.group(1).strip().replace("object.", ""))
            return replacement

        replaced_text = re.sub(pattern, replace, text)
       # return replaced_text, replacements

my_object = MyClass()
text = "This is an example with {{content}} inside double curly braces. Also, {{object.property}} can be replaced."
replaced_text, replacements = my_object.replace_content(text)

print(replaced_text)
print(replacements)
