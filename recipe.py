import streamlit as st
# Sample recipes stored locally
recipes = {
    "pasta": {
        "title": "Simple Pasta",
        "ingredients": [
            "200g pasta",
            "2 cloves garlic",
            "2 tablespoons olive oil",
            "Salt and pepper to taste",
            "Grated Parmesan cheese"
        ],
        "instructions": [
            "Cook the pasta according to the package instructions.",
            "While the pasta is cooking, heat the olive oil in a pan over medium heat.",
            "Add the garlic and sauté until fragrant, about 1-2 minutes.",
            "Drain the pasta and toss it with the garlic and olive oil.",
            "Season with salt and pepper, and serve with grated Parmesan cheese."
        ],
        "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38"
    },
    "pancakes": {
        "title": "Fluffy Pancakes",
        "ingredients": [
            "1 cup flour",
            "2 tablespoons sugar",
            "1 tablespoon baking powder",
            "1/2 teaspoon salt",
            "1 cup milk",
            "1 egg",
            "2 tablespoons melted butter"
        ],
        "instructions": [
            "In a large bowl, whisk together the flour, sugar, baking powder, and salt.",
            "In another bowl, whisk together the milk, egg, and melted butter.",
            "Pour the wet ingredients into the dry ingredients and stir until just combined.",
            "Heat a non-stick pan over medium heat and lightly grease with butter or oil.",
            "Pour 1/4 cup of batter onto the pan and cook until bubbles form on the surface.",
            "Flip the pancake and cook until golden brown on both sides.",
            "Serve warm with your favorite toppings."
        ],
        "image": "https://images.unsplash.com/photo-1588345921523-4a2cd57b50fa"
    },
    "chocolate chip cookies": {
        "title": "Chocolate Chip Cookies",
        "ingredients": [
            "1 cup unsalted butter, softened",
            "1 cup sugar",
            "1 cup brown sugar",
            "2 eggs",
            "1 teaspoon vanilla extract",
            "3 cups all-purpose flour",
            "1 teaspoon baking soda",
            "1/2 teaspoon baking powder",
            "1/2 teaspoon salt",
            "2 cups semisweet chocolate chips"
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C).",
            "Cream together the butter, sugar, and brown sugar until smooth.",
            "Beat in the eggs one at a time, then stir in the vanilla.",
            "In a separate bowl, combine the flour, baking soda, baking powder, and salt.",
            "Gradually blend the dry ingredients into the wet mixture.",
            "Stir in the chocolate chips.",
            "Drop by large spoonfuls onto ungreased baking sheets.",
            "Bake for about 10 minutes, or until edges are nicely browned."
        ],
        "image": "https://images.unsplash.com/photo-1617737461499-6f81a359cc70"
    },
    "brownies": {
        "title": "Fudgy Brownies",
        "ingredients": [
            "1/2 cup unsalted butter",
            "1 cup sugar",
            "2 large eggs",
            "1 teaspoon vanilla extract",
            "1/3 cup unsweetened cocoa powder",
            "1/2 cup all-purpose flour",
            "1/4 teaspoon salt",
            "1/4 teaspoon baking powder"
        ],
        "instructions": [
            "اوون کو 350 ڈگری فارن ہائیٹ (175 ڈگری سینٹی گریڈ) تک گرم کریں۔",
            "مکھن کو پگھلائیں اور چینی، انڈے اور ونیلا میں ہلائیں۔",
            "ایک علیحدہ پیالے میں، کوکو، آٹا، نمک، اور بیکنگ پاؤڈر کو یکجا کریں.",
          "آہستہ آہستہ خشک اجزاء کو گیلے مرکب میں شامل کریں۔",
            "بیٹر کو چکنائی والے 8x8 انچ پین میں یکساں طور پر پھیلائیں",
            "20-25 منٹ تک پکائیں، یا اس وقت تک پکائیں جب تک کہ براؤنی پین کے کناروں سے دور کھینچنا شروع نہ کر دے۔",
            "چوراہوں کو کاٹنے سے پہلے ٹھنڈا ہونے دو۔",
        ],
        "image": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092"
    },
    # You can add more recipes as needed
}

# Streamlit app
def main():
    st.title("Simple Recipe Finder")

    food_item = st.text_input("Enter a food item:")

    if st.button("Find Recipe"):
        food_item = food_item.lower()  # Convert input to lowercase to match keys
        if food_item in recipes:
            recipe = recipes[food_item]
            st.subheader(recipe["title"])
            st.image(recipe["image"], width=300)
            st.write("### Ingredients:")
            for ingredient in recipe["ingredients"]:
                st.write(f" - {ingredient}")
            st.write("### Instructions:")
            for step in recipe["instructions"]:
                st.write(step)
        else:
            st.write("Sorry, no recipe found for that food item. Try 'pasta', 'pancakes', 'chocolate chip cookies', or 'brownies'.")

if __name__ == "__main__":
    main()