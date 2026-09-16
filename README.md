# Grandi Origini Catastali Italiane (Cassini-Soldner)

Repository di documentazione e parametri geodetici per i centri di emanazione delle **Grandi Origini catastali** (proiezione Cassini-Soldner) dell'Agenzia delle Entrate / Catasto italiano.

Contiene coordinate di riferimento (Est/Nord, Lat/Lon WGS84), ripartizione per province, stringhe per definizioni personalizzate **PROJ** con pulsante di copia dedicato per ciascuna origine e istruzioni operative per l'uso in ambienti GIS (**QGIS**, GDAL, PostGIS).

---

## 📌 Indice
1. [Inquadramento Generale](#-inquadramento-generale)
2. [Tabella Sinottica delle Origini](#-tabella-sinottica-delle-origini)
3. [Stringhe PROJ con Copia Rapida](#-stringhe-proj-con-copia-rapida)
4. [Guida all'Uso in QGIS](#-guida-alluso-in-qgis)
   - [A. Creazione del CRS Cassini-Soldner personalizzato](#a-creazione-del-crs-cassini-soldner-personalizzato)
   - [B. Importazione e visualizzazione del layer dei centri di emanazione](#b-importazione-e-visualizzazione-del-layer-dei-centri-di-emanazione)
5. [Note Geodetiche e Tecniche](#-note-geodetiche-e-tecniche)
6. [Licenza e Utilizzo](#-licenza-e-utilizzo)

---

## 📖 Inquadramento Generale

Nel sistema catastale italiano le mappe geometriche particellari storiche sono state costituite su sistemi di coordinate piane a proiezione analitica **Cassini-Soldner**. 

Ciascun sistema locale è incentrato su uno specifico punto trigonometrico fondamentale (vertice trigonometrico, torri o punti ideali) denominato **Grande Origine** o **Centro di Emanazione**. Le mappe catastali delle province collegate a una determinata origine esprimono le posizioni in metri rispetto agli assi cartesiani ortogonali passanti per quel punto:
- Asse delle ascisse ($X$ o $Est$): perpendicolare al meridiano di emanazione.
- Asse delle ordinate ($Y$ o $Nord$): coincidente con il meridiano di emanazione.

---

## 📊 Tabella Sinottica delle Origini

| N° | Origine / Punto Trigonometrico | Nord (m) | Est (m) | Latitudine (°N) | Longitudine (°E) | Province di Competenza |
|:---:|:---|---:|---:|---:|---:|:---|
| **1** | Vercelli (Punto Ideale) | 5033316.62 | 1437864.36 | 45.45042576 | 8.20503948 | Biella, Novara (parte), Verbano Cusio Ossola, Vercelli |
| **2** | Pordenone | 5091681.44 | 2338704.15 | 45.95458397 | 12.66047164 | Belluno (gran parte), Udine (parte), Venezia (parte) |
| **3** | Monte Bronzone | 5062219.67 | 1577145.63 | 45.70905303 | 9.99074064 | Sondrio, Bergamo, Brescia, Cremona |
| **4** | Lodi | 5017990.42 | 1539453.24 | 45.31413505 | 9.50297431 | Como, Milano, Parma (parte), Piacenza (parte) |
| **5** | Alessandria | 4973570.20 | 1469349.75 | 44.91472668 | 8.61134796 | Alessandria (parte), Asti (parte) |
| **6** | Monte Bignone | 4858622.59 | 1398286.99 | 43.87352936 | 7.73372694 | Imperia |
| **7** | Forte Diamante | 4923110.92 | 1495211.83 | 44.46112587 | 8.93946834 | Genova (gran parte), La Spezia (gran parte), Savona, Parma (gran parte) |
| **8** | Portonovo | 4934722.35 | 1718797.19 | 44.53248216 | 11.75335874 | Bologna, Ferrara, Forlì, Rimini, Ravenna, Rovigo |
| **9** | Siena (Torre del Mangia) | 4798817.15 | 1689143.93 | 43.31828703 | 11.33221016 | Arezzo, Firenze, Grosseto, Livorno (gran parte), Lucca (parte), Pisa (gran parte), Pistoia, Siena |
| **10** | Urbino | 4844075.80 | 2329619.57 | 43.72514932 | 12.63626776 | Pesaro, Urbino |
| **11** | Monte Pennino | 4774249.57 | 2348202.28 | 43.10138543 | 12.88876541 | Ascoli Piceno, Fermo, Macerata, Perugia, Arezzo (piccola parte) |
| **12** | Monte Mario | 4644532.03 | 2308739.38 | 41.92439627 | 12.45214521 | Frosinone (parte), Littoria (parte), Roma (gran parte), Viterbo, Terni |
| **13** | Monte Ocre | 4679435.16 | 2391587.01 | 42.25645724 | 13.44313386 | Aquila, Pescara (piccola parte), Rieti |
| **14** | Monte Pietrereie (Monte Palombo) | 4611304.82 | 2458358.88 | 41.65102260 | 14.25965522 | Benevento (parte), Campobasso (gran parte), Chieti, Pescara (gran parte), Isernia, Teramo |
| **16** | Taranto (Cattedrale) | 4483002.72 | 2708912.67 | 40.47618517 | 17.22847695 | Taranto (gran parte), Brindisi (parte) |
| **17** | Lecce | 4471650.16 | 2789164.74 | 40.35195558 | 18.16922358 | Lecce, Brindisi (parte), Taranto (piccola parte) |
| **18** | Monte Bruto | 4333378.75 | 2642886.51 | 39.14090145 | 16.42183592 | Cosenza, Catanzaro, Reggio Calabria |
| **19** | Torre Titone | 4191811.43 | 2303526.25 | 37.84805703 | 12.53962245 | Trapani (esclusa Pantelleria) |
| **20** | Monte Etna (Punta Lucia) | 4179704.64 | 2518709.12 | 37.76465593 | 14.98527080 | Messina, Catania (parte) |
| **21** | Monte Castelluccio | 4141719.28 | 2411977.49 | 37.41597534 | 13.77923129 | Agrigento (escluse isole), Caltanissetta, Enna (parte) |
| **22** | Mineo | 4124536.45 | 2492734.53 | 37.26699983 | 14.69242068 | Siracusa, Ragusa |
| **23** | Sardegna (Punto Ideale) | 4427815.65 | 1510008.25 | 40.00039120 | 9.11695110 | Cagliari, Nuoro, Sassari |
| **24** | Innsbruck | 5237890.45 | 1681094.46 | 47.26927415 | 11.39370656 | Trento, Bolzano |
| **27** | Monte Cairo | 4599624.86 | 2416623.61 | 41.54152292 | 13.76055843 | Frosinone (parte), Napoli (parte) |
| **28** | Francolise | 4559460.60 | 2441482.72 | 41.18261872 | 14.06374347 | Napoli (parte), Campobasso (parte), Benevento (parte) |
| **29** | Cancello (Castello) | 4521180.39 | 2472074.94 | 40.84019413 | 14.43144708 | Napoli (parte) |
| **30** | Miradois (Osservatorio Capodimonte) | 4523895.55 | 2457265.54 | 40.86365124 | 14.25552353 | Napoli (parte) |
| **31** | Monte Petrella | 4575392.36 | 2408326.59 | 41.32219558 | 13.66559070 | Frosinone (parte), Littoria (parte) |
| **32** | Marigliano | 4530606.62 | 2474204.30 | 40.92522593 | 14.45600831 | Napoli (parte) |

---

## 📐 Stringhe PROJ con Copia Rapida

Su GitHub ogni blocco di codice seguente attiva automaticamente l'icona nativa di **copia negli appunti**:

**1) Vercelli (Punto Ideale)**
```proj
+proj=cass +lat_0=45.45042576 +lon_0=8.20503948 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**2) Pordenone**
```proj
+proj=cass +lat_0=45.95458397 +lon_0=12.66047164 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**3) Monte Bronzone**
```proj
+proj=cass +lat_0=45.70905303 +lon_0=9.99074064 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**4) Lodi**
```proj
+proj=cass +lat_0=45.31413505 +lon_0=9.50297431 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**5) Alessandria**
```proj
+proj=cass +lat_0=44.91472668 +lon_0=8.61134796 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**6) Monte Bignone**
```proj
+proj=cass +lat_0=43.87352936 +lon_0=7.73372694 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**7) Forte Diamante**
```proj
+proj=cass +lat_0=44.46112587 +lon_0=8.93946834 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**8) Portonovo**
```proj
+proj=cass +lat_0=44.53248216 +lon_0=11.75335874 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**9) Siena (Torre del Mangia)**
```proj
+proj=cass +lat_0=43.31828703 +lon_0=11.33221016 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**10) Urbino**
```proj
+proj=cass +lat_0=43.72514932 +lon_0=12.63626776 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**11) Monte Pennino**
```proj
+proj=cass +lat_0=43.10138543 +lon_0=12.88876541 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**12) Monte Mario**
```proj
+proj=cass +lat_0=41.92439627 +lon_0=12.45214521 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**13) Monte Ocre**
```proj
+proj=cass +lat_0=42.25645724 +lon_0=13.44313386 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**14) Monte Pietrereie (Monte Palombo)**
```proj
+proj=cass +lat_0=41.6510226 +lon_0=14.25965522 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**16) Taranto (Cattedrale)**
```proj
+proj=cass +lat_0=40.47618517 +lon_0=17.22847695 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**17) Lecce**
```proj
+proj=cass +lat_0=40.35195558 +lon_0=18.16922358 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**18) Monte Bruto**
```proj
+proj=cass +lat_0=39.14090145 +lon_0=16.42183592 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**19) Torre Titone**
```proj
+proj=cass +lat_0=37.84805703 +lon_0=12.53962245 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**20) Monte Etna (Punta Lucia)**
```proj
+proj=cass +lat_0=37.76465593 +lon_0=14.9852708 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**21) Monte Castelluccio**
```proj
+proj=cass +lat_0=37.41597534 +lon_0=13.77923129 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**22) Mineo**
```proj
+proj=cass +lat_0=37.26699983 +lon_0=14.69242068 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**23) Sardegna (Punto Ideale)**
```proj
+proj=cass +lat_0=40.0003912 +lon_0=9.1169511 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**24) Innsbruck**
```proj
+proj=cass +lat_0=47.26927415 +lon_0=11.39370656 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**27) Monte Cairo**
```proj
+proj=cass +lat_0=41.54152292 +lon_0=13.76055843 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**28) Francolise**
```proj
+proj=cass +lat_0=41.18261872 +lon_0=14.06374347 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**29) Cancello (Castello)**
```proj
+proj=cass +lat_0=40.84019413 +lon_0=14.43144708 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**30) Miradois (Osservatorio Capodimonte)**
```proj
+proj=cass +lat_0=40.86365124 +lon_0=14.25552353 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**31) Monte Petrella**
```proj
+proj=cass +lat_0=41.32219558 +lon_0=13.6655907 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

**32) Marigliano**
```proj
+proj=cass +lat_0=40.92522593 +lon_0=14.45600831 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs
```

---

## 🗺️ Guida all'Uso in QGIS

### A. Creazione del CRS Cassini-Soldner personalizzato

Utilizzare questa procedura per inquadrare o georeferenziare mappe catastali raster (.tif, .png) o importare file vettoriali (.dxf, shapefile, CXF) con coordinate locali catastali:

1. Aprire **QGIS**.
2. Andare sul menu: **Impostazioni** > **Proiezioni personalizzate...** *(Settings > Custom Projections...)*.
3. Nella finestra di dialogo, cliccare sul pulsante verde **`+`** (*Aggiungi nuovo CRS*) in alto a destra.
4. Compilare i parametri:
   - **Nome**: indicare un nome riconoscibile (es. `Catasto Cassini - 14 Monte Pietrereie`).
   - **Formato**: selezionare dal menu a tendina **PROJ String** (o *PROJ*).
   - **Parametri**: copiare con il pulsante dedicato la stringa dell'origine desiderata e incollarla nel campo.
5. Cliccare sul pulsante **Convalida** *(Validate)* per verificare che la sintassi sia valida.
6. Cliccare su **Applica** e infine su **OK**.
7. Il nuovo CRS sarà selezionabile sotto **Sistemi di riferimento definiti dall'utente** e potrà essere assegnato al progetto o al singolo layer catastale.

---

### B. Importazione e visualizzazione del layer dei centri di emanazione

Utilizzare questa procedura per caricare sulla mappa il file `grandi_origini_catasto.csv` presente nel repository:

1. Aprire **QGIS**.
2. Dal menu principale, selezionare: **Layer** > **Aggiungi layer** > **Aggiungi layer testo delimitato...** *(oppure premere `Ctrl + Shift + T`)*.
3. Nel campo **Nome file**, cliccare su **Sfoglia (...)** e selezionare `grandi_origini_catasto.csv`.
4. Configurare le opzioni:
   - **Formato file**: scegliere **Delimitatori personalizzati** e spuntare esclusivamente **Punto e virgola** (`;`).
   - **Opzioni record e campi**: assicurarsi che sia attiva la spunta su *I primi record hanno i nomi dei campi*.
   - **Definizione della geometria**:
     - Selezionare **Coordinate punto**.
     - **Campo X**: selezionare `Longitudine`.
     - **Campo Y**: selezionare `Latitudine`.
     - **SR della geometria**: impostare **EPSG:4326 - WGS 84**.
5. Verificare l'anteprima tabellare e cliccare su **Aggiungi** > **Chiudi**.
6. I 29 centri di emanazione compariranno sulla mappa geografica con tutti gli attributi associati.

---

## ℹ️ Note Geodetiche e Tecniche

1. **Origine degli assi cartesiani**:
   Nelle definizioni PROJ fornite, le traslazioni all'origine sono poste a zero (`+x_0=0 +y_0=0`), rispecchiando la convenzione nativa catastale in cui le coordinate sono conteggiate direttamente a partire dal punto trigonometrico di emanazione.
2. **Ellissoide di riferimento**:
   I parametri usano convenzionalmente l'ellissoide `+ellps=WGS84` per consentire la sovrapposizione immediata su basi cartografiche moderne (OpenStreetMap, ortofoto regionali). Per rilievi millimetrici e trasformazioni storiche con Bessel 1841 nativo, si raccomanda l'uso dei grigliati di correzione IGM (`.gsb` / ConveRgo).

---

## 📄 Licenza e Utilizzo

Dati tecnici derivati da documentazione catastale pubblica. Il repository e le istruzioni sono liberamente utilizzabili per finalità professionali, accademiche e di sviluppo GIS.
