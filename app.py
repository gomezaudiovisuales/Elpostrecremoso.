{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red183\green111\blue179;\red15\green16\blue16;\red173\green176\blue178;
\red67\green192\blue160;\red198\green146\blue255;\red189\green198\blue208;\red120\green129\blue140;\red202\green202\blue202;
\red150\green204\blue255;\red104\green177\blue255;\red252\green99\blue95;\red70\green137\blue204;\red167\green197\blue152;
\red205\green173\blue106;\red253\green149\blue70;}
{\*\expandedcolortbl;;\cssrgb\c77255\c52549\c75294;\cssrgb\c7059\c7451\c7843;\cssrgb\c73333\c74510\c74902;
\cssrgb\c30588\c78824\c69020;\cssrgb\c82353\c65882\c100000;\cssrgb\c78824\c81961\c85098;\cssrgb\c54510\c58039\c61961;\cssrgb\c83137\c83137\c83137;
\cssrgb\c64706\c83922\c100000;\cssrgb\c47451\c75294\c100000;\cssrgb\c100000\c48235\c44706;\cssrgb\c33725\c61176\c83922;\cssrgb\c70980\c80784\c65882;
\cssrgb\c84314\c72941\c49020;\cssrgb\c100000\c65098\c34118;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 flask\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 Flask\cf4 \strokec4 , \cf6 \strokec6 render_template_string\cf4 \strokec4 , \cf7 \strokec7 request\cf4 \strokec4 , \cf7 \strokec7 session\cf4 \strokec4 , \cf6 \strokec6 redirect\cf4 \strokec4 , \cf6 \strokec6 jsonify\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 datetime\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 datetime\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 json\cf4 \strokec4  \cf8 \strokec8 # A\'f1adido para guardar los datos en un archivo\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 os\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 app\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf5 \strokec5 Flask\cf4 \strokec4 (\cf7 \strokec7 __name__\cf4 \strokec4 )\cb1 \
\cf7 \cb3 \strokec7 app\cf4 \strokec4 .\cf7 \strokec7 secret_key\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 'postre_cremoso_seguridad_final_2026'\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf11 \cb3 \strokec11 USER_ADMIN\cf4 \strokec4 , \cf11 \strokec11 PASS_ADMIN\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 "admin"\cf4 \strokec4 , \cf10 \strokec10 "1234"\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 # --- L\'d3GICA DE PERSISTENCIA (Para que no se borre nada) ---\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf11 \cb3 \strokec11 DATA_FILE\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 "datos_postre.json"\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 guardar_todo\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 datos\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \{\cb1 \
\cb3         \cf10 \strokec10 "pedidos"\cf4 \strokec4 : \cf7 \strokec7 pedidos_reales\cf4 \strokec4 ,\cb1 \
\cb3         \cf10 \strokec10 "usuarios"\cf4 \strokec4 : \cf7 \strokec7 usuarios_registrados\cf4 \strokec4 ,\cb1 \
\cb3         \cf10 \strokec10 "productos"\cf4 \strokec4 : \cf7 \strokec7 productos_db\cf4 \cb1 \strokec4 \
\cb3     \}\cb1 \
\cb3     \cf2 \strokec2 with\cf4 \strokec4  \cf6 \strokec6 open\cf4 \strokec4 (\cf11 \strokec11 DATA_FILE\cf4 \strokec4 , \cf10 \strokec10 "w"\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  \cf7 \strokec7 f\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 json\cf4 \strokec4 .\cf6 \strokec6 dump\cf4 \strokec4 (\cf7 \strokec7 datos\cf4 \strokec4 , \cf7 \strokec7 f\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 cargar_todo\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf5 \strokec5 os\cf4 \strokec4 .\cf5 \strokec5 path\cf4 \strokec4 .\cf6 \strokec6 exists\cf4 \strokec4 (\cf11 \strokec11 DATA_FILE\cf4 \strokec4 ):\cb1 \
\cb3         \cf2 \strokec2 with\cf4 \strokec4  \cf6 \strokec6 open\cf4 \strokec4 (\cf11 \strokec11 DATA_FILE\cf4 \strokec4 , \cf10 \strokec10 "r"\cf4 \strokec4 ) \cf2 \strokec2 as\cf4 \strokec4  \cf7 \strokec7 f\cf4 \strokec4 :\cb1 \
\cb3             \cf2 \strokec2 return\cf4 \strokec4  \cf5 \strokec5 json\cf4 \strokec4 .\cf6 \strokec6 load\cf4 \strokec4 (\cf7 \strokec7 f\cf4 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf13 \strokec13 None\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 # Cargar datos guardados o usar los iniciales\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 datos_cargados\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf6 \strokec6 cargar_todo\cf4 \strokec4 ()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 datos_cargados\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 pedidos_reales\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 datos_cargados\cf4 \strokec4 [\cf10 \strokec10 "pedidos"\cf4 \strokec4 ]\cb1 \
\cb3     \cf7 \strokec7 usuarios_registrados\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 datos_cargados\cf4 \strokec4 [\cf10 \strokec10 "usuarios"\cf4 \strokec4 ]\cb1 \
\cb3     \cf7 \strokec7 productos_db\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 datos_cargados\cf4 \strokec4 [\cf10 \strokec10 "productos"\cf4 \strokec4 ]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 else\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 pedidos_reales\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  [] \cb1 \
\cb3     \cf7 \strokec7 usuarios_registrados\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \{\} \cb1 \
\cb3     \cf7 \strokec7 productos_db\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \{\cb1 \
\cb3         \cf10 \strokec10 'Brownie Avellana'\cf4 \strokec4 : \{\cf10 \strokec10 'precio'\cf4 \strokec4 : \cf14 \strokec14 7000\cf4 \strokec4 , \cf10 \strokec10 'estado'\cf4 \strokec4 : \cf10 \strokec10 'Disponible'\cf4 \strokec4 \},\cb1 \
\cb3         \cf10 \strokec10 'Brownie Arequipe'\cf4 \strokec4 : \{\cf10 \strokec10 'precio'\cf4 \strokec4 : \cf14 \strokec14 7000\cf4 \strokec4 , \cf10 \strokec10 'estado'\cf4 \strokec4 : \cf10 \strokec10 'Disponible'\cf4 \strokec4 \},\cb1 \
\cb3         \cf10 \strokec10 'Galleta Beteada Frutos Rojos'\cf4 \strokec4 : \{\cf10 \strokec10 'precio'\cf4 \strokec4 : \cf14 \strokec14 7500\cf4 \strokec4 , \cf10 \strokec10 'estado'\cf4 \strokec4 : \cf10 \strokec10 'Disponible'\cf4 \strokec4 \},\cb1 \
\cb3         \cf10 \strokec10 'Galleta Red Velvet'\cf4 \strokec4 : \{\cf10 \strokec10 'precio'\cf4 \strokec4 : \cf14 \strokec14 8000\cf4 \strokec4 , \cf10 \strokec10 'estado'\cf4 \strokec4 : \cf10 \strokec10 'Disponible'\cf4 \strokec4 \},\cb1 \
\cb3         \cf10 \strokec10 'Galleta Chips Tradicional'\cf4 \strokec4 : \{\cf10 \strokec10 'precio'\cf4 \strokec4 : \cf14 \strokec14 7500\cf4 \strokec4 , \cf10 \strokec10 'estado'\cf4 \strokec4 : \cf10 \strokec10 'Disponible'\cf4 \strokec4 \}\cb1 \
\cb3     \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf11 \cb3 \strokec11 CSS_MASTER\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 <style>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     :root \{ --cafe: #4e342e; --dorado: #bf8f5a; --blanco: #ffffff; --fondo-oscuro: #1a0f0a; --cafe-claro: #5d4037; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     body \{ margin: 0; font-family: 'Arial Black', sans-serif; overflow-x: hidden; background: white; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .flotante \{ position: fixed; z-index: 1; animation: move 10s infinite ease-in-out; opacity: 0.7; pointer-events: none; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     @keyframes move \{ 0%, 100% \{ transform: translate(0,0) rotate(0deg); \} 50% \{ transform: translate(30px, 40px) rotate(15deg); \} \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .view \{ display: none; min-height: 100vh; width: 100%; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .active \{ display: flex; flex-direction: column; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .btn-portal \{ width: 320px; padding: 18px; margin: 10px; border: 2px solid var(--cafe); background: white; color: var(--cafe); border-radius: 15px; font-weight: bold; cursor: pointer; text-transform: uppercase; transition: 0.3s; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .btn-portal:hover \{ background: var(--cafe) !important; color: white !important; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .sidebar \{ position: fixed; top: 0; left: -300px; width: 280px; height: 100%; background: var(--cafe); transition: 0.4s; z-index: 9000; padding-top: 60px; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .sidebar a \{ display: block; color: white; padding: 18px; text-decoration: none; border-bottom: 1px solid var(--cafe-claro); cursor: pointer; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .btn-menu \{ position: fixed; top: 20px; left: 20px; font-size: 30px; cursor: pointer; z-index: 8000; color: var(--cafe); background: white; border-radius: 5px; padding: 5px; border: 1px solid #ccc; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .caja-blanca \{ background: white; border-radius: 20px; padding: 30px; margin: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.15); color: var(--cafe); text-align: center; position: relative; z-index: 10; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     input, select, textarea \{ width: 90%; padding: 12px; margin: 8px 0; border-radius: 10px; border: 1px solid #ccc; font-family: sans-serif; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .hero-tienda \{ height: 60vh; display: flex; flex-direction: column; justify-content: center; align-items: center; background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1606313564200-e75d5e30476c?q=80&w=1000') center/cover; color: white; text-align:center; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .item-car \{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #ffffff22; padding: 15px 0; color: white; width: 100%; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     table \{ width: 100%; border-collapse: collapse; margin-top: 20px; font-family: sans-serif; font-size: 0.8rem; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     th, td \{ padding: 12px; border: 1px solid #ddd; text-align: left; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     th \{ background: var(--cafe); color: white; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .btn-qty \{ background: var(--dorado); color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     .status-badge \{ padding: 5px 10px; border-radius: 5px; font-size: 0.7rem; font-weight: bold; color: white; \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10 </style>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10 <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10 """\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 home\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 dulces\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  [(\cf10 \strokec10 "\uc0\u55356 \u57194 "\cf4 \strokec4 , \cf10 \strokec10 "5%"\cf4 \strokec4 , \cf10 \strokec10 "10%"\cf4 \strokec4 ), (\cf10 \strokec10 "\uc0\u55356 \u57195 "\cf4 \strokec4 , \cf10 \strokec10 "10%"\cf4 \strokec4 , \cf10 \strokec10 "80%"\cf4 \strokec4 ), (\cf10 \strokec10 "\uc0\u55356 \u57193 "\cf4 \strokec4 , \cf10 \strokec10 "50%"\cf4 \strokec4 , \cf10 \strokec10 "5%"\cf4 \strokec4 ), (\cf10 \strokec10 "\uc0\u55356 \u57194 "\cf4 \strokec4 , \cf10 \strokec10 "80%"\cf4 \strokec4 , \cf10 \strokec10 "75%"\cf4 \strokec4 ), (\cf10 \strokec10 "\uc0\u55356 \u57195 "\cf4 \strokec4 , \cf10 \strokec10 "30%"\cf4 \strokec4 , \cf10 \strokec10 "20%"\cf4 \strokec4 )]\cb1 \
\cb3     \cf7 \strokec7 html_dulces\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 ""\cf4 \strokec4 .\cf6 \strokec6 join\cf4 \strokec4 ([\cf12 \strokec12 f\cf10 \strokec10 '<div class="flotante" style="top:\cf12 \strokec12 \{\cf7 \strokec7 d\cf4 \strokec4 [\cf14 \strokec14 1\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 ; left:\cf12 \strokec12 \{\cf7 \strokec7 d\cf4 \strokec4 [\cf14 \strokec14 2\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 ; font-size:50px;">\cf12 \strokec12 \{\cf7 \strokec7 d\cf4 \strokec4 [\cf14 \strokec14 0\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </div>'\cf4 \strokec4  \cf2 \strokec2 for\cf4 \strokec4  \cf7 \strokec7 d\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf7 \strokec7 dulces\cf4 \strokec4 ])\cb1 \
\cb3     \cb1 \
\cb3     \cf7 \strokec7 html_productos\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 ""\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  \cf7 \strokec7 nombre\cf4 \strokec4 , \cf7 \strokec7 info\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf7 \strokec7 productos_db\cf4 \strokec4 .\cf6 \strokec6 items\cf4 \strokec4 ():\cb1 \
\cb3         \cf7 \strokec7 estado_html\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 ""\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 info\cf4 \strokec4 [\cf10 \strokec10 'estado'\cf4 \strokec4 ] \cf9 \strokec9 ==\cf4 \strokec4  \cf10 \strokec10 'Disponible'\cf4 \strokec4 :\cb1 \
\cb3             \cf7 \strokec7 estado_html\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf12 \strokec12 f\cf10 \strokec10 '<button class="btn-portal" style="width:100%; border-color:white; margin:0; padding:10px;" onclick="add(\cf15 \strokec15 \\'\cf12 \strokec12 \{\cf7 \strokec7 nombre\cf12 \strokec12 \}\cf15 \strokec15 \\'\cf10 \strokec10 , \cf12 \strokec12 \{\cf7 \strokec7 info\cf4 \strokec4 [\cf10 \strokec10 "precio"\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 )">AGREGAR</button>'\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 else\cf4 \strokec4 :\cb1 \
\cb3             \cf7 \strokec7 color\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 "#e74c3c"\cf4 \strokec4  \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 info\cf4 \strokec4 [\cf10 \strokec10 'estado'\cf4 \strokec4 ] \cf9 \strokec9 ==\cf4 \strokec4  \cf10 \strokec10 'Agotado'\cf4 \strokec4  \cf2 \strokec2 else\cf4 \strokec4  \cf10 \strokec10 "#f39c12"\cf4 \cb1 \strokec4 \
\cb3             \cf7 \strokec7 estado_html\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf12 \strokec12 f\cf10 \strokec10 '<div style="background:\cf12 \strokec12 \{\cf7 \strokec7 color\cf12 \strokec12 \}\cf10 \strokec10 ; color:white; padding:10px; border-radius:10px; font-weight:bold;">\cf12 \strokec12 \{\cf7 \strokec7 info\cf4 \strokec4 [\cf10 \strokec10 "estado"\cf4 \strokec4 ].upper()\cf12 \strokec12 \}\cf10 \strokec10 </div>'\cf4 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         \cf7 \strokec7 html_productos\cf4 \strokec4  \cf9 \strokec9 +=\cf4 \strokec4  \cf12 \strokec12 f\cf10 \strokec10 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10         <div style="background:#2d1b12; padding:20px; border-radius:15px; width:220px; border:1px solid var(--dorado); text-align:center; color:white;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <h3>\cf12 \strokec12 \{\cf7 \strokec7 nombre\cf12 \strokec12 \}\cf10 \strokec10 </h3>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <p style="color:var(--dorado)">$\cf12 \strokec12 \{\cf7 \strokec7 info\cf4 \strokec4 [\cf10 \strokec10 'precio'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </p>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf12 \strokec12 \{\cf7 \strokec7 estado_html\cf12 \strokec12 \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>"""\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 render_template_string\cf4 \strokec4 (\cf12 \strokec12 f\cf10 \strokec10 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10     \cf12 \strokec12 \{\cf11 \strokec11 CSS_MASTER\cf12 \strokec12 \}\cf10 \strokec10  \cf12 \strokec12 \{\cf7 \strokec7 html_dulces\cf12 \strokec12 \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div id="portada" class="view active" style="justify-content:center; align-items:center;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <h1 style="font-size: 4rem; color: var(--cafe);">EL POSTRE CREMOSO</h1>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <button class="btn-portal" onclick="show('login-admin')">ACCESO PROPIETARIO</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <button class="btn-portal" onclick="show('registro-cliente')">VER MEN\'da CLIENTE</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div id="tienda" class="view" style="background:var(--fondo-oscuro);">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="btn-menu" style="left:auto; right:20px;" onclick="toggleMenu('side-t', true)">\uc0\u9776 </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div id="side-t" class="sidebar"><a onclick="toggleMenu('side-t', false)" style="font-size:30px">&times;</a><a onclick="show('tienda')">TIENDA</a><a onclick="showCarrito()">CARRITO \uc0\u55357 \u57042 </a><a href="/">SALIR</a></div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="hero-tienda">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <h1 style="font-size: 3.5rem; margin:0;">EL POSTRE CREMOSO</h1>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <p style="color:var(--dorado); font-size:1.5rem;">M\'c1S QUE CREMOSO</p>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div style="padding:40px; display:flex; justify-content:center; gap:20px; flex-wrap:wrap;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf12 \strokec12 \{\cf7 \strokec7 html_productos\cf12 \strokec12 \}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div id="registro-cliente" class="view" style="justify-content:center; align-items:center; background:#fdfaf8;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:380px;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <h2>REGISTRO</h2>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="text" id="r-nom" placeholder="Nombre">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="number" id="r-cel" placeholder="N\'famero Celular">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="email" id="r-cor" placeholder="Correo Electr\'f3nico">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="password" id="r-pass" placeholder="Contrase\'f1a">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <button class="btn-portal" style="width:100%;" onclick="registrarUsuario()">INGRESAR</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <span style="cursor:pointer; text-decoration:underline;" onclick="show('login-cliente')">\'bfYa tienes cuenta? Inicia sesi\'f3n</span>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10     <div id="login-cliente" class="view" style="justify-content:center; align-items:center; background:#fdfaf8;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:380px;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <h2>INICIAR SESI\'d3N</h2>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="email" id="l-cor" placeholder="Correo">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="password" id="l-pass" placeholder="Contrase\'f1a">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <button class="btn-portal" style="width:100%;" onclick="loginUsuario()">ENTRAR</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10     <div id="view-carrito" class="view" style="background:var(--fondo-oscuro); color:white; padding:40px 20px; align-items:center;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <h2>TU CARRITO</h2>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div id="lista-items" style="width:100%; max-width:500px; background:#2d1b12; padding:20px; border-radius:15px; border:1px solid var(--dorado);"></div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <h3 id="total-car" style="margin-top:20px; color:var(--dorado); font-size:1.8rem;">Total: $0</h3>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <button class="btn-portal" style="background:var(--dorado); color:white; border:none;" onclick="irAPagar()">IR A PAGAR</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <button class="btn-portal" onclick="show('tienda')">VOLVER A LA TIENDA</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10     <div id="pago-final" class="view" style="justify-content:center; align-items:center; background:#fdfaf8;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" id="contenedor-pago" style="width:420px; text-align:left;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <h2 style="text-align:center;">DATOS DE ENV\'cdO</h2>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="text" id="p-nom" placeholder="Nombre completo *">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="number" id="p-cel" placeholder="Celular *">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="email" id="p-cor" placeholder="Correo electr\'f3nico *">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="text" id="p-ciu" placeholder="Ciudad *">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <input type="text" id="p-dir" placeholder="Ubicaci\'f3n exacta *">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <textarea id="p-obs" placeholder="Observaciones para el domiciliario (Detalles del lugar)..." rows="3"></textarea>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <select id="p-met">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <option value="Efectivo">Pago Contra Entrega</option>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <option value="Nequi">Nequi</option>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             </select>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <button class="btn-portal" style="width:100%; background:var(--cafe); color:white;" onclick="confirmarVenta()">CONFIRMAR PEDIDO</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10     <div id="login-admin" class="view" style="justify-content:center; align-items:center;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:360px;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <h2>ACCESO PROPIETARIO</h2>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <form action="/auth" method="POST">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <input type="text" name="u" placeholder="Usuario"><input type="password" name="p" placeholder="Clave">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <button type="submit" class="btn-portal" style="width:100%;">ENTRAR</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             </form>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10     <script>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         let car = []; let totalF = 0;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         function show(id) \cf15 \strokec15 \{\{\cf10 \strokec10  document.querySelectorAll('.view').forEach(v => v.classList.remove('active')); document.getElementById(id).classList.add('active'); \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         function toggleMenu(id, o) \cf15 \strokec15 \{\{\cf10 \strokec10  document.getElementById(id).style.left = o ? '0' : '-300px'; \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         function registrarUsuario() \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             const nom = document.getElementById('r-nom').value; const cel = document.getElementById('r-cel').value;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             const cor = document.getElementById('r-cor').value; const pas = document.getElementById('r-pass').value;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             fetch('/validar_registro', \cf15 \strokec15 \{\{\cf10 \strokec10  method: 'POST', headers: \cf15 \strokec15 \{\{\cf10 \strokec10 'Content-Type': 'application/json'\cf15 \strokec15 \}\}\cf10 \strokec10 , body: JSON.stringify(\cf15 \strokec15 \{\{\cf10 \strokec10 nom, cel, cor, pas\cf15 \strokec15 \}\}\cf10 \strokec10 ) \cf15 \strokec15 \}\}\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             .then(res => res.json()).then(data => \cf15 \strokec15 \{\{\cf10 \strokec10  if(data.status === 'ok') show('tienda'); else alert(data.msg); \cf15 \strokec15 \}\}\cf10 \strokec10 );\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10         function loginUsuario() \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             const cor = document.getElementById('l-cor').value; const pas = document.getElementById('l-pass').value;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             fetch('/validar_login', \cf15 \strokec15 \{\{\cf10 \strokec10  method: 'POST', headers: \cf15 \strokec15 \{\{\cf10 \strokec10 'Content-Type': 'application/json'\cf15 \strokec15 \}\}\cf10 \strokec10 , body: JSON.stringify(\cf15 \strokec15 \{\{\cf10 \strokec10 cor, pas\cf15 \strokec15 \}\}\cf10 \strokec10 ) \cf15 \strokec15 \}\}\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             .then(res => res.json()).then(data => \cf15 \strokec15 \{\{\cf10 \strokec10  if(data.status === 'ok') show('tienda'); else alert(data.msg); \cf15 \strokec15 \}\}\cf10 \strokec10 );\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10         function add(n, p) \cf15 \strokec15 \{\{\cf10 \strokec10  \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             let item = car.find(x => x.n === n);\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             if(item) item.q++; else car.push(\cf15 \strokec15 \{\{\cf10 \strokec10 n, p, q: 1\cf15 \strokec15 \}\}\cf10 \strokec10 );\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             alert(n + " a\'f1adido!"); \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10         function changeQty(n, v) \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             let item = car.find(x => x.n === n);\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             if(item) \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 item.q += v;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 if(item.q <= 0) car = car.filter(x => x.n !== n);\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             showCarrito();\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10         function showCarrito() \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             const box = document.getElementById('lista-items'); box.innerHTML = ""; totalF = 0;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             if(car.length === 0) box.innerHTML = "<p style='text-align:center;'>El carrito est\'e1 vac\'edo.</p>";\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             car.forEach(item => \cf15 \strokec15 \{\{\cf10 \strokec10  \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 totalF += (item.p * item.q); \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 box.innerHTML += `\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <div class="item-car">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     <span>$\cf15 \strokec15 \{\{\cf10 \strokec10 item.n\cf15 \strokec15 \}\}\cf10 \strokec10 </span>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     <div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                         <button class="btn-qty" onclick="changeQty('$\cf15 \strokec15 \{\{\cf10 \strokec10 item.n\cf15 \strokec15 \}\}\cf10 \strokec10 ', -1)">-</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                         <span style="margin:0 10px;">$\cf15 \strokec15 \{\{\cf10 \strokec10 item.q\cf15 \strokec15 \}\}\cf10 \strokec10 </span>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                         <button class="btn-qty" onclick="changeQty('$\cf15 \strokec15 \{\{\cf10 \strokec10 item.n\cf15 \strokec15 \}\}\cf10 \strokec10 ', 1)">+</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     <span>$$\cf15 \strokec15 \{\{\cf10 \strokec10 item.p * item.q\cf15 \strokec15 \}\}\cf10 \strokec10 </span>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 </div>`;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf15 \strokec15 \}\}\cf10 \strokec10 );\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             document.getElementById('total-car').innerText = "Total: $" + totalF; show('view-carrito');\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10         function irAPagar() \cf15 \strokec15 \{\{\cf10 \strokec10  \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             if(car.length === 0) alert("\uc0\u9888 \u65039  No tienes nada en el carrito."); \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             else show('pago-final'); \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10         function confirmarVenta() \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             const campos = ['p-nom', 'p-cel', 'p-cor', 'p-ciu', 'p-dir'];\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             for(let c of campos) if(!document.getElementById(c).value) return alert("\uc0\u9888 \u65039  Rellena todos los campos obligatorios (*)");\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             const metodo = document.getElementById('p-met').value;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             const datos = \cf15 \strokec15 \{\{\cf10 \strokec10  \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 nom: document.getElementById('p-nom').value, \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 cel: document.getElementById('p-cel').value,\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 cor: document.getElementById('p-cor').value,\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 ciu: document.getElementById('p-ciu').value, \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 dir: document.getElementById('p-dir').value,\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 obs: document.getElementById('p-obs').value, \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 metodo: metodo,\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 total: totalF \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf15 \strokec15 \}\}\cf10 \strokec10 ;\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10             fetch('/finalizar_pedido', \cf15 \strokec15 \{\{\cf10 \strokec10  method: 'POST', headers: \cf15 \strokec15 \{\{\cf10 \strokec10 'Content-Type': 'application/json'\cf15 \strokec15 \}\}\cf10 \strokec10 , body: JSON.stringify(datos) \cf15 \strokec15 \}\}\cf10 \strokec10 )\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             .then(() => \cf15 \strokec15 \{\{\cf10 \strokec10  \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 if(metodo === "Efectivo") \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     document.getElementById('contenedor-pago').innerHTML = `\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                         <div style="text-align:center; padding: 20px;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                             <h2 style="color:var(--cafe); margin-bottom:10px;">TU PEDIDO A SIDO RESIVIDO GRACIAS POR TU COMPRA.</h2>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                             <p style="font-size:0.8rem; color:#666;">su pedido llegara seguro y perfecto a su casa.</p>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                             <br>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                             <button class="btn-portal" onclick="location.reload()" style="width:100%;">VOLVER AL INICIO</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     `;\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 \cf15 \strokec15 \}\}\cf10 \strokec10  else \cf15 \strokec15 \{\{\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     alert("\'a1Pedido realizado con \'e9xito!");\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                     location.reload();\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf15 \strokec15 \}\}\cf10 \strokec10 );\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </script>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     """\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 # --- RUTAS DE ADMINISTRACI\'d3N ---\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/auth'\cf4 \strokec4 , \cf16 \strokec16 methods\cf9 \strokec9 =\cf4 \strokec4 [\cf10 \strokec10 'POST'\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 auth\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 request\cf4 \strokec4 .\cf7 \strokec7 form\cf4 \strokec4 [\cf10 \strokec10 'u'\cf4 \strokec4 ] \cf9 \strokec9 ==\cf4 \strokec4  \cf11 \strokec11 USER_ADMIN\cf4 \strokec4  \cf13 \strokec13 and\cf4 \strokec4  \cf7 \strokec7 request\cf4 \strokec4 .\cf7 \strokec7 form\cf4 \strokec4 [\cf10 \strokec10 'p'\cf4 \strokec4 ] \cf9 \strokec9 ==\cf4 \strokec4  \cf11 \strokec11 PASS_ADMIN\cf4 \strokec4 :\cb1 \
\cb3         \cf7 \strokec7 session\cf4 \strokec4 [\cf10 \strokec10 'admin'\cf4 \strokec4 ] \cf9 \strokec9 =\cf4 \strokec4  \cf13 \strokec13 True\cf4 \cb1 \strokec4 \
\cb3         \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/panel'\cf4 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf10 \strokec10 "Error"\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/panel'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 panel\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 session\cf4 \strokec4 .\cf6 \strokec6 get\cf4 \strokec4 (\cf10 \strokec10 'admin'\cf4 \strokec4 ): \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/'\cf4 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 render_template_string\cf4 \strokec4 (\cf12 \strokec12 f\cf10 \strokec10 """\cf12 \strokec12 \{\cf11 \strokec11 CSS_MASTER\cf12 \strokec12 \}\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10     <div class="btn-menu" onclick="toggleMenu('side-a', true)">\uc0\u9776 </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div id="side-a" class="sidebar">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <a href="/panel">\uc0\u55356 \u57312  INICIO</a> \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <a href="/pedidos">\uc0\u55357 \u56550  PEDIDOS</a> \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <a href="/admin_productos">\uc0\u55356 \u57166  PRODUCTOS</a>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <a href="/usuarios">\uc0\u55357 \u56421  USUARIOS</a> \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <a href="/">SALIR</a>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div class="view active" style="justify-content:center; align-items:center;"><h1>PANEL DE CONTROL</h1></div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <script>function toggleMenu(id, o) \cf15 \strokec15 \{\{\cf10 \strokec10  document.getElementById(id).style.left = o ? '0' : '-300px'; \cf15 \strokec15 \}\}\cf10 \strokec10 </script>"""\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/admin_productos'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 admin_productos\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 session\cf4 \strokec4 .\cf6 \strokec6 get\cf4 \strokec4 (\cf10 \strokec10 'admin'\cf4 \strokec4 ): \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/'\cf4 \strokec4 )\cb1 \
\cb3     \cf7 \strokec7 filas\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 ""\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf4 \strokec4  \cf7 \strokec7 nom\cf4 \strokec4 , \cf7 \strokec7 info\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf7 \strokec7 productos_db\cf4 \strokec4 .\cf6 \strokec6 items\cf4 \strokec4 ():\cb1 \
\cb3         \cf7 \strokec7 filas\cf4 \strokec4  \cf9 \strokec9 +=\cf4 \strokec4  \cf12 \strokec12 f\cf10 \strokec10 """\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10         <tr>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <td>\cf12 \strokec12 \{\cf7 \strokec7 nom\cf12 \strokec12 \}\cf10 \strokec10 </td>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <td>$\cf12 \strokec12 \{\cf7 \strokec7 info\cf4 \strokec4 [\cf10 \strokec10 'precio'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <td>\cf12 \strokec12 \{\cf7 \strokec7 info\cf4 \strokec4 [\cf10 \strokec10 'estado'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <td>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <a href="/cambiar_estado/\cf12 \strokec12 \{\cf7 \strokec7 nom\cf12 \strokec12 \}\cf10 \strokec10 /Disponible"><button style="background:#2ecc71; color:white; border:none; cursor:pointer;">Disponible</button></a>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <a href="/cambiar_estado/\cf12 \strokec12 \{\cf7 \strokec7 nom\cf12 \strokec12 \}\cf10 \strokec10 /Agotado"><button style="background:#e74c3c; color:white; border:none; cursor:pointer;">Agotado</button></a>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <a href="/cambiar_estado/\cf12 \strokec12 \{\cf7 \strokec7 nom\cf12 \strokec12 \}\cf10 \strokec10 /No Disponible Temporalmente"><button style="background:#f39c12; color:white; border:none; cursor:pointer;">Temporal</button></a>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             </td>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </tr>"""\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 render_template_string\cf4 \strokec4 (\cf12 \strokec12 f\cf10 \strokec10 """\cf12 \strokec12 \{\cf11 \strokec11 CSS_MASTER\cf12 \strokec12 \}\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10     <div class="btn-menu" onclick="toggleMenu('side-a', true)">\uc0\u9776 </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div id="side-a" class="sidebar">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <a href="/panel">\uc0\u55356 \u57312  INICIO</a><a href="/pedidos">\u55357 \u56550  PEDIDOS</a><a href="/admin_productos">\u55356 \u57166  PRODUCTOS</a><a href="/usuarios">\u55357 \u56421  USUARIOS</a><a href="/">SALIR</a>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div class="view active" style="padding:80px 20px; align-items:center;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <h1>GESTI\'d3N DE PRODUCTOS</h1>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:90%; margin-bottom:20px;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <h3>AGREGAR PRODUCTO NUEVO</h3>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <form action="/nuevo_producto" method="POST" style="display:flex; flex-direction:column; align-items:center;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <input type="text" name="nom" placeholder="Nombre del Postre" required style="width:80%;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <input type="number" name="precio" placeholder="Precio ($)" required style="width:80%;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <button type="submit" class="btn-portal" style="width:80%;">CREAR PRODUCTO</button>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             </form>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:90%;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <table>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <thead><tr><th>Producto</th><th>Precio</th><th>Estado</th><th>Acciones</th></tr></thead>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <tbody>\cf12 \strokec12 \{\cf7 \strokec7 filas\cf12 \strokec12 \}\cf10 \strokec10 </tbody>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             </table>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <script>function toggleMenu(id, o) \cf15 \strokec15 \{\{\cf10 \strokec10  document.getElementById(id).style.left = o ? '0' : '-300px'; \cf15 \strokec15 \}\}\cf10 \strokec10 </script>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     """\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/nuevo_producto'\cf4 \strokec4 , \cf16 \strokec16 methods\cf9 \strokec9 =\cf4 \strokec4 [\cf10 \strokec10 'POST'\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 nuevo_producto\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 nom\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 request\cf4 \strokec4 .\cf7 \strokec7 form\cf4 \strokec4 .\cf6 \strokec6 get\cf4 \strokec4 (\cf10 \strokec10 'nom'\cf4 \strokec4 )\cb1 \
\cb3     \cf7 \strokec7 precio\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 request\cf4 \strokec4 .\cf7 \strokec7 form\cf4 \strokec4 .\cf6 \strokec6 get\cf4 \strokec4 (\cf10 \strokec10 'precio'\cf4 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 nom\cf4 \strokec4  \cf13 \strokec13 and\cf4 \strokec4  \cf7 \strokec7 precio\cf4 \strokec4 :\cb1 \
\cb3         \cf7 \strokec7 productos_db\cf4 \strokec4 [\cf7 \strokec7 nom\cf4 \strokec4 ] \cf9 \strokec9 =\cf4 \strokec4  \{\cf10 \strokec10 'precio'\cf4 \strokec4 : \cf5 \strokec5 int\cf4 \strokec4 (\cf7 \strokec7 precio\cf4 \strokec4 ), \cf10 \strokec10 'estado'\cf4 \strokec4 : \cf10 \strokec10 'Disponible'\cf4 \strokec4 \}\cb1 \
\cb3         \cf6 \strokec6 guardar_todo\cf4 \strokec4 ()\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/admin_productos'\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/cambiar_estado/<nom>/<estado>'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 cambiar_estado\cf4 \strokec4 (\cf16 \strokec16 nom\cf4 \strokec4 , \cf16 \strokec16 estado\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf16 \strokec16 nom\cf4 \strokec4  \cf13 \strokec13 in\cf4 \strokec4  \cf7 \strokec7 productos_db\cf4 \strokec4 :\cb1 \
\cb3         \cf7 \strokec7 productos_db\cf4 \strokec4 [\cf16 \strokec16 nom\cf4 \strokec4 ][\cf10 \strokec10 'estado'\cf4 \strokec4 ] \cf9 \strokec9 =\cf4 \strokec4  \cf16 \strokec16 estado\cf4 \cb1 \strokec4 \
\cb3         \cf6 \strokec6 guardar_todo\cf4 \strokec4 () \cf8 \strokec8 # Guardar cambio de stock\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/admin_productos'\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/pedidos'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 pedidos\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 session\cf4 \strokec4 .\cf6 \strokec6 get\cf4 \strokec4 (\cf10 \strokec10 'admin'\cf4 \strokec4 ): \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/'\cf4 \strokec4 )\cb1 \
\cb3     \cf7 \strokec7 filas\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 ""\cf4 \strokec4 .\cf6 \strokec6 join\cf4 \strokec4 ([\cf12 \strokec12 f\cf10 \strokec10 "<tr><td>\cf12 \strokec12 \{\cf7 \strokec7 p\cf4 \strokec4 [\cf10 \strokec10 'fecha'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>\cf12 \strokec12 \{\cf7 \strokec7 p\cf4 \strokec4 [\cf10 \strokec10 'nom'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>\cf12 \strokec12 \{\cf7 \strokec7 p\cf4 \strokec4 [\cf10 \strokec10 'cel'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>\cf12 \strokec12 \{\cf7 \strokec7 p\cf4 \strokec4 [\cf10 \strokec10 'ciu'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>\cf12 \strokec12 \{\cf7 \strokec7 p\cf4 \strokec4 [\cf10 \strokec10 'dir'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>\cf12 \strokec12 \{\cf7 \strokec7 p\cf4 \strokec4 [\cf10 \strokec10 'obs'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>$\cf12 \strokec12 \{\cf7 \strokec7 p\cf4 \strokec4 [\cf10 \strokec10 'total'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td></tr>"\cf4 \strokec4  \cf2 \strokec2 for\cf4 \strokec4  \cf7 \strokec7 p\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf7 \strokec7 pedidos_reales\cf4 \strokec4 ])\cb1 \
\cb3     \cb1 \
\cb3     \cf8 \strokec8 # L\'f3gica de gr\'e1ficas corregida: En 0 si no hay nada\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 data_grafica\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  [\cf14 \strokec14 0\cf4 \strokec4 , \cf14 \strokec14 0\cf4 \strokec4 , \cf14 \strokec14 0\cf4 \strokec4 , \cf14 \strokec14 0\cf4 \strokec4 , \cf14 \strokec14 0\cf4 \strokec4 , \cf14 \strokec14 0\cf4 \strokec4 , \cf14 \strokec14 0\cf4 \strokec4 ]\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf6 \strokec6 len\cf4 \strokec4 (\cf7 \strokec7 pedidos_reales\cf4 \strokec4 ) \cf9 \strokec9 >\cf4 \strokec4  \cf14 \strokec14 0\cf4 \strokec4 :\cb1 \
\cb3         \cf7 \strokec7 data_grafica\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  [\cf14 \strokec14 10\cf4 \strokec4 , \cf14 \strokec14 20\cf4 \strokec4 , \cf14 \strokec14 15\cf4 \strokec4 , \cf14 \strokec14 30\cf4 \strokec4 , \cf14 \strokec14 25\cf4 \strokec4 , \cf14 \strokec14 40\cf4 \strokec4 , \cf14 \strokec14 50\cf4 \strokec4 ] \cf8 \strokec8 # Datos ejemplo si hay ventas\cf4 \cb1 \strokec4 \
\
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 render_template_string\cf4 \strokec4 (\cf12 \strokec12 f\cf10 \strokec10 """\cf12 \strokec12 \{\cf11 \strokec11 CSS_MASTER\cf12 \strokec12 \}\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10     <div class="btn-menu" onclick="toggleMenu('side-a', true)">\uc0\u9776 </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div id="side-a" class="sidebar"><a href="/panel">\uc0\u55356 \u57312  INICIO</a><a href="/pedidos">\u55357 \u56550  PEDIDOS</a><a href="/admin_productos">\u55356 \u57166  PRODUCTOS</a><a href="/usuarios">\u55357 \u56421  USUARIOS</a><a href="/">SALIR</a></div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div style="padding:60px 20px; display:flex; flex-direction:column; align-items:center; background:#f4f4f4;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <h1>REPORTE DE PEDIDOS</h1>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:600px; padding:15px;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <canvas id="grafica" style="max-height: 250px;"></canvas>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:95%; text-align:left; overflow-x:auto;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <table>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <thead><tr><th>Fecha</th><th>Cliente</th><th>Celular</th><th>Ciudad</th><th>Ubicaci\'f3n</th><th>Obs.</th><th>Total</th></tr></thead>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <tbody>\cf12 \strokec12 \{\cf7 \strokec7 filas\cf4 \strokec4  \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 filas\cf4 \strokec4  \cf2 \strokec2 else\cf4 \strokec4  \cf10 \strokec10 '<tr><td colspan="7" style="text-align:center">No hay pedidos registrados</td></tr>'\cf12 \strokec12 \}\cf10 \strokec10 </tbody>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             </table>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <script>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         function toggleMenu(id, o) \cf15 \strokec15 \{\{\cf10 \strokec10  document.getElementById(id).style.left = o ? '0' : '-300px'; \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         const c = document.getElementById('grafica').getContext('2d');\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         new Chart(c, \cf15 \strokec15 \{\{\cf10 \strokec10  \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             type:'line', \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             data:\cf15 \strokec15 \{\{\cf10 \strokec10  \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 labels:['Lun','Mar','Mie','Jue','Vie','Sab','Dom'], \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 datasets:[\cf15 \strokec15 \{\{\cf10 \strokec10 label:'Ventas $', data:\cf12 \strokec12 \{\cf7 \strokec7 data_grafica\cf12 \strokec12 \}\cf10 \strokec10 , borderColor:'#4e342e', fill: false\cf15 \strokec15 \}\}\cf10 \strokec10 ] \cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             \cf15 \strokec15 \}\}\cf10 \strokec10 ,\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             options: \cf15 \strokec15 \{\{\cf10 \strokec10  scales: \cf15 \strokec15 \{\{\cf10 \strokec10  y: \cf15 \strokec15 \{\{\cf10 \strokec10  beginAtZero: true \cf15 \strokec15 \}\}\cf10 \strokec10  \cf15 \strokec15 \}\}\cf10 \strokec10  \cf15 \strokec15 \}\}\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         \cf15 \strokec15 \}\}\cf10 \strokec10 );\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </script>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     """\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/finalizar_pedido'\cf4 \strokec4 , \cf16 \strokec16 methods\cf9 \strokec9 =\cf4 \strokec4 [\cf10 \strokec10 'POST'\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 finalizar_pedido\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 d\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 request\cf4 \strokec4 .\cf7 \strokec7 json\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 pedidos_reales\cf4 \strokec4 .\cf6 \strokec6 append\cf4 \strokec4 (\{\cf10 \strokec10 "fecha"\cf4 \strokec4 : \cf5 \strokec5 datetime\cf4 \strokec4 .\cf6 \strokec6 now\cf4 \strokec4 ().\cf6 \strokec6 strftime\cf4 \strokec4 (\cf10 \strokec10 "%Y-%m-\cf12 \strokec12 %d\cf10 \strokec10  %H:%M"\cf4 \strokec4 ), \cf9 \strokec9 **\cf7 \strokec7 d\cf4 \strokec4 \})\cb1 \
\cb3     \cf6 \strokec6 guardar_todo\cf4 \strokec4 () \cf8 \strokec8 # Guardar pedido\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 jsonify\cf4 \strokec4 (\{\cf10 \strokec10 "status"\cf4 \strokec4 : \cf10 \strokec10 "ok"\cf4 \strokec4 \})\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/validar_registro'\cf4 \strokec4 , \cf16 \strokec16 methods\cf9 \strokec9 =\cf4 \strokec4 [\cf10 \strokec10 'POST'\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 validar_registro\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 d\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 request\cf4 \strokec4 .\cf7 \strokec7 json\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 usuarios_registrados\cf4 \strokec4 [\cf7 \strokec7 d\cf4 \strokec4 [\cf10 \strokec10 'cor'\cf4 \strokec4 ]] \cf9 \strokec9 =\cf4 \strokec4  \{\cf9 \strokec9 **\cf7 \strokec7 d\cf4 \strokec4 , \cf10 \strokec10 "bloqueado"\cf4 \strokec4 : \cf13 \strokec13 False\cf4 \strokec4 \}\cb1 \
\cb3     \cf6 \strokec6 guardar_todo\cf4 \strokec4 () \cf8 \strokec8 # Guardar usuario\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 jsonify\cf4 \strokec4 (\{\cf10 \strokec10 "status"\cf4 \strokec4 : \cf10 \strokec10 "ok"\cf4 \strokec4 \})\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/validar_login'\cf4 \strokec4 , \cf16 \strokec16 methods\cf9 \strokec9 =\cf4 \strokec4 [\cf10 \strokec10 'POST'\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 validar_login\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 d\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 request\cf4 \strokec4 .\cf7 \strokec7 json\cf4 \cb1 \strokec4 \
\cb3     \cf7 \strokec7 u\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf7 \strokec7 usuarios_registrados\cf4 \strokec4 .\cf6 \strokec6 get\cf4 \strokec4 (\cf7 \strokec7 d\cf4 \strokec4 [\cf10 \strokec10 'cor'\cf4 \strokec4 ])\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 u\cf4 \strokec4  \cf13 \strokec13 and\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 u\cf4 \strokec4 [\cf10 \strokec10 'bloqueado'\cf4 \strokec4 ] \cf13 \strokec13 and\cf4 \strokec4  \cf7 \strokec7 u\cf4 \strokec4 [\cf10 \strokec10 'pas'\cf4 \strokec4 ] \cf9 \strokec9 ==\cf4 \strokec4  \cf7 \strokec7 d\cf4 \strokec4 [\cf10 \strokec10 'pas'\cf4 \strokec4 ]: \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 jsonify\cf4 \strokec4 (\{\cf10 \strokec10 "status"\cf4 \strokec4 : \cf10 \strokec10 "ok"\cf4 \strokec4 \})\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 jsonify\cf4 \strokec4 (\{\cf10 \strokec10 "status"\cf4 \strokec4 : \cf10 \strokec10 "error"\cf4 \strokec4 , \cf10 \strokec10 "msg"\cf4 \strokec4 : \cf10 \strokec10 "Acceso Denegado"\cf4 \strokec4 \})\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/usuarios'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 usuarios\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 session\cf4 \strokec4 .\cf6 \strokec6 get\cf4 \strokec4 (\cf10 \strokec10 'admin'\cf4 \strokec4 ): \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/'\cf4 \strokec4 )\cb1 \
\cb3     \cf7 \strokec7 filas\cf4 \strokec4  \cf9 \strokec9 =\cf4 \strokec4  \cf10 \strokec10 ""\cf4 \strokec4 .\cf6 \strokec6 join\cf4 \strokec4 ([\cf12 \strokec12 f\cf10 \strokec10 "<tr><td>\cf12 \strokec12 \{\cf7 \strokec7 u\cf4 \strokec4 [\cf10 \strokec10 'nom'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>\cf12 \strokec12 \{\cf7 \strokec7 u\cf4 \strokec4 [\cf10 \strokec10 'cel'\cf4 \strokec4 ]\cf12 \strokec12 \}\cf10 \strokec10 </td><td>\cf12 \strokec12 \{\cf7 \strokec7 cor\cf12 \strokec12 \}\cf10 \strokec10 </td><td><a href='/bloq/\cf12 \strokec12 \{\cf7 \strokec7 cor\cf12 \strokec12 \}\cf10 \strokec10 '><button style='background:\cf12 \strokec12 \{\cf10 \strokec10 '#e74c3c'\cf4 \strokec4  \cf2 \strokec2 if\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 u\cf4 \strokec4 [\cf10 \strokec10 'bloqueado'\cf4 \strokec4 ] \cf2 \strokec2 else\cf4 \strokec4  \cf10 \strokec10 '#2ecc71'\cf12 \strokec12 \}\cf10 \strokec10 ; color:white; border:none; padding:5px; border-radius:5px;'>\cf12 \strokec12 \{\cf10 \strokec10 'Bloquear'\cf4 \strokec4  \cf2 \strokec2 if\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 u\cf4 \strokec4 [\cf10 \strokec10 'bloqueado'\cf4 \strokec4 ] \cf2 \strokec2 else\cf4 \strokec4  \cf10 \strokec10 'Desbloquear'\cf12 \strokec12 \}\cf10 \strokec10 </button></a></td></tr>"\cf4 \strokec4  \cf2 \strokec2 for\cf4 \strokec4  \cf7 \strokec7 cor\cf4 \strokec4 , \cf7 \strokec7 u\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf7 \strokec7 usuarios_registrados\cf4 \strokec4 .\cf6 \strokec6 items\cf4 \strokec4 ()])\cb1 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 render_template_string\cf4 \strokec4 (\cf12 \strokec12 f\cf10 \strokec10 """\cf12 \strokec12 \{\cf11 \strokec11 CSS_MASTER\cf12 \strokec12 \}\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10     <div class="btn-menu" onclick="toggleMenu('side-a', true)">\uc0\u9776 </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div id="side-a" class="sidebar"><a href="/panel">\uc0\u55356 \u57312  INICIO</a><a href="/pedidos">\u55357 \u56550  PEDIDOS</a><a href="/admin_productos">\u55356 \u57166  PRODUCTOS</a><a href="/usuarios">\u55357 \u56421  USUARIOS</a><a href="/">SALIR</a></div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <div class="view active" style="padding:80px 20px; align-items:center;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <h1>DATOS DE REGISTRO - USUARIOS</h1>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         <div class="caja-blanca" style="width:90%;">\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             <table>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <thead><tr><th>Nombre</th><th>Celular</th><th>Correo</th><th>Estado</th></tr></thead>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10                 <tbody>\cf12 \strokec12 \{\cf7 \strokec7 filas\cf4 \strokec4  \cf2 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 filas\cf4 \strokec4  \cf2 \strokec2 else\cf4 \strokec4  \cf10 \strokec10 '<tr><td colspan="4" style="text-align:center">No hay usuarios registrados</td></tr>'\cf12 \strokec12 \}\cf10 \strokec10 </tbody>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10             </table>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10         </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     </div>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     <script>function toggleMenu(id, o) \cf15 \strokec15 \{\{\cf10 \strokec10  document.getElementById(id).style.left = o ? '0' : '-300px'; \cf15 \strokec15 \}\}\cf10 \strokec10 </script>\cf4 \cb1 \strokec4 \
\cf10 \cb3 \strokec10     """\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 @\cf7 \strokec7 app\cf6 \strokec6 .route\cf4 \strokec4 (\cf10 \strokec10 '/bloq/<cor>'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf12 \cb3 \strokec12 def\cf4 \strokec4  \cf6 \strokec6 bloq\cf4 \strokec4 (\cf16 \strokec16 cor\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 \strokec2 if\cf4 \strokec4  \cf16 \strokec16 cor\cf4 \strokec4  \cf13 \strokec13 in\cf4 \strokec4  \cf7 \strokec7 usuarios_registrados\cf4 \strokec4 : \cb1 \
\cb3         \cf7 \strokec7 usuarios_registrados\cf4 \strokec4 [\cf16 \strokec16 cor\cf4 \strokec4 ][\cf10 \strokec10 'bloqueado'\cf4 \strokec4 ] \cf9 \strokec9 =\cf4 \strokec4  \cf13 \strokec13 not\cf4 \strokec4  \cf7 \strokec7 usuarios_registrados\cf4 \strokec4 [\cf16 \strokec16 cor\cf4 \strokec4 ][\cf10 \strokec10 'bloqueado'\cf4 \strokec4 ]\cb1 \
\cb3         \cf6 \strokec6 guardar_todo\cf4 \strokec4 () \cf8 \strokec8 # Guardar bloqueo\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 return\cf4 \strokec4  \cf6 \strokec6 redirect\cf4 \strokec4 (\cf10 \strokec10 '/usuarios'\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf4 \strokec4  \cf7 \strokec7 __name__\cf4 \strokec4  \cf9 \strokec9 ==\cf4 \strokec4  \cf10 \strokec10 '__main__'\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 \strokec7 app\cf4 \strokec4 .\cf6 \strokec6 run\cf4 \strokec4 (\cf16 \strokec16 debug\cf9 \strokec9 =\cf13 \strokec13 True\cf4 \strokec4 , \cf16 \strokec16 port\cf9 \strokec9 =\cf14 \strokec14 8000\cf4 \strokec4 )\cb1 \
}