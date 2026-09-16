import sqlite3
from qgis.core import QgsApplication, QgsCoordinateReferenceSystem

origini = [
    (1, "Vercelli (Punto Ideale)", "+proj=cass +lat_0=45.45042576 +lon_0=8.20503948 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (2, "Pordenone", "+proj=cass +lat_0=45.95458397 +lon_0=12.66047164 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (3, "Monte Bronzone", "+proj=cass +lat_0=45.70905303 +lon_0=9.99074064 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (4, "Lodi", "+proj=cass +lat_0=45.31413505 +lon_0=9.50297431 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (5, "Alessandria", "+proj=cass +lat_0=44.91472668 +lon_0=8.61134796 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (6, "Monte Bignone", "+proj=cass +lat_0=43.87352936 +lon_0=7.73372694 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (7, "Forte Diamante", "+proj=cass +lat_0=44.46112587 +lon_0=8.93946834 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (8, "Portonovo", "+proj=cass +lat_0=44.53248216 +lon_0=11.75335874 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (9, "Siena (Torre del Mangia)", "+proj=cass +lat_0=43.31828703 +lon_0=11.33221016 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (10, "Urbino", "+proj=cass +lat_0=43.72514932 +lon_0=12.63626776 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (11, "Monte Pennino", "+proj=cass +lat_0=43.10138543 +lon_0=12.88876541 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (12, "Monte Mario", "+proj=cass +lat_0=41.92439627 +lon_0=12.45214521 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (13, "Monte Ocre", "+proj=cass +lat_0=42.25645724 +lon_0=13.44313386 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (14, "Monte Pietrereie (Monte Palombo)", "+proj=cass +lat_0=41.6510226 +lon_0=14.25965522 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (16, "Taranto (Cattedrale)", "+proj=cass +lat_0=40.47618517 +lon_0=17.22847695 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (17, "Lecce", "+proj=cass +lat_0=40.35195558 +lon_0=18.16922358 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (18, "Monte Bruto", "+proj=cass +lat_0=39.14090145 +lon_0=16.42183592 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (19, "Torre Titone", "+proj=cass +lat_0=37.84805703 +lon_0=12.53962245 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (20, "Monte Etna (Punta Lucia)", "+proj=cass +lat_0=37.76465593 +lon_0=14.9852708 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (21, "Monte Castelluccio", "+proj=cass +lat_0=37.41597534 +lon_0=13.77923129 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (22, "Mineo", "+proj=cass +lat_0=37.26699983 +lon_0=14.69242068 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (23, "Sardegna (Punto Ideale)", "+proj=cass +lat_0=40.0003912 +lon_0=9.1169511 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (24, "Innsbruck", "+proj=cass +lat_0=47.26927415 +lon_0=11.39370656 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (27, "Monte Cairo", "+proj=cass +lat_0=41.54152292 +lon_0=13.76055843 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (28, "Francolise", "+proj=cass +lat_0=41.18261872 +lon_0=14.06374347 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (29, "Cancello (Castello)", "+proj=cass +lat_0=40.84019413 +lon_0=14.43144708 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (30, "Miradois (Osservatorio Capodimonte)", "+proj=cass +lat_0=40.86365124 +lon_0=14.25552353 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (31, "Monte Petrella", "+proj=cass +lat_0=41.32219558 +lon_0=13.6655907 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs"),
    (32, "Marigliano", "+proj=cass +lat_0=40.92522593 +lon_0=14.45600831 +x_0=0 +y_0=0 +ellps=WGS84 +units=m +no_defs")
]

db_path = QgsApplication.qgisUserDatabaseFilePath()
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Ricava l'ID progressivo massimo per i CRS definiti dall'utente (> 100000)
cur.execute("SELECT COALESCE(MAX(srs_id), 100000) FROM tbl_srs")
max_id = max(cur.fetchone()[0], 100000)

inseriti = 0
for num, name, proj_str in origini:
    desc = f"Catasto Cassini - {num:02d} {name}"
    
    # Verifica se già presente per evitare duplicazioni
    cur.execute("SELECT srs_id FROM tbl_srs WHERE description = ?", (desc,))
    row = cur.fetchone()
    if row:
        print(f"[GIA PRESENTE] {desc} (ID: USER:{row[0]})")
        continue

    max_id += 1
    cur.execute("""
        INSERT INTO tbl_srs (
            srs_id, description, projection_acronym, ellipsoid_acronym,
            parameters, srid, auth_name, auth_id, is_geo, deprecated
        ) VALUES (?, ?, 'cass', 'WGS84', ?, ?, 'USER', ?, 0, 0)
    """, (max_id, desc, proj_str, max_id, str(max_id)))
    
    inseriti += 1
    print(f"[OK] Inserito: {desc} (ID: USER:{max_id})")

conn.commit()
conn.close()

# Invalida la cache interna del CRS per aggiornare subito QGIS senza errori
QgsCoordinateReferenceSystem.invalidateCache()

print(f"\nOperazione completata: {inseriti} nuovi CRS registrati in QGIS.")