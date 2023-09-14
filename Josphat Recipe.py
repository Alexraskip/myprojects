recipe = {
    "title": "Spaghetti Carbonara",
    "ingredients": [
        "200g spaghetti",
        "100g guanciale or pancetta, diced",
        "2 large eggs",
        "50g Pecorino Romano cheese, grated",
        "50g Parmesan cheese, grated",
        "2 cloves garlic, minced",
        "Freshly ground black pepper",
        "Salt",
    ],
    "instructions": [
        "Bring a large pot of salted water to a boil and cook spaghetti according to package instructions until al dente.",
        "In a separate pan, cook the diced guanciale or pancetta until crispy. Remove excess fat if needed.",
        "In a bowl, whisk together the eggs, grated Pecorino Romano cheese, and grated Parmesan cheese. Season with black pepper.",
        "When the spaghetti is cooked, reserve a cup of pasta water, then drain the spaghetti.",
        "Quickly toss the hot, drained spaghetti with the crispy guanciale or pancetta in the pan to coat.",
        "Remove the pan from heat and immediately pour the egg and cheese mixture over the pasta. Toss quickly to combine, using reserved pasta water to achieve a creamy consistency.",
        "Serve immediately with additional grated cheese and black pepper as garnish.",
    ],
    "prep_time": "10 minutes",
    "cook_time": "15 minutes",
    "total_time": "25 minutes",
    "serving_size": "2",
}

# Printing the recipe
print("Recipe:", recipe["title"])
print("Ingredients:")
for ingredient in recipe["ingredients"]:
    print("-", ingredient)
print("Instructions:")
for step, instruction in enumerate(recipe["instructions"], start=1):
    print(f"{step}. {instruction}")
print("Preparation Time:", recipe["prep_time"])
print("Cooking Time:", recipe["cook_time"])
print("Total Time:", recipe["total_time"])
print("Serving Size:", recipe["serving_size"])
