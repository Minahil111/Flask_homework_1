from flask import Flask, url_for

cookbook = Flask(__name__)


@cookbook.route('/')
def homepage():
    cuisine_url = url_for('list_of_cuisines')
    dietary_requirement_url = url_for('list_of_dietary_requirements')
    return f"""
    <!doctype>
    <html>
        <head>
            <h1>Welcome to your online CookBook!</h1>
        </head>

        <body>
            <h2>Browse for a recipe:</h2>
            <h2><a href="{cuisine_url}">- By cuisine - </a></h2>
            <h2><a href="{dietary_requirement_url}">- By dietary requirement-</a></h2>
        </body>
    </html>
    """


@cookbook.route('/browse_by_cuisine')
def list_of_cuisines():
    home_url = url_for("homepage")
    italian_url = url_for('browse_by_cuisine', cuisine='italian')
    mexican_url = url_for('browse_by_cuisine', cuisine='mexican')
    indian_url = url_for('browse_by_cuisine', cuisine='indian')
    return f"""
    <!doctype>
    <html>
        <head>
            <h1>Cuisines</h1>
        </head>
        
        <body>
            <ul>
              <li><a href={italian_url}>Italian</a></li>
              <li><a href={mexican_url}>Mexican</a></li>
              <li><a href={indian_url}>Indian</a></li>
            </ul>
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """


@cookbook.route('/browse_by_dietary_requirement')
def list_of_dietary_requirements():
    home_url = url_for("homepage")
    gluten_free_url = url_for('browse_by_dietary_requirement', dietary_requirement='gluten_free')
    vegan_url = url_for('browse_by_dietary_requirement', dietary_requirement='vegan')
    return f"""
    <!doctype>
    <html>
        <head>
            <h1>Dietary Requirements</h1>
        </head>

        <body>
            <ul>
              <li><a href={gluten_free_url}>Gluten Free Recipes</a></li>
              <li><a href={vegan_url}>Vegan Recipes</a></li>
            </ul>
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """


@cookbook.route('/browse_by_dietary_requirement/<dietary_requirement>')
def browse_by_dietary_requirement(dietary_requirement):
    home_url = url_for("homepage")
    dietary_requirements_url = url_for('list_of_dietary_requirements')
    if dietary_requirement == 'vegan':
        return f"""
    <!doctype>
    <html>
        <head>
            <h1>Vegan Recipes</h1>
        </head>

        <body>
            <ul>
              <li>Vegan Lentil Curry</li>
              <li>Vegan Chickpea Salad Sandwich</li>
              <li>Vegan Mushroom Risottoe</li>
            </ul>
          <hr>
            <a href="{dietary_requirements_url}">Back to Dietary Requirements</a>
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """
    elif dietary_requirement == 'gluten_free':
        return f"""
    <!doctype>
    <html>
        <head>
            <h1>Gluten Free Recipes</h1>
        </head>

        <body>
            <ul>
              <li>Gluten-Free Quinoa Salad</li>
              <li>Gluten-Free Chicken Stir-Fry</li>
              <li>Gluten-Free Banana Bread</li>
            </ul>
          <hr>
            <a href="{dietary_requirements_url}">Back to Dietary Requirements</a>
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """


@cookbook.route('/browse_by_cuisine/<cuisine>')
def browse_by_cuisine(cuisine):
    home_url = url_for("homepage")
    cuisine_url = url_for('list_of_cuisines')
    spaghetti_carbonara_url = url_for('recipe_choice', recipe='spaghetti_carbonara')
    if cuisine == 'italian':
        return f"""
    <!doctype>
    <html>
        <head>
            <h1>Italian Recipes</h1>
        </head>
        
        <body>
            <ul>
              <li><a href={spaghetti_carbonara_url}>Spaghetti Carbonara</a></li>
              <li>Margherita Pizza</li>
              <li>Risotto alla Milanese</li>
              <li>Bruschetta</li>
              <li>Tiramisu</li>
            </ul>
          <hr>
            <a href="{cuisine_url}">Back to Cuisines</a> 
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """
    elif cuisine == 'mexican':
        return f"""
    <!doctype>
    <html>
        <head>
            <h1>Mexican Recipes</h1>
        </head>
        
        <body>
            <ul>
              <li>Pico de Gallo</li>
              <li>Chicken Quesadillas</li>
              <li>Mexican Street Corn (Elote)</li>
              <li>Churros</li>
              <li>Mango Salsa</li>
            </ul>
          <hr>
            <a href="{cuisine_url}">Back to Cuisines</a> 
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """

    elif cuisine == 'indian':
        return f"""
    <!doctype>
    <html>
        <head>
            <h1>Indian Recipes</h1>
        </head>

        <body>
            <ul>
              <li>Chicken Tikka Masala</li>
              <li>Vegetable Biryani</li>
              <li>Palak Paneer</li>
              <li>Tandoori Chicken</li>
              <li>Dal Makhani</li>  
            </ul>
          <hr>
            <a href="{cuisine_url}">Back to Cuisines</a> 
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """


@cookbook.route('/browse_by_cuisine/italian/<recipe>')
def recipe_choice(recipe):
    home_url = url_for("homepage")
    cuisine_url = url_for('list_of_cuisines')
    italian_url = url_for('list_of_cuisines', cuisine='italian')
    if recipe == 'spaghetti_carbonara':
        return f"""
    <!doctype>
    <html>
        <head>
            <h1>Spaghetti Carbonara</h1>
        </head>

        <body>
            <ul>
              
              <h4>Ingredients:</h4>
              <p> Spaghetti, pancetta or guanciale, eggs, Parmesan cheese, black pepper, salt</p>
              
              <h4>Instructions:</h4>
              <p>Cook spaghetti until al dente. In a pan, cook pancetta until crispy. In a 
              bowl, whisk eggs, Parmesan cheese, and black pepper. Toss cooked spaghetti with pancetta, then mix in 
              egg mixture. Serve immediately.</p>

            </ul>
          <hr>
            <a href="{italian_url}">Back to Italian Recipes</a> 
          <hr>
            <a href="{cuisine_url}">Back to Cuisines</a> 
          <hr>
            <a href="{home_url}">Back to Home Page</a>
        </body>
    </html>
    """


if __name__ == '__main__':
    cookbook.run(debug=True)
