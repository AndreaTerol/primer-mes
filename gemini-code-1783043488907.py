# Let's write the index.html content to a file that the user can directly download as requested.
# It includes the password protection ('2026') and the neon aesthetic.

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Primer mes juntos <3</title>
    <style>
        :root {
            --bg-color: #0a0a0c;
            --card-bg: rgba(20, 20, 25, 0.6);
            --text-main: #ffffff;
            --text-muted: #a0a0ab;
            --neon-pink: #ff007f;
            --neon-purple: #9d4edd;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        /* Bloqueo de seguridad */
        #lock-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: #050507;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            color: white;
            transition: opacity 0.5s ease, visibility 0.5s ease;
        }

        #lock-screen.hidden {
            opacity: 0;
            visibility: hidden;
        }

        .lock-container {
            text-align: center;
            padding: 20px;
        }

        .lock-container h2 {
            font-size: 1.5rem;
            margin-bottom: 20px;
            letter-spacing: 1px;
            color: var(--text-main);
        }

        .lock-container input {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 0, 127, 0.3);
            padding: 12px 20px;
            border-radius: 12px;
            color: white;
            font-size: 1.1rem;
            text-align: center;
            outline: none;
            margin-bottom: 15px;
            width: 200px;
            transition: border-color 0.3s;
        }

        .lock-container input:focus {
            border-color: var(--neon-pink);
            box-shadow: 0 0 10px rgba(255, 0, 127, 0.2);
        }

        .lock-container button {
            background: linear-gradient(135deg, var(--neon-pink), var(--neon-purple));
            border: none;
            padding: 12px 25px;
            color: white;
            border-radius: 12px;
            font-weight: bold;
            cursor: pointer;
            width: 200px;
            font-size: 1rem;
            transition: transform 0.2s;
        }

        .lock-container button:active {
            transform: scale(0.98);
        }

        #error-msg {
            color: #ff4a4a;
            font-size: 0.9rem;
            margin-top: 10px;
            display: none;
        }

        /* Contenido Principal */
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 20% 30%, rgba(255, 0, 127, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(157, 78, 221, 0.12) 0%, transparent 45%);
        }

        #main-content {
            opacity: 0;
            transition: opacity 0.8s ease;
            max-width: 600px;
            width: 100%;
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 40px 30px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            text-align: center;
        }

        #main-content.visible {
            opacity: 1;
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: -1px;
            margin-bottom: 10px;
            background: linear-gradient(to right, #ff007f, #9d4edd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            color: var(--text-muted);
            font-size: 1.1rem;
            margin-bottom: 35px;
        }

        .countdown {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 40px;
        }

        .time-block {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 15px 5px;
        }

        .time-val {
            font-size: 2.2rem;
            font-weight: 700;
            font-family: monospace;
        }

        .time-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin-top: 5px;
        }

        .message-box {
            background: rgba(255, 255, 255, 0.02);
            border-left: 3px solid var(--neon-pink);
            padding: 20px;
            border-radius: 0 16px 16px 0;
            text-align: left;
            margin-top: 20px;
            font-style: italic;
            line-height: 1.6;
            color: #e4e4e7;
        }

        .decor {
            margin-top: 30px;
            font-size: 0.85rem;
            color: rgba(255, 255, 255, 0.2);
            letter-spacing: 2px;
            text-transform: uppercase;
        }
    </style>
</head>
<body>

    <!-- PANTALLA DE BLOQUEO PRIVADA -->
    <div id="lock-screen">
        <div class="lock-container">
            <h2>🔒 Acceso Privado</h2>
            <input type="password" id="password-input" placeholder="Introduce la contraseña" onkeypress="handleKeyPress(event)">
            <br>
            <button onclick="checkPassword()">Entrar</button>
            <div id="error-msg">Contraseña incorrecta, inténtalo de nuevo ⚡</div>
        </div>
    </div>

    <!-- CONTENIDO PRINCIPAL DE LA WEB -->
    <div id="main-content">
        <h1>Primer mes juntos <3</h1>
        <p class="subtitle">El tiempo vuela cuando estoy contigo...</p>

        <div class="countdown">
            <div class="time-block">
                <div class="time-val" id="days">00</div>
                <div class="time-label">Días</div>
            </div>
            <div class="time-block">
                <div class="time-val" id="hours">00</div>
                <div class="time-label">Horas</div>
            </div>
            <div class="time-block">
                <div class="time-val" id="minutes">00</div>
                <div class="time-label">Min</div>
            </div>
            <div class="time-block">
                <div class="time-val" id="seconds">00</div>
                <div class="time-label">Seg</div>
            </div>
        </div>

        <div class="message-box">
            "Parece mentira que ya haya pasado un mes entero. Gracias por cada risa, cada canción compartida y por estar ahí siempre. Esto es solo el principio de todo lo que nos espera de la mano. ¡Te quiero!"
        </div>
        
        <div class="decor">Side A — Track 01</div>
    </div>

    <script>
        // CONTRASEÑA SECRETA: Cambia '2026' por lo que quieras si prefieres otra clave
        const SECRET_PASSWORD = "2026";

        function checkPassword() {
            const input = document.getElementById("password-input").value;
            if (input === SECRET_PASSWORD) {
                document.getElementById("lock-screen").classList.add("hidden");
                document.getElementById("main-content").classList.add("visible");
                initCounter();
            } else {
                document.getElementById("error-msg").style.display = "block";
            }
        }

        function handleKeyPress(event) {
            if (event.key === "Enter") {
                checkPassword();
            }
        }

        // FECHA DE INICIO DE LA CUENTA (Año, Mes [0-11], Día, Hora, Minutos)
        // Ajustada a Junio (5) de 2026
        const startDate = new Date(2026, 5, 3, 0, 0, 0).getTime();

        function initCounter() {
            function updateCounter() {
                const now = new Date().getTime();
                const difference = now - startDate;

                const days = Math.floor(difference / (1000 * 60 * 60 * 24));
                const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((difference % (1000 * 60)) / 1000);

                document.getElementById("days").innerText = days.toString().padStart(2, '0');
                document.getElementById("hours").innerText = hours.toString().padStart(2, '0');
                document.getElementById("minutes").innerText = minutes.toString().padStart(2, '0');
                document.getElementById("seconds").innerText = seconds.toString().padStart(2, '0');
            }
            setInterval(updateCounter, 1000);
            updateCounter();
        }
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS")