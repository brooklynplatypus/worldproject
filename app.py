
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# Configure the template folder explicitly
template_dir = os.path.abspath('templates')
app.template_folder = template_dir

# Mock database of articles
articles = [
    {
        'id': 1,
        'title': 'White Castle Opens!',
        'author': 'William',
        'date': 'Fall 1922',
        'content': 'Established in 1921, White Castle was the beginning of the American Fast Food industry. It provided efficiency, affordable prices, and high volume. By using an assembly-line system, they reduced labor costs and became highly profitable. This was the start of fast-food chains that used business strategies such as capitalism, consumer culture, and low-cost labor.',
        'category': 'history',
        'image': 'white-castle.jpg',
        'featured': True
    },
    {
        'id': 2,
        'title': 'The Appeal of “Take-Out food” to Families',
        'author': 'Mia',
        'date': 'Fall 1922',
        'content': 'Somewhere between a cafeteria and a restaurant, The Automat, located in New York City, has remained popular in the new decade despite its age: it first opened in the US in 1902. Inspired by German automat Quisiana, American entrepreneurs began work on a new type of restaurant that allowed for an easier food experience than ever before. Now a classic institution that is a deep part of New York City culture, the Automat has even become a must-see destination for tourists. The Automat has become a place of cultural mixing for the vibrant, socially diverse inhabitants and visitors of Broadway. The Automat serves up American comfort foods like pie, mac n’ cheese, and mashed potatoes sold by machines that are easily operated, even by children. For families, it has never been easier to access an easy, quick meal. The Automat isn’t a tourist trap: it feeds families.',
        'category': 'history',
        'image': 'automat.jpg',
        'featured': True
    },
    {
        'id': 3,
        'title': 'McLiberty: The Intersection Between Fast Food and Civil Rights',
        'author': 'Mia',
        'date': 'Summer 1970',
        'content': 'Originally founded in California in the 1940s, the first McDonald’s was a barbecue restaurant serving customers by drive-through. However, after the McDonald’s brothers realized they could earn most of their profit through selling hamburgers, they quickly streamlined the process for maximum efficiency. They began to seek out franchisees in the 1950s and quickly gained 228 franchises all across the US by 1960. At this time, they were grossing $56 million every year. Their success largely resulted from the increased popularization of car use, as well as good marketing. In the 1950s and ‘60s, leaders like Martin Luther King Jr. and Thurgood Marshall led the Civil Rights Movement. The Civil Rights Movement finally ended in 1968, after Congress passed the Civil Rights Act. This same year, Herman Petty became the first African-American to franchise a McDonald’s. He made history and facilitated the entrance of African-Americans into the entrepreneurial roles in the fast food industry.',
        'category': 'history',
        'image': 'herman-petty.jpg',
        'featured': True
    },
    {
        'id': 4,
        'title': 'Fast Food: Europe (The McWorld)',
        'author': 'Mia',
        'date': 'May 2025',
        'content': 'Only in very recent years have American fast food companies gained traction in Europe. Popular companies include McDonald’s, KFC, and Burger King. However, Europe also has its own fast food brands that have slowed the further expansion of American fast food brands. In Germany, Doner Kebab is a very popular kebab chain. Nando’s is an originally UK-based South African fast food chain serving quick cultural food like peri-peri chicken. However, McDonald’s remains at the top of popularity amongst European diners.',
        'category': 'today',
        'image': 'europe.jpg',
        'featured': True
    },
    {
        'id': 5,
        'title': 'Fast Food: Asia (The McWorld)',
        'author': 'Mia',
        'date': 'May 2025',
        'content': 'In recent years, American fast food chains like McDonald’s and KFC have spread to Asian countries like China, Japan, and Indonesia due to rising globalization. The convenience of fast food and the adaptation of fast food chains to local tastes and cultures, as well as a need in quickly growing Asian countries for more food, have caused chains to experience growth in Asia. KFC, for instance, derives over 40% of its revenues from China alone (see graph above), and has become a staple in Chinese and Japanese society.',
        'category': 'today',
        'image': 'asia.jpg',
        'featured': False
    },
    {
        'id': 6,
        'title': 'Fast Food Calories Increase',
        'author': 'William',
        'date': 'May 2025',
        'content': 'With the globalization of fast food, the calorie content of fast food has increased. As companies expand and move into new markets, they add larger portion sizes to attract customers and compete with local restaurants. Additionally, to cut costs, many chains rely on highly processed ingredients, artificial flavors, and preservatives. These are all high in sodium, sugar, and unhealthy fats. In many chain restaurants, local ingredients and traditional cooking methods are replaced with cheaper alternatives, which reduces the quality of food while increasing the caloric intake. Side dishes and desserts have also become more calorie-dense due to the globalization of fast food. (15) Simple side dishes such as salads or steamed vegetables are replaced with large servings of fries, onion rings, or cheese-covered sides. Both side dishes and desserts come bundled in value meals, which often encourage customers to spend more money and consume more than they usually would. The convenience and price of these meals make them popular, but contribute to a significant amount of calories to an average meal. ',
        'category': 'today',
        'image': 'calories.jpg',
        'featured': True
    },
    {
        'id': 7,
        'title': 'Globesity',
        'author': 'William',
        'date': 'May 2025',
        'content': 'The graph shows a clear, positive correlation between obesity rates and globalization. Countries with higher scores on KOF have a significantly higher percentage of being overweight. Globalization not only brings greater economic change but also contributes to drastic lifestyle changes. Among these changes is increasing availability and consumption of calorie-dense foods, or “empty calories.” Companies like McDonalds have implemented these changes into their companies and have made very calorie-dense menu items. The globalization of Western markets plays a direct role in rising obesity, especially in developing nations that are trying to rapidly industrialize. ',
        'category': 'today',
        'image': 'globesity.jpg',
        'featured': True
    },
    {
        'id': 8,
        'title': 'Growing Obesity Rates in Children',
        'author': 'William',
        'date': 'May 2025',
        'content': 'As globalization increases, so does the access to unhealthy and processed foods worldwide. As global trade expands, fast food chains have become accessible in many countries, even in countries that had traditionally healthy diets. Children and youth were not exempt from this. From the 1960s to 2002s, the percentage of kids aged 6-11, and aged 12-19 with obesity have quadrupled and almost tripled, respectively.',
        'category': 'today',
        'image': 'childobesity.jpg',
        'featured': True
    },
    {
        'id': 9,
        'title': 'Fast Foods Impact',
        'author': 'William',
        'date': 'May 2025',
        'content': 'As nations become more and more globally connected, peoples’ experience shifts in diet and physical activity. They often adopt sedentary lifestyles and consume higher-fat, higher-calorie foods.  ',
        'category': 'today',
        'image': 'impact.jpg',
        'featured': True
    },
    {
        'id': 10,
        'title': 'Food Marketing Towards Youth',
        'author': 'William',
        'date': 'May 2025',
        'content': 'Food marketing to children plays a major role in obesity rates among children in the U.S. Children are heavily targeted by advertisers promoting high-calorie, low-nutrient foods. This marketing technique takes advantage of',
        'category': 'today',
        'image': 'youthmarketing.jpg',
        'featured': True
    },
    {
        'id': 11,
        'title': 'Fast Food Predecessors',
        'author': 'Deon',
        'date': '100 AD',
        'content': 'Romans, known for their strong military, grand architecture, and developments in politics, just like our modern day selves, had also enjoyed their own version of fast food. That is, well, if wine dyed with white beans; soups made of snails, sheep, and fish; or skewered meat sound delightful to you. Roman thermopolias, literally meaning “hot shop” in Greek, were snack bars that served popular street food around A.D. 79. As excavators began their work as far back as 1748, fragments of this ancient architecture have continued to provide more clues about how residents may have lived, dressed, and eaten while also revealing culinary tastes from food and drink residue that has lasted for millennia. Coincidentally, there existed an ancestor of the hamburger called the isicia omentata. This was among one of the best-selling foods in thermopolias. Like many national foods, there are bound to be different variations. The most common variations of isicia omentata included minced meat, breadcrumbs, sweet red wine, peppercorns, pine nuts, liquamen, and myrtle berries, all commonly found near the Mediterranean. When all of these ingredients are combined, a meatball-like patty would be made out of them. The structure of the thermopolium was very simplistic, including a small, open room with a masonry counter usually decorated with marble slabs. Additionally, large terracotta amphorea were encased for food storage. These structures usually differed from one another, with some having seating areas resembling modern fast food restaurants. Additionally, interior design was of utmost importance in these themopolia. Excavators have uncovered 89 and counting thermopolia. The graffiti found on the walls of Asellina, one standing thermopolium, suggests that young women had offered company to ease foreign customers. This highly suggested to excavators that people from all over the Mediterranean basin traveled to Pompeii. Other thermopolias had rooms for courtyards, gambling spaces, and recreational usage. However, this is the mere surface of what has been discovered by ongoing excavations. More excavations will lead to more laboratory analysis, including expert analysis from anthropologists, refining knowledge about thermopolias. Maybe you might have to thank the Romans the next time you grab a quick meal from McDonalds.',
        'category': 'history',
        'image': 'roman.jpg',
        'featured': True
    },
    {
        'id': 12,
        'title': 'Greener Than Vegetables',
        'author': 'Deon',
        'date': 'May 2025',
        'content': 'In recent years, people around the world have felt the effects of global warming and climate change: intense weather conditions, droughts, rising temperatures, and many more. One main factor that accelerates the speed of global warming, though, is the growth of greenhouse gases. Greenhouse gases such as carbon dioxide, methane, and even water vapor absorb heat from the sun, trapping it in the atmosphere which leads to global warming. Although urbanization, deforestation, and the use of fossil fuels have all greatly increased levels of greenhouse gases, about a third of all greenhouse gas emissions have been linked to food production. Imagine a fast food restaurant in its full glory: the clean tabletops with chairs, the smell of freshly grilled patties, and the cool air conditioning from the vents. However, these restaurants happen to be greatly involved in greenhouse gas emissions. For one, the most iconic part of most fast food chains is the burger. Most burgers include beef, which is the least environmentally friendly option of all protein options, releasing 70.6 kilograms of greenhouse gases per kilogram. Additionally, products made from vegetables, fruits, and grains use high amounts of fertilizers which can lead to runoff, a process where the over-use of fertilizers leads to land and water pollution. In the U.S. alone, approximately 22 to 33 billion pounds of food waste is created from restaurant food, with 15% of all this waste put into landfills. Take note that there are over 200,000 fast food businesses in the United States. A large portion of food waste is being produced by fast food restaurants. This also accounts for an estimated $218 billion of food waste or approximately 1.3% of the GDP of the United States. The production of single-use products, including plastic packaging, brown paper bags, and paper straws, also contribute to the emission of greenhouse gases. Plastic packaging nationally creates an additional 184 to 213 million metric tons of greenhouse gases each year. Plastic production also creates methane emissions, a greenhouse gas that is an estimated 80 to 120 times more potent at trapping heat than carbon dioxide. As global warming continues to impact the Earth, fast food companies have started to help. An increasing number of fast food chains have started to prioritize waste management throughout tens of thousands of facilities by converting food scraps into compost helps to reduce landfill waste, creating more healthy soil, and reducing the carbon footprint of food waste. Recycling packaging used for storing food is also helpful. In addition, using biodegradable and edible food packaging is also better and more sustainable. As the fast food industry continues to grow, climate change awareness must grow with it. ',
        'category': 'today',
        'image': 'greenhousegas.jpg',
        'featured': True
    },
    {
        'id': 13,
        'title': 'Desserts? No, Food Desert',
        'author': 'Deon',
        'date': 'May 2025',
        'content': 'Throughout the history of the English language, the words desert and dessert have been commonly confused for each other. Desserts are sweet, delectable, and mostly bring fond memories. In contrast, deserts are the complete opposite: dry, humid, and desolate. Though many people may not live next to a literal desert, one in ten families in the United States feel the effect of a food dessert. A food desert is  an urban area in which it is difficult to buy affordable and good-quality food. Americans have faced growing rates of obesity, caused by a combination of unhealthy lifestyle habits and lack of physical activity. Additionally, some Americans have been negatively affected just by the way their street, neighborhood, or even city was built. A study by Jae In Oh et al. was conducted to see the correlation between the food environment, park access, diet, and physical activity throughout America, despite the fact that the direction and degree of this relationship would heavily vary depending on the use of different variables studied. The study focused on obesity and diabetes rates to determine if there was an effect (see maps). There is a multitude of health effects caused by frequent consumption of fast food, both short-term and long-term. For instance, fast food is usually digested relatively quickly by the body, leading to a short but very sharp spike in blood sugar levels because of the large amount of carbohydrates and sugar being digested at once. This is also the reason for many people of why fast food isn’t filling for an adequate amount of time. Some long-term impacts include inflammation, constipation, higher blood pressure, and a weaker immune system.',
        'category': 'today',
        'image': 'fooddesert.jpg',
        'featured': True
    },
    {
        'id': 14,
        'title': 'Food Scarcity in History',
        'author': 'Mia',
        'date': 'May 2025',
        'content': 'Food crises have led to political instability and economic problems since the beginning of history. In dynastic China, for example, food scarcity has been a factor leading to the loss of the Mandate of Heaven of the current dynasty. However, food issues have also been used as a political weapon. In history, famines have been used by the Soviets and the British as a way to exert power over the population (see other articles). In recent years, food scarcity around the world has been unequal based on poverty and identity. In the US, Native Americans and African Americans experience the highest poverty rates in comparison to their population proportions: while Native Americans only make up about 1.2% of the US population, they make up 2.6% of the population that is in poverty. Despite the creation of federal food assistance programs, food scarcity still disproportionately affects minorities and only increases the gap between the rich and poor.',
        'category': 'enduring-issue',
        'image': 'scarcity.jpg',
        'featured': True
    },
    {
        'id': 15,
        'title': 'Holodomor',
        'author': 'William',
        'date': 'Winter 1934',
        'content': 'The Holodomor was a man-made famine in Soviet Ukraine from 1932 to 1933. The Soviet government took grain and food from Ukrainian farmers to meet high quotas for food. This caused widespread starvation in the Soviet Union and led to the starvation of millions of people.',
        'category': 'enduring-issue',
        'image': 'holodomor.jpg',
        'featured': True
    },
    {
        'id': 16,
        'title': 'Great Chinese Famine',
        'author': 'Deon',
        'date': 'Summer 1962',
        'content': 'The Great Chinese Famine occurred between 1959 and 1961 and is considered one of the deadliest famines in human history. During Mao Zedongs rule, the Great Leap Forward had prioritized the collectivization of agriculture. This led to a widespread food shortage throughout China. An estimated 15 to 45 million Chinese died during this period. ',
        'category': 'enduring-issue',
        'image': 'china.jpg',
        'featured': True
    },
    {
        'id': 17,
        'title': 'Irish Potato Famine',
        'author': 'William',
        'date': 'Spring 1860',
        'content': 'The Irish Potato Famine lasted from 1845 to 1852. A disease had destroyed most potato crops, which were the main food for people at the time. Although there was other food in Ireland, the British government allowed it to be exported to other countries. Over time, the famine got worse, which lead to mass deaths.',
        'category': 'enduring-issue',
        'image': 'potato.jpg',
        'featured': True
    },
]

# Add current date to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/category/<category_name>')
def category(category_name):
    try:
        category_articles = [a for a in articles if a['category'].lower() == category_name.lower()]
        if not category_articles:
            return render_template('category.html', 
                                category=category_name.capitalize(), 
                                articles=None,
                                message=f"No articles found in {category_name} category")
        return render_template('category.html', 
                            category=category_name.capitalize(), 
                            articles=category_articles)
    except Exception as e:
        print(f"Error in category route: {str(e)}")
        return redirect(url_for('home'))


@app.route('/article/<int:article_id>')
def article(article_id):
    try:
        article = next((a for a in articles if a['id'] == article_id), None)
        if article:
            related = [a for a in articles if a['category'] == article['category'] and a['id'] != article_id][:3]
            return render_template('article.html', 
                                article=article, 
                                related_articles=related)
        return redirect(url_for('home'))
    except Exception as e:
        print(f"Error in article route: {str(e)}")
        return redirect(url_for('home'))

@app.route('/category/<category_name>')
def category(category_name):
    try:
        category_articles = [a for a in articles if a['category'].lower() == category_name.lower()]
        return render_template('category.html', 
                            category=category_name, 
                            articles=category_articles)
    except Exception as e:
        print(f"Error in category route: {str(e)}")
        return redirect(url_for('home'))

@app.route('/search')
def search():
    try:
        query = request.args.get('q', '')
        results = []
        if query:
            results = [a for a in articles if query.lower() in a['title'].lower() or query.lower() in a['content'].lower()]
        return render_template('search.html', 
                             query=query, 
                             results=results)
    except Exception as e:
        print(f"Error in search route: {str(e)}")
        return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.template_filter('format_date')
def format_date(value):
    try:
        date_obj = datetime.strptime(value, '%Y-%m-%d')
        return date_obj.strftime('%B %d, %Y')
    except:
        return value

if __name__ == '__main__':
    # Run on port 5001 if 5000 is in use
    try:
        app.run(debug=True, port=5000)
    except OSError:
        app.run(debug=True, port=5001)

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Mock database of articles
articles = [
    {
        'id': 1,
        'title': 'Local Election Results Announced',
        'author': 'Jane Smith',
        'date': '2023-05-15',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus.',
        'category': 'Politics',
        'image': 'election.jpg',
        'featured': True
    },
    {
        'id': 2,
        'title': 'New School Budget Approved',
        'author': 'John Doe',
        'date': '2023-05-14',
        'content': 'Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio.',
        'category': 'Education',
        'image': 'school.jpg',
        'featured': False
    },
    {
        'id': 3,
        'title': 'Tech Giant Opens Local Office',
        'author': 'Mike Johnson',
        'date': '2023-05-13',
        'content': 'Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et justo dignissim congue.',
        'category': 'Business',
        'image': 'tech-office.jpg',
        'featured': False
    }
]

# Routes
@app.route('/')
def home():
    featured = [article for article in articles if article['featured']]
    recent = sorted(articles, key=lambda x: x['date'], reverse=True)[:3]
    return render_template('index.html', featured=featured[0] if featured else None, recent_articles=recent)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        related = [a for a in articles if a['category'] == article['category'] and a['id'] != article_id][:3]
        return render_template('article.html', article=article, related_articles=related)
    return redirect(url_for('home'))

@app.route('/category/<category_name>')
def category(category_name):
    category_articles = [a for a in articles if a['category'].lower() == category_name.lower()]
    return render_template('category.html', category=category_name, articles=category_articles)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        results = [a for a in articles if query.lower() in a['title'].lower() or query.lower() in a['content'].lower()]
    else:
        results = []
    return render_template('search.html', query=query, results=results)

@app.route('/about')
def about():
    return render_template('about.html')

@app.template_filter('format_date')
def format_date(value):
    date_obj = datetime.strptime(value, '%Y-%m-%d')
    return date_obj.strftime('%B %d, %Y')

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Remove debug=True for production
