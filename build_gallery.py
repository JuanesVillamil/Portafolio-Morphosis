
with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The gallery HTML replacement content
GALLERY = '''<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 GALER\u00cdA \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->
<section id="galeria" class="section">
  <div class="section-inner reveal">
    <div class="chapter-marker"><span class="chapter-num">Cap\u00edtulo VIII</span></div>
    <h2>Ecosistemas<span class="h2-original">\u00b7 Galer\u00eda \u00b7</span></h2>
    <p class="section-subtitle">Registro de mis ensambles en la Carrera de Artes Esc\u00e9nicas</p>
    <div class="flourish"></div>

    <style>
    .gal-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      margin: 2rem 0;
    }
    @media(max-width:900px){ .gal-grid { grid-template-columns: repeat(2,1fr); } }
    @media(max-width:500px){ .gal-grid { grid-template-columns: 1fr; } }
    .gal-card {
      cursor: pointer;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 18px rgba(0,0,0,0.13);
      transition: transform 0.25s, box-shadow 0.25s;
      background: #fff;
      position: relative;
      border: 1px solid rgba(184,146,74,0.25);
    }
    .gal-card:hover { transform: translateY(-5px); box-shadow: 0 10px 32px rgba(0,0,0,0.22); }
    .gal-card img { width: 100%; aspect-ratio: 4/5; object-fit: cover; display: block; }
    .gal-card-info { padding: 0.75rem 0.9rem; background: rgba(244,234,213,0.95); }
    .gal-card-info h3 {
      font-family: "Cormorant Garamond", serif;
      font-size: 1rem; font-weight: 700;
      color: var(--morpho-deep); margin: 0 0 0.25rem; letter-spacing: 0.03em;
    }
    .gal-card-info p {
      font-family: "Cormorant Garamond", serif;
      font-size: 0.8rem; color: var(--sepia); margin: 0; font-style: italic;
    }
    .gal-bonus-badge {
      position: absolute; top: 0.6rem; right: 0.6rem;
      background: linear-gradient(135deg,#b8924a,#d4af6a);
      color: #fff; font-size: 0.65rem; font-weight: 700;
      letter-spacing: 0.08em; text-transform: uppercase;
      padding: 0.2rem 0.5rem; border-radius: 20px; font-family: "Cinzel", serif;
    }
    .gal-trasescena-badge {
      position: absolute; top: 0.6rem; left: 0.6rem;
      background: linear-gradient(135deg,#2d3a6b,#4a5fa0);
      color: #fff; font-size: 0.6rem; font-weight: 700;
      letter-spacing: 0.08em; text-transform: uppercase;
      padding: 0.2rem 0.5rem; border-radius: 20px; font-family: "Cinzel", serif;
    }
    .gal-nophoto-card img { opacity: 0.6; filter: grayscale(20%); }
    .gal-modal {
      display: none; position: fixed; inset: 0;
      background: rgba(10,8,20,0.82); z-index: 9999;
      align-items: center; justify-content: center;
      padding: 1rem; backdrop-filter: blur(3px);
    }
    .gal-modal.open { display: flex; }
    .gal-modal-content {
      background: #f9f5ef; border-radius: 12px;
      max-width: 820px; width: 100%; max-height: 90vh; overflow-y: auto;
      position: relative;
      box-shadow: 0 20px 60px rgba(0,0,0,0.45);
      border: 1px solid rgba(184,146,74,0.3);
    }
    .gal-modal-header {
      background: var(--morpho-deep); color: #f4ead5;
      padding: 1.5rem 3rem 1.2rem 2rem; border-radius: 12px 12px 0 0;
    }
    .gal-modal-header h2 {
      font-family: "Cormorant Garamond", serif;
      font-size: 1.8rem; margin: 0 0 0.2rem; letter-spacing: 0.04em;
    }
    .gal-modal-header .gal-dir-line {
      font-family: "Cormorant Garamond", serif;
      font-size: 0.95rem; opacity: 0.8; font-style: italic;
    }
    .gal-modal-body { padding: 1.5rem 2rem; }
    @media(max-width:500px){ .gal-modal-body { padding: 1rem; } }
    .gal-trailer-btn {
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: linear-gradient(135deg,#1a2060,#2d3a8c);
      color: #fff; text-decoration: none;
      padding: 0.6rem 1.2rem; border-radius: 30px;
      font-family: "Cinzel", serif; font-size: 0.8rem;
      letter-spacing: 0.06em; font-weight: 600;
      margin-bottom: 1.2rem; transition: opacity 0.2s;
    }
    .gal-trailer-btn:hover { opacity: 0.85; }
    .gal-canva-btn {
      display: inline-flex; align-items: center; gap: 0.5rem;
      background: linear-gradient(135deg,#00c4cc,#0098a0);
      color: #fff; text-decoration: none;
      padding: 0.6rem 1.2rem; border-radius: 30px;
      font-family: "Cinzel", serif; font-size: 0.8rem;
      letter-spacing: 0.06em; font-weight: 600;
      margin-bottom: 1.2rem; transition: opacity 0.2s;
    }
    .gal-canva-btn:hover { opacity: 0.85; }
    .gal-trasescena-label {
      display: inline-block;
      background: linear-gradient(135deg,#2d3a6b,#4a5fa0);
      color: #fff; font-family: "Cinzel", serif;
      font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase;
      padding: 0.25rem 0.8rem; border-radius: 20px; margin-bottom: 0.8rem;
    }
    .gal-asist-label {
      display: inline-block;
      background: rgba(45,58,107,0.12); color: #2d3a6b;
      font-family: "Cormorant Garamond", serif;
      font-size: 0.85rem; font-style: italic;
      padding: 0.25rem 0.8rem; border-radius: 6px;
      margin-bottom: 0.8rem; border: 1px solid rgba(45,58,107,0.2);
    }
    .gal-synopsis {
      font-family: "Cormorant Garamond", serif;
      font-size: 1.05rem; line-height: 1.7; color: #3a3028;
      margin-bottom: 1.5rem; padding: 1rem 1.2rem;
      background: rgba(255,255,255,0.6);
      border-left: 3px solid var(--morpho-bright);
      border-radius: 0 6px 6px 0;
    }
    .gal-photos {
      display: grid; grid-template-columns: repeat(3,1fr); gap: 0.75rem; margin-top: 1rem;
    }
    @media(max-width:500px){ .gal-photos { grid-template-columns: 1fr; } }
    .gal-photos img {
      width: 100%; aspect-ratio: 3/4; object-fit: cover; border-radius: 6px;
      box-shadow: 0 3px 12px rgba(0,0,0,0.15); cursor: pointer; transition: transform 0.2s;
    }
    .gal-photos img:hover { transform: scale(1.02); }
    .gal-pending {
      font-family: "Cormorant Garamond", serif; font-style: italic;
      color: var(--sepia); font-size: 0.95rem; padding: 1rem;
      background: rgba(184,146,74,0.08); border-radius: 6px;
      border: 1px dashed rgba(184,146,74,0.35); text-align: center;
    }
    .gal-close {
      position: absolute; top: 1rem; right: 1rem;
      background: rgba(255,255,255,0.2); border: none;
      color: #f4ead5; font-size: 1.2rem;
      width: 2rem; height: 2rem; border-radius: 50%;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: background 0.2s; z-index: 10;
    }
    .gal-close:hover { background: rgba(255,255,255,0.35); }
    .gal-lightbox {
      display: none; position: fixed; inset: 0;
      background: rgba(0,0,0,0.92); z-index: 10000;
      align-items: center; justify-content: center;
    }
    .gal-lightbox.open { display: flex; }
    .gal-lightbox img {
      max-width: 90vw; max-height: 90vh; object-fit: contain;
      border-radius: 4px; box-shadow: 0 0 40px rgba(0,0,0,0.8);
    }
    .gal-lightbox-close {
      position: absolute; top: 1.5rem; right: 1.5rem;
      background: rgba(255,255,255,0.15); border: none;
      color: #fff; font-size: 1.5rem;
      width: 2.5rem; height: 2.5rem; border-radius: 50%; cursor: pointer;
    }
    </style>

    <div class="gal-grid">

      <div class="gal-card" onclick="openGal('condena')">
        <img src="img/gallery/condena-flyer.jpg" alt="La Condena">
        <div class="gal-card-info">
          <h3>La Condena</h3>
          <p>Dir. Isaac Barbosa y Juliana Atuesta</p>
        </div>
      </div>

      <div class="gal-card" onclick="openGal('intento')">
        <img src="img/gallery/intento-flyer.jpg" alt="Intento Optimista de un_ lun\u00e1tic_">
        <div class="gal-card-info">
          <h3>Intento Optimista de un_ lun\u00e1tic_</h3>
          <p>Dir. Arnulfo Pardo y Laura Castiblanco</p>
        </div>
      </div>

      <div class="gal-card" onclick="openGal('mientras')">
        <span class="gal-trasescena-badge">Trasescena</span>
        <img src="img/gallery/mientras-flyer.jpg" alt="Mientras Caemos">
        <div class="gal-card-info">
          <h3>Mientras Caemos</h3>
          <p>Dir. Diana Salamank y M. A. Morales</p>
        </div>
      </div>

      <div class="gal-card gal-nophoto-card" onclick="openGal('otracosa')">
        <img src="img/gallery/otracosa-flyer.jpg" alt="Otra cosa es otra cosa">
        <div class="gal-card-info">
          <h3>Otra cosa es otra cosa</h3>
          <p>Dir. Humberto Canessa</p>
        </div>
      </div>

      <div class="gal-card" onclick="openGal('t346')">
        <img src="img/gallery/346-flyer.jpg" alt="346">
        <div class="gal-card-info">
          <h3>346</h3>
          <p>Dir. Jonathan Hern\u00e1ndez</p>
        </div>
      </div>

      <div class="gal-card" onclick="openGal('ecdisis')">
        <img src="img/gallery/ecdisis-flyer.jpg" alt="Ecdisis">
        <div class="gal-card-info">
          <h3>Ecdisis</h3>
          <p>Dir. Jorge Bernal</p>
        </div>
      </div>

      <div class="gal-card gal-nophoto-card" onclick="openGal('madriguera')">
        <img src="img/gallery/madriguera-flyer.jpg" alt="La Madriguera">
        <div class="gal-card-info">
          <h3>La Madriguera</h3>
          <p>Dir. Humberto Canessa y Leonardo Gir\u00f3n</p>
        </div>
      </div>

      <div class="gal-card" onclick="openGal('tormenta')" style="background:linear-gradient(160deg,#1a2060,#2d3a8c);">
        <span class="gal-bonus-badge">Bonus</span>
        <div style="width:100%;aspect-ratio:4/5;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:0.8rem;padding:1.5rem;">
          <div style="font-size:3rem;">&#10052;</div>
          <p style="font-family:Cormorant Garamond,serif;font-size:1.15rem;font-weight:700;color:#f4ead5;text-align:center;margin:0;letter-spacing:0.05em;">Tormenta de Nieve</p>
          <p style="font-family:Cormorant Garamond,serif;font-size:0.85rem;color:rgba(244,234,213,0.75);text-align:center;margin:0;font-style:italic;">La Tempestad</p>
        </div>
        <div class="gal-card-info" style="background:rgba(26,32,96,0.92);">
          <h3 style="color:#d4af6a;">Creaci\u00f3n Colaborativa</h3>
          <p style="color:rgba(244,234,213,0.75);">Artes Visuales &middot; M\u00fasica &middot; Esc\u00e9nicas</p>
        </div>
      </div>

    </div>

    <div id="galModal" class="gal-modal" onclick="if(event.target===this)closeGal()">
      <div class="gal-modal-content">
        <button class="gal-close" onclick="closeGal()">&#x2715;</button>
        <div id="galModalInner"></div>
      </div>
    </div>

    <div id="galLightbox" class="gal-lightbox" onclick="closeLB()">
      <img id="galLBImg" src="" alt="">
      <button class="gal-lightbox-close" onclick="closeLB()">&#x2715;</button>
    </div>

    <script>
    var GD = {
      condena: {
        t: "La Condena",
        s: "XIX Temporada de Ensambles",
        d: "Isaac Barbosa y Juliana Atuesta",
        url: "https://www.instagram.com/reel/CzMapz9Jfe3/?igsh=cDR4Mml5a3Fmc3Fo",
        syn: "La Condena plantea una apertura performat\u00e9tica a un reportaje escrito por Santiago Wills, sobre la invaluable labor social y ambiental de Jani Rita Silva en la zona de reserva campesina del bajo Putumayo. Desde el valor expresivo de la performancia, nos permitimos dialogar con el documento, tanto su textualidad como con sus posibilidades interpretativas; dialogamos tambi\u00e9n desde nuestras existencias, nuestros discursos propios y nuestras aproximaciones al territorio. Convocamos la comprensi\u00f3n desde la potencia de la palabra, pero tambi\u00e9n del movimiento y de la presencia de nuestras diversas corporalidades. El documento nos permite ver a Jani, y Jani nos permite ser el reflejo que proyecta preguntas y posibilidades de conectarnos con nuestro contexto, de incidir, de denunciar, de cuestionar y de agenciar posibilidades po\u00e9ticas discursivas que toman lugar como espacio de creaci\u00f3n.",
        ph: ["img/gallery/condena-p1.jpg","img/gallery/condena-p2.jpg","img/gallery/condena-p3.jpg"]
      },
      intento: {
        t: "Intento Optimista de un_ lun\u00e1tic_",
        s: "XX Temporada de Ensambles",
        d: "Arnulfo Pardo y Laura Castiblanco",
        url: "https://www.instagram.com/reel/C6_KlndOqCp/?igsh=NzBqaXQ2YnNlZmVw",
        syn: "Y as\u00ed se repitieron a trav\u00e9s de los a\u00f1os los mismos poemas.<br>El sol, la lluvia, un arco\u00edris. Refracci\u00f3n. n1&middot;sin\u03b81=n2&middot;sin\u03b82<br>Pasaron tantas cosas... 5.175 pesos por una hora de trabajo. 45 minutos esperando el bus.<br>Pero \u00e9l nunca avanza, sino que el sendero pasa por debajo de \u00e9l.<br>... y apenas vio el destello porque la casa en la que creci\u00f3 ya no existe.<br>Un funeral. Nosotros y ellxs solo para un d\u00eda ocupado.<br>Se quemaba la punta de los dedos. Cabeza en llamas.<br>\u00bfY qui\u00e9n sabe qui\u00e9n es qui\u00e9n? Silencio.<br>Nunca pudo decir otra cosa y se qued\u00f3 girando...<br>... y al final es solo redondo y redondo y redondo...",
        ph: ["img/gallery/intento-p1.jpg","img/gallery/intento-p2.jpg","img/gallery/intento-p3.jpg"]
      },
      mientras: {
        t: "Mientras Caemos",
        s: "XXI Temporada Intersemestral",
        d: "Diana Salamank y Mar\u00eda Alejandra Morales",
        url: "https://www.instagram.com/reel/DCFJpLiJscp/?igsh=aXJnNG0wZTFkeXBz",
        canva: "https://www.canva.com/design/DAGU7DYvLG8/jcxWl8L6e84ktIJ0fxTv3Q/edit",
        trasescena: true,
        syn: "Es un c\u00famulo de cr\u00f3nicas basadas en exhibir, excavar, exponer las m\u00e1s profundas capas, los m\u00e1s profundos abismos internos del comportamiento del ser humano. Situaciones que capaz a cualquiera de nosotros nos puede suceder, podemos generar situaciones que en momentos nos confronta con esa voz interna, \u00edntima, solo nuestra, que no quisier\u00e9amos que nadie m\u00e1s escuchara. Esta propuesta esc\u00e9nica est\u00e1 basada en el universo literario del escritor bogotano Mario Mendoza, quien con sus palabras ha calado hondamente en este proceso creativo.",
        ph: []
      },
      otracosa: {
        t: "Otra cosa es otra cosa",
        s: "XXII Temporada de Ensambles",
        d: "Humberto Canessa",
        url: "https://www.instagram.com/reel/DKIEWTJA0-G/?igsh=a3luNnY3amM2bHA4",
        syn: "Soy una mujer...<br>Soy una mujer semilla de cambio.<br>Soy una mujer compuesta de c\u00e9lulas de deseos, convertidos en un cuerpo so\u00f1ador.<br>Soy una mujer oprimida en un mundo capitalista sin coraz\u00f3n repleto de dinero.<br>Soy una mujer desfaldada, desmedida, destaconada, despeinada.<br>Soy una mujer que construye su propio cuerpo.<br>Soy una mujer frutal, \u00e1cida, verdulera.",
        ph: []
      },
      t346: {
        t: "346",
        s: "XXIII Temporada de Ensambles",
        d: "Jonathan Hern\u00e1ndez",
        url: "https://www.instagram.com/reel/DQ4HmYWDZut/?igsh=OWNqenU5YnNzZHIz",
        syn: "346 es un viaje de emociones y de an\u00e9cdotas. Es el latido de un coraz\u00f3n cargado, que pulsa a trav\u00e9s de la memoria y las experiencias que buscan reunirse y ser compartidas. 346 es un suspiro que se eleva, con la esperanza del encuentro.",
        ph: ["img/gallery/346-p1.jpg","img/gallery/346-p2.jpg","img/gallery/346-p3.jpg"]
      },
      ecdisis: {
        t: "Ecdisis",
        s: "XXIII Temporada de Ensambles",
        d: "Jorge Bernal",
        url: "https://www.instagram.com/reel/DRKWqXDgGhg/?igsh=ZjFlemZrcTZlbWNw",
        syn: "Retoma como referente el proceso natural y vital en el que muchos animales, especialmente invertebrados como los artr\u00f3podos y reptiles, se desprenden de su capa externa antigua para poder crecer.<br><br>Es un acto repetitivo, un ciclo, una transformaci\u00f3n...<br><br>Un desprendimiento que deja atr\u00e1s lo viejo para abrir espacio a lo nuevo, una serpenteante memoria de lo que fue...<br><br>Columna vertebral que viene de la tierra. Mujer lunar, astuta y sanadora. Oscura, silenciosa y prudente.",
        ph: ["img/gallery/ecdisis-p1.jpg","img/gallery/ecdisis-p2.jpg","img/gallery/ecdisis-p3.jpg"]
      },
      madriguera: {
        t: "La Madriguera",
        s: "Ensamble Intensivo &middot; 2026-01",
        d: "Humberto Canessa y Leonardo Gir\u00f3n",
        url: null,
        syn: "\u201cLa Madriguera\u201d, un centro de reciclaje olvidado de la ciudad donde se acumula la basura... y tambi\u00e9n los sue\u00f1os. Vive Juani Pi, una ni\u00f1a valiente que, entre monta\u00f1as de desechos, descubrir\u00e1 un universo de juego, imaginaci\u00f3n y magia.<br><br>Rodeada de personajes tan extra\u00f1os como entra\u00f1ables que, a trav\u00e9s del circo, el movimiento y la fantas\u00eda, le revelar\u00e1n algo fundamental: que los ni\u00f1os tienen derechos... derecho a jugar, a tener una familia, a un hogar, a ser cuidados y a so\u00f1ar.<br><br>Un universo donde lo que parec\u00eda desechado vuelve a brillar y donde todos recordamos que tenemos derecho a la felicidad.",
        ph: [],
        pending: true
      },
      tormenta: {
        t: "Tormenta de Nieve",
        s: "La Tempestad &middot; Creaci\u00f3n Colaborativa",
        d: "Creaci\u00f3n colectiva &middot; Artes Visuales, M\u00fasica y Artes Esc\u00e9nicas",
        url: "https://www.instagram.com/reel/DH4T46DhId3/?igsh=MW5xaGJhYnJ5eWtocg==",
        bonus: true,
        syn: null,
        ph: ["img/gallery/tormenta-p1.jpg","img/gallery/tormenta-p2.jpg","img/gallery/tormenta-p3.jpg"]
      }
    };

    function openGal(id) {
      var d = GD[id]; if (!d) return;
      var h = '<div class="gal-modal-header"><h2>' + d.t + '</h2>';
      h += '<div class="gal-dir-line">' + d.s + ' &nbsp;&middot;&nbsp; Dir. ' + d.d + '</div></div>';
      h += '<div class="gal-modal-body">';
      if (d.trasescena) {
        h += '<span class="gal-trasescena-label">Ensamble Trasescena</span><br>';
        h += '<span class="gal-asist-label">Rol: Asistente de Direcci\u00f3n y Producci\u00f3n</span><br><br>';
      }
      if (d.bonus) {
        h += '<span class="gal-bonus-badge" style="position:static;display:inline-block;margin-bottom:0.8rem;">Creaci\u00f3n Bonus</span><br><br>';
      }
      if (d.url) {
        h += '<a href="' + d.url + '" target="_blank" rel="noopener" class="gal-trailer-btn">';
        h += '<svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>';
        h += ' Ver Tr\u00e1iler en Instagram</a>&nbsp;';
      }
      if (d.canva) {
        h += '<a href="' + d.canva + '" target="_blank" rel="noopener" class="gal-canva-btn">';
        h += '<svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>';
        h += ' Ver Trabajo en Canva</a>';
      }
      if (d.url || d.canva) h += '<br><br>';
      if (d.syn) h += '<div class="gal-synopsis">' + d.syn + '</div>';
      if (d.ph && d.ph.length > 0) {
        h += '<div class="gal-photos">';
        for (var i = 0; i < d.ph.length; i++) {
          h += '<img src="' + d.ph[i] + '" alt="Foto" onclick="openLB(this.src)" loading="lazy">';
        }
        h += '</div>';
      } else if (d.pending) {
        h += '<p class="gal-pending">&#128247; Fotograf\u00edas en proceso de edici\u00f3n \u2014 pr\u00f3ximamente disponibles</p>';
      } else if (d.trasescena) {
        h += '<p class="gal-pending">Particip\u00e9 como Asistente de Direcci\u00f3n, no como ejecutante en escena.</p>';
      } else if (!d.bonus) {
        h += '<p class="gal-pending">&#128247; Fotograf\u00edas pr\u00f3ximamente \u2014 el fot\u00f3grafo est\u00e1 recopilando el material</p>';
      }
      h += '</div>';
      document.getElementById('galModalInner').innerHTML = h;
      document.getElementById('galModal').classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeGal() {
      document.getElementById('galModal').classList.remove('open');
      document.body.style.overflow = '';
    }
    function openLB(src) {
      document.getElementById('galLBImg').src = src;
      document.getElementById('galLightbox').classList.add('open');
    }
    function closeLB() {
      document.getElementById('galLightbox').classList.remove('open');
    }
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') { closeGal(); closeLB(); }
    });
    </script>

  </div>
</section>
'''

# Locate section boundaries in the HTML
START = '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 GALER\u00cdA \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->'
END   = '<!-- \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 FOOTER \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550 -->'

si = html.index(START)
ei = html.index(END)

out = html[:si] + GALLERY + '\n' + html[ei:]

with open('/sessions/fervent-stoic-mccarthy/mnt/outputs/index.html', 'w', encoding='utf-8') as f:
    f.write(out)

print("Success. Lines:", out.count('\n'))
print("openGal present:", 'openGal' in out)
print("Gallery images present:", 'condena-flyer' in out)
