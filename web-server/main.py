
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class = HTMLResponse)
def get_list():
    return """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Inicio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

        nav ul {
            list-style: none;
            padding: 0;
            display: flex;
            justify-content: center;
        }

        nav ul li {
            margin-right: 20px;
        }

        nav ul li a {
            color: #333;
            text-decoration: none;
        }

        section {
            padding: 20px;
        }

        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
            position: absolute;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>Bienvenido a Mi Página</h1>
        <nav>
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Acerca de</a></li>
                <li><a href="#">Servicios</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <section>
        <h2>Sobre Nosotros</h2>
        <p>Somos una empresa comprometida...</p>
    </section>

    <section>
        <h2>Nuestros Servicios</h2>
        <ul>
            <li>Servicio 1</li>
            <li>Servicio 2</li>
            <li>Servicio 3</li>
        </ul>
    </section>

    <section>
        <h2>Contacto</h2>
        <p>Puede contactarnos en...</p>
    </section>

    <footer>
        <p>&copy; 2023 Mi Página. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
        """

@app.get('/contact')
def get_list():
    return ""


