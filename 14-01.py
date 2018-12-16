
recipes_count = 360781
recipes = [3,7]
elfs_recipes = [0,1]
while len(recipes) < (recipes_count + 10 + 1):
    recipes_sum = sum([recipes[elf] for elf in elfs_recipes])
    recipes += map(int, list(str(recipes_sum)))
    elfs_recipes = [(elf_recipe+1+recipes[elf_recipe])%len(recipes) for elf_recipe in elfs_recipes]
score = ''.join(map(str, recipes[recipes_count:recipes_count+10]))
print(f'Score of the ten recipes after {recipes_count}: {score}')
