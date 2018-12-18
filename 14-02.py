import numpy as np


recipes_count = '360781'
recipes = ['3', '7']
elfs_recipes = [0,1]
last_recipes = ''

while recipes_count not in last_recipes:
    recipes_sum = sum([int(recipes[elf]) for elf in elfs_recipes])
    recipes.extend(list(str(recipes_sum)))
    elfs_recipes = [(elf_recipe+1+int(recipes[elf_recipe]))%len(recipes) for elf_recipe in elfs_recipes]
    last_recipes = ''.join(recipes[abs(len(recipes)-len(recipes_count))-1:])

recipes = ''.join(recipes)
print(f'{recipes_count} first appears after {len(recipes[:recipes.index(recipes_count)])} recipes')
