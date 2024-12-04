<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mon Portfolio</title>
    <link rel="stylesheet" href="louu.css">
</head>
<body>
    <header>
        <h1>Mon Nom</h1>
        <p>Développeur Web</p>
    </header>
    
    <nav>
        <ul>
            <li><a href="#about">À propos</a></li>
            <li><a href="#projects">Projets</a></li>
            <li><a href="#skills">Compétences</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="about">
        <h2>À propos de moi</h2>
        <p>Je suis un développeur web passionné avec une expertise en HTML, CSS et JavaScript.</p>
    </section>

    <section id="projects">
        <h2>Mes Projets</h2>
        <div class="project">
            <h3>Projet 1</h3>
            <p>Description du projet 1.</p>
        </div>
        <div class="project">
            <h3>Projet 2</h3>
            <p>Description du projet 2.</p>
        </div>
        <div class="project">
            <h3>Projet 3</h3>
            <p>Description du projet 3.</p>
        </div>
    </section>

    <section id="skills">
        <h2>Compétences</h2>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
            <li>React</li>
            <li>Node.js</li>
        </ul>
    </section>

    <footer id="contact">
        <h2>Contact</h2>
        <p>Email: monemail@example.com</p>
    </footer>
</body>
</html>
<style>
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

nav {
    background: #35424a;
    color: #ffffff;
}

nav ul {
    padding: 0;
    list-style: none;
    text-align: center;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

section {
    padding: 20px;
    margin: 20px;
    background: #ffffff;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.project {
    margin-bottom: 20px;
}

footer {
    text-align: center;
    padding: 20px;
    background: #35424a;
    color: #ffffff;
}</style>