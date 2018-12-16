
recipes_count = '360781'
recipes = '37'
elfs_recipes = [0,1]
while len(recipes) < (int(recipes_count) + 10 + 1):
    recipes_sum = sum([int(recipes[elf]) for elf in elfs_recipes])
    recipes += str(recipes_sum)
    elfs_recipes = [(elf_recipe+1+int(recipes[elf_recipe]))%len(recipes) for elf_recipe in elfs_recipes]
print(f'Score of the ten recipes after {recipes_count}: {recipes[int(recipes_count):int(recipes_count)+10]}')
