<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Recommendation System</title>
</head>
<body>
    <h1>Movie Recommendation System</h1>
    <p>A Python-based movie recommendation system that uses machine learning techniques like TF-IDF and cosine similarity to suggest movies based on a user's input.</p>

    <h2>Features</h2>
    <ul>
        <li>Analyzes movie data including genres, keywords, cast, director, and tagline.</li>
        <li>Uses TF-IDF vectorization to represent text data as feature vectors.</li>
        <li>Calculates cosine similarity to find movies similar to the user's favorite.</li>
        <li>Recommends the top 10 movies most similar to the user’s input.</li>
    </ul>

    <h2>How It Works</h2>
    <ol>
        <li>Loads the dataset (<code>movies.csv</code>).</li>
        <li>Preprocesses data by combining relevant columns into a single text string.</li>
        <li>Transforms the data into feature vectors using TF-IDF vectorization.</li>
        <li>Calculates similarity scores using cosine similarity.</li>
        <li>Matches the user's input movie with the closest match in the dataset using difflib.</li>
        <li>Returns a list of movies ranked by similarity score.</li>
    </ol>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/your-username/movie-recommendation-system.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd movie-recommendation-system</code></pre>
        </li>
        <li>Install the required Python libraries:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Place the movie dataset as <code>movies.csv</code> in the project directory.</li>
        <li>Run the script:
            <pre><code>python main.py</code></pre>
        </li>
        <li>Input your favorite movie when prompted.</li>
        <li>Receive a list of 10 recommended movies!</li>
    </ol>

    <h2>Dataset</h2>
    <p>The project uses a movie dataset in CSV format. Ensure the dataset contains the following columns:</p>
    <ul>
        <li><code>title</code></li>
        <li><code>genres</code></li>
        <li><code>keywords</code></li>
        <li><code>cast</code></li>
        <li><code>director</code></li>
        <li><code>tagline</code></li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li>Python</li>
        <li>Pandas</li>
        <li>NumPy</li>
        <li>Scikit-learn</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to fork the repository and submit a pull request.</p>

    <h2>Contact</h2>
    <p>For any inquiries, please contact <strong>your-email@example.com</strong>.</p>
</body>
</html>
