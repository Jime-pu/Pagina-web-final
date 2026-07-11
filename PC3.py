# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components
import base64
import pandas as pd
import random
import numpy as np 
import random
#Imagen pa
#pip install pandas openpyxl
# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos', 'Que tanto sabes de los chinos?'] , 
        icons=['0-circle','1-circle', '2-circle','3-circle'], menu_icon="filetype-py", default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
selected = option_menu(
    menu_title="Selecciona una sección: ", 
    options=['Inicio', 'Experiencia', 'Gráficos'], 
    icons=['person-heart', 'globe-americas', 'pencil-square'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>Nombre del blog</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("ellie.png", caption='Ellie', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Aquí escribe una presentación creativa sobre ti.
    ¿Quién eres?, 
    ¿De dónde eres?, 
    ¿Qué estudias?, 
    ¿Qué te gusta de tu carrera?, 
    ¿Qué te gustaría hacer en el futuro?, 
    ¿Qué te gusta hacer en tu tiempo libre?
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif opciones == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio?, 
    ¿Qué te ha enseñado la programación?, 
    ¿Qué te gusta de programar?, 
    ¿Qué te gustaría hacer con la programación en el futuro?
    ¿Cómo se relaciona lo que haz aprendido con tu carrera?
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - YouTube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta ...., "
    )

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - Google Drive")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta ...., "
    )

elif opciones == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Nombre a la sección 'Gráficos'</h2>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("📊 Gráfico 1: Lenguas aisladas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Aquí debe ir una breve interpretación de tu gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "aisladas_base_datos.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_2':
        # Título de la sección
        st.subheader("📊 Gráfico 2: Familias lingüísticas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "lengua_familia_GB.png",
                width=800
            )
    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("🗺️ Mapa 1: Distribución geográfica")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del mapa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )



###Aqui es donde se hace el quiz de los chinos 
elif opciones == 'Que tanto sabes de los chinos?':
    st.markdown("<h1 style='text-align: center;'>Que tanto sabes de los chinos? 💻</h1>",unsafe_allow_html=True)    
    # Agregar un  texto para la respuesta
    texto_4 = """
    Hola preciosa calabazita de algodon, en este quiz se te hara una prueba psicometrica 
    para saber que tan fan eres de los hermosos chicos ojos razgados que cantan como los mismos angeles
    """
    
    col1, col2 = st.columns(2)
    with open("Amongus1.png", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    
    # Poner el enlace (esto es HTML, pero escrito desde Python) Con esto podemos escribiri HTML en phyton para que el amongus te mande a un video
    st.markdown(
        f'<a href="https://www.youtube.com/watch?v=VoQ1q41iJS0" target="_blank">'
        f'<img src="data:image/png;base64,{img_data}" width="50">'
        f'<p style="text-align:center;font-size:12px;color:gray;">Causa</p>'
        f'</a>',
        unsafe_allow_html=True
    )
    
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
        # --- SELECCIONAR DIFICULTAD ---
    dificultad = st.radio(
        "Selecciona el nivel de dificultad:",
        options=["Fácil", "Normal", "Difícil"],
        index=0,  # Por defecto "Fácil"
        horizontal=True
    )
    st.divider()  # Línea separadora

    # --- BANCO DE PREGUNTAS ---
    preguntas_facil = [
        {
            "pregunta": "¿De qué país proviene el K-pop?",
            "opciones": ["Japón", "Corea del Sur", "China", "Tailandia"],
            "respuesta": "Corea del Sur"
        },
        {
            "pregunta": "¿Qué significa K-pop?",
            "opciones": ["Korean Pop", "King Pop", "Kawaii Pop", "K-Music"],
            "respuesta": "Korean Pop"
        },
        {
            "pregunta": "¿Cuál de estos es un grupo de K-pop?",
            "opciones": ["BTS", "One Direction", "Maroon 5", "Coldplay"],
            "respuesta": "BTS"
        },
        {
            "pregunta": "¿Cuál de estas palabras se usa mucho en K-pop para referirse a los fans?",
            "opciones": ["Fandom", "Clan", "Equipo", "Banda"],
            "respuesta": "Fandom"
        },
        {
            "pregunta": "¿Qué significa 'maknae'?",
            "opciones": ["Líder", "Integrante más joven", "Rapero principal", "Coreógrafo"],
            "respuesta": "Integrante más joven"
        }
    ]

    preguntas_normal = [
        {
            "pregunta": "¿Cuál es la compañía detrás del grupo BTS?",
            "opciones": ["SM Entertainment", "YG Entertainment", "HYBE (antes Big Hit)", "JYP Entertainment"],
            "respuesta": "HYBE (antes Big Hit)"
        },
        {
            "pregunta": "En el K-pop, ¿qué es un 'comeback'?",
            "opciones": ["Un concierto especial", "El lanzamiento de nuevo material musical", "Un baile característico", "El saludo del grupo"],
            "respuesta": "El lanzamiento de nuevo material musical"
        },
        {
            "pregunta": "¿Qué significa 'bias' en el fandom del K-pop?",
            "opciones": ["El miembro favorito de cada persona", "El líder del grupo", "El baile principal", "El primer álbum"],
            "respuesta": "El miembro favorito de cada persona"
        },
        {
            "pregunta": "¿Qué artista popularizó el K-pop a nivel mundial con 'Gangnam Style'?",
            "opciones": ["BTS", "PSY", "BLACKPINK", "EXO"],
            "respuesta": "PSY"
        },
        {
            "pregunta": "¿Cómo se llama el sistema de baile sincronizado en grupo que caracteriza al K-pop?",
            "opciones": ["Freestyle", "Coreografía en espejo", "Dance battle", "Performance grupal"],
            "respuesta": "Coreografía en espejo"  # Aunque es un término común, lo dejo así para la prueba
        }
    ]

    # --- LÓGICA PARA DIFICULTAD DIFÍCIL (CON EXCEL Y SESSION_STATE) ---
    if dificultad == "Difícil":
        # Inicializar las variables de estado si no existen
        if "artista_dificil" not in st.session_state:
            st.session_state.artista_dificil = None
            st.session_state.preguntas_dificil = None
            st.session_state.respuestas_usuario_dificil = {}
            st.session_state.calificado_dificil = False
    
        # Función para cargar un nuevo artista y generar preguntas
        def cargar_nuevo_artista():
            try:
                df = pd.read_excel("BASE DE DATOS.xlsx", engine="openpyxl")
                # Verificar columnas
                columnas_requeridas = ["Nombre artístico", "Lugar de nacimiento", "Signo", "Grupo de Kpop", "Rol en el grupo", "Imagen del idol"]
                for col in columnas_requeridas:
                    if col not in df.columns:
                        st.error(f"❌ El archivo Excel no contiene la columna '{col}'. Verifica los nombres.")
                        return False
                # Elegir un artista aleatorio
                artista = df.sample(n=1).iloc[0]
                # Guardar en session_state
                st.session_state.artista_dificil = artista
                # Generar opciones para cada atributo
                todos_nombres = df["Nombre artístico"].dropna().unique()
                todos_lugares = df["Lugar de nacimiento"].dropna().unique()
                todos_signos = df["Signo"].dropna().unique()
                todos_grupos = df["Grupo de Kpop"].dropna().unique()

                def obtener_opciones(correcto, lista_completa):
                    opciones = [op for op in lista_completa if op != correcto]
                    if len(opciones) < 3:
                        while len(opciones) < 3:
                            opciones.append(random.choice(lista_completa))
                    incorrectas = random.sample(opciones, 3) if len(opciones) >= 3 else random.choices(opciones, k=3)
                    todas = incorrectas + [correcto]
                    random.shuffle(todas)
                    return todas

                # Almacenar las opciones en session_state
                st.session_state.preguntas_dificil = {
                    "grupo": {
                        "pregunta": "¿A qué grupo de K-pop pertenece este idol?",
                        "opciones": obtener_opciones(artista["Grupo de Kpop"], todos_grupos),
                        "correcta": artista["Grupo de Kpop"]
                    },
                    "nombre": {
                        "pregunta": "¿Cuál es el nombre artístico de este idol?",
                        "opciones": obtener_opciones(artista["Nombre artístico"], todos_nombres),
                        "correcta": artista["Nombre artístico"]
                    },
                    "lugar": {
                        "pregunta": "¿Dónde nació?",
                        "opciones": obtener_opciones(artista["Lugar de nacimiento"], todos_lugares),
                        "correcta": artista["Lugar de nacimiento"]
                    },
                    "signo": {
                        "pregunta": "¿Cuál es su signo zodiacal?",
                        "opciones": obtener_opciones(artista["Signo"], todos_signos),
                        "correcta": artista["Signo"]
                    }
                }
                # Reiniciar respuestas del usuario
                st.session_state.respuestas_usuario_dificil = {}
                st.session_state.calificado_dificil = False
                return True
            except FileNotFoundError:
                st.error("❌ No se encontró el archivo 'BASE DE DATOS.xlsx'. Asegúrate de que esté en la misma carpeta.")
                return False
            except Exception as e:
                st.error(f"❌ Error al leer el archivo Excel: {e}")
                return False

        # Si no hay artista cargado (primera vez), cargar uno
        if st.session_state.artista_dificil is None:
            cargando = cargar_nuevo_artista()
            if not cargando:
                st.stop()

        # Mostrar el artista y las preguntas desde session_state
        artista = st.session_state.artista_dificil
        preguntas = st.session_state.preguntas_dificil

        # Mostrar imagen
        imagen = artista["Imagen del idol"]
        if pd.notna(imagen) and imagen != "":
            try:
                st.image(imagen, caption=f"¿Reconoces a este idol?", width=200)
            except:
                st.warning("No se pudo cargar la imagen. Puede que la ruta sea inválida.")
        else:
            st.info("📸 No hay imagen disponible para este artista.")

        # Mostrar las preguntas (usando session_state para almacenar las respuestas)
        # Pregunta 1: Grupo
        resp_grupo = st.radio(
            f"**1. {preguntas['grupo']['pregunta']}**",
            preguntas['grupo']['opciones'],
            key="dif_grupo",
            index=None  # para que no tenga selección por defecto
        )
        # Pregunta 2: Nombre
        resp_nombre = st.radio(
            f"**2. {preguntas['nombre']['pregunta']}**",
            preguntas['nombre']['opciones'],
            key="dif_nombre",
            index=None
        )
        # Pregunta 3: Lugar
        resp_lugar = st.radio(
            f"**3. {preguntas['lugar']['pregunta']}**",
            preguntas['lugar']['opciones'],
            key="dif_lugar",
            index=None
        )
        # Pregunta 4: Signo
        resp_signo = st.radio(
            f"**4. {preguntas['signo']['pregunta']}**",
            preguntas['signo']['opciones'],
            key="dif_signo",
            index=None
        )

        # Guardar respuestas en session_state
        st.session_state.respuestas_usuario_dificil["grupo"] = resp_grupo
        st.session_state.respuestas_usuario_dificil["nombre"] = resp_nombre
        st.session_state.respuestas_usuario_dificil["lugar"] = resp_lugar
        st.session_state.respuestas_usuario_dificil["signo"] = resp_signo

        # Botón para calificar
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Ver mi puntuación", use_container_width=True):
                # Verificar que todas las preguntas tengan respuesta
                if any(v is None for v in st.session_state.respuestas_usuario_dificil.values()):
                    st.warning("Por favor, responde todas las preguntas antes de calificar.")
                else:
                    correctas = 0
                    if st.session_state.respuestas_usuario_dificil["grupo"] == preguntas['grupo']['correcta']:
                        correctas += 1
                    if st.session_state.respuestas_usuario_dificil["nombre"] == preguntas['nombre']['correcta']:
                        correctas += 1
                    if st.session_state.respuestas_usuario_dificil["lugar"] == preguntas['lugar']['correcta']:
                        correctas += 1
                    if st.session_state.respuestas_usuario_dificil["signo"] == preguntas['signo']['correcta']:
                        correctas += 1
                    total = 4
                    porcentaje = (correctas / total) * 100
                    if porcentaje == 100:
                        mensaje = "🌟 ¡Perfecto! Conoces a tu idol a la perfección."
                    elif porcentaje >= 50:
                        mensaje = "🎉 ¡Bien! Tienes buen ojo, pero aún puedes profundizar."
                    else:
                        mensaje = "📖 ¡Sigue practicando! Cada idol tiene su historia."
                    st.success(f"**{correctas}** de **{total}** respuestas correctas ({porcentaje:.0f}%)")
                    st.info(mensaje)
                    st.session_state.calificado_dificil = True

        with col2:
            if st.button("🔄 Nuevo artista", use_container_width=True):
                # Cargar un nuevo artista
                cargar_nuevo_artista()
                st.rerun()  # Forzar refresco de la página

        # Mostrar respuestas correctas si ya se calificó
        if st.session_state.calificado_dificil:
            with st.expander("Ver respuestas correctas"):
                st.write(f"**Grupo:** {preguntas['grupo']['correcta']}")
                st.write(f"**Nombre artístico:** {preguntas['nombre']['correcta']}")
                st.write(f"**Lugar de nacimiento:** {preguntas['lugar']['correcta']}")
                st.write(f"**Signo:** {preguntas['signo']['correcta']}")
        
         # --- Si la dificultad es Fácil o Normal, usar las preguntas fijas ---
    else:
        if dificultad == "Fácil":
            preguntas = preguntas_facil
        else:  # Normal
            preguntas = preguntas_normal

        respuestas_usuario = {}
        for i, p in enumerate(preguntas):
            respuestas_usuario[i] = st.radio(
                f"**{i+1}. {p['pregunta']}**",
                p["opciones"],
                key=f"pregunta_{i}"
            )

        if st.button("📊 Ver mi puntuación", use_container_width=True):
            correctas = 0
            for i, p in enumerate(preguntas):
                if respuestas_usuario[i] == p["respuesta"]:
                    correctas += 1
            total = len(preguntas)
            porcentaje = (correctas / total) * 100
            if porcentaje == 100:
                mensaje = "🌟 ¡Perfecto! Eres un auténtico experto en K-pop."
                
               
            elif porcentaje >= 60:
                mensaje = "🎉 ¡Bien! Tienes buen conocimiento, pero puedes mejorar."
            else:
                mensaje = "📖 ¡Sigue practicando! El K-pop tiene mucho más que ofrecer."
            st.success(f"**{correctas}** de **{total}** respuestas correctas ({porcentaje:.0f}%)")
            st.info(mensaje)
