# PicoUSB - BadUSB basato su RP2040

Repository per PicoUSB - Dispositivo BadUSB basato su RP2040, economico, facile da usare e da programmare.

## Indice

- [Setup Iniziale](#setup-iniziale)
- [Modalità di Funzionamento](#modalità-di-funzionamento)
- [File Importanti](#file-importanti)
- [API Comandi](#api-comandi)
- [Layout Tastiera Supportati](#layout-tastiera-supportati)
- [Esempi](#esempi)
- [Sviluppo](#sviluppo)
- [Risoluzione Problemi](#risoluzione-problemi)

## Setup Iniziale

Hai appena ricevuto un PicoUSB vuoto? Ecco come programmarlo:

### 1. Installa CircuitPython

1. Scarica l'ultima versione di [CircuitPython per Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)
2. Inserisci il PicoUSB nel tuo PC tenendo premuto il pulsante **"Boot"** (oppure collega GPIO 0 a GND)
3. Il dispositivo apparirà come un'unità USB chiamata "RPI-RP2"
4. Copia il file `CircuitPython.uf2` nell'unità USB
5. Attendi qualche secondo o un minuto che il setup si completi (l'explorer si chiuderà e riaprirà automaticamente)

### 2. Carica i File

1. Scarica o clona i contenuti di questa repository
2. Apri il dispositivo USB nell'explorer (ora si chiamerà "CIRCUITPY")
3. Copia/incolla **tutto** dalla cartella `./src/` nel dispositivo USB (Sostituisci tutto)

✅ Fatto! Il tuo PicoUSB è pronto all'uso.

## Modalità di Funzionamento

Questa versione usa un sistema di **selezione modalità tramite bridge GPIO 3** (invece dei pulsanti fisici).

### ⚡ Modalità BadUSB (Esecuzione Payload)

**Per eseguire l'attacco BadUSB:**

1. **Disconnetti qualsiasi jumper wire** dal GPIO 3
2. Inserisci il dispositivo nel computer target
3. Il payload in `pico_usb.txt` verrà eseguito automaticamente
4. La memoria USB è disabilitata (modalità stealth)

### 🔧 Modalità Boot/Safe (Modifica File)

**Per modificare i file in sicurezza:**

1. **Collega GPIO 3 a un pin GND** usando un jumper wire
2. Inserisci il dispositivo nel tuo computer
3. Il dispositivo apparirà come unità USB "PicoUSB"
4. Puoi modificare liberamente:
   - `pico_usb.txt` (il tuo payload)
   - `layout.txt` (layout tastiera)
   - Qualsiasi altro file
5. Rimuovi il jumper wire prima di deployare il dispositivo

### 📍 Posizione dei Pin GPIO

Sulla maggior parte delle schede RP2040 mini USB:
- **GPIO 3** è solitamente etichettato come "GP3" o "3"
- I pin **GND** sono etichettati come "GND" o "-"
- Usa qualsiasi pin GND disponibile (ce ne sono tipicamente multipli)

## File Importanti

⚠️ **ATTENZIONE**

Modificare i file Python può risultare nel danneggiamento permanente del dispositivo. Fai molta attenzione quando modifichi `boot.py`, poiché disabilitare l'unità USB senza un failsafe potrebbe rendere il dispositivo inutilizzabile! Gli sviluppatori non sono responsabili se bricchi il tuo dispositivo in questo modo!

### File Principali

| File | Descrizione |
|------|-------------|
| **pico_usb.txt** | Il tuo codice payload eseguibile (pseudo-codice) |
| **layout.txt** | Selezione del layout tastiera |
| **code.py** | Interprete che esegue il tuo pseudo-codice (modificabile) |
| **boot.py** | Eseguito prima che l'USB venga riconosciuto (modificabile) |
| **example.txt** | Esempio di payload |

## API Comandi

Scrivi i tuoi comandi nel file `pico_usb.txt` usando i seguenti comandi:

### Comandi Tastiera

| Comando | Descrizione | Esempio |
|---------|-------------|---------|
| `delay(secondi)` | Attende per il numero specificato di secondi | `delay(0.8)` |
| `press(tasti)` | Preme uno o più tasti contemporaneamente | `press(enter)` o `press(control + a)` |
| `write(testo)` | Scrive il testo specificato | `write(Hello world!)` |
| `hold(tasti)` | Tiene premuti uno o più tasti fino a `release()` | `hold(shift)` |
| `release()` | Rilascia tutti i tasti tenuti premuti | `release()` |

### Comandi Mouse

| Comando | Descrizione | Esempio |
|---------|-------------|---------|
| `move(x, y)` | Muove il mouse dalla posizione corrente | `move(100, -50)` |
| `click(btn)` | Clicca il mouse (left, right, middle) | `click(left)` |
| `scroll(x)` | Scrolla il mouse (negativo=giù, positivo=su) | `scroll(-5)` |

> **Nota:** Per `move()`: x negativo=sinistra, x positivo=destra, y negativo=giù, y positivo=su

### Comandi Sistema

| Comando | Descrizione | Esempio |
|---------|-------------|---------|
| `volume(x)` | Modifica il volume (range 0-100) | `volume(50)` o `volume(-20)` |
| `volume(mute)` | Silenzia gli altoparlanti | `volume(mute)` |
| `loop()` | Loop infinito di tutto **dopo** questo comando | `loop()` |

> ⚠️ **Importante:** Usa `loop()` una sola volta. Tutto ciò che viene **dopo** `loop()` verrà ripetuto all'infinito.

## Layout Tastiera Supportati

Modifica il layout nel file `layout.txt`. Layout supportati:

| Codice | Paese/Regione |
|--------|---------------|
| `US` | Stati Uniti |
| `UK` | Regno Unito |
| `IT` | Italia |
| `DE` | Germania |
| `FR` | Francia |
| `ES` | Spagna |
| `CZ` | Repubblica Ceca |
| `BR` | Brasile |
| `CRO` | Croazia/Slovenia/Bosnia |
| `HU` | Ungheria |
| `PO` | Polonia |
| `SW` | Svezia |
| `TR` | Turchia |
| `BE` | Belgio |
| `SG` | Svizzera Tedesca |

**Esempio `layout.txt`:**
```
layout(IT)
```

⚠️ **NON DIMENTICARE** di cambiare il layout della tastiera in base al paese target!

## Esempi

### Esempio 1: Apri Notepad e scrivi un messaggio

```
delay(1)
press(windows + r)
delay(1)
write(notepad)
press(enter)
delay(2)
write(Hello from PicoUSB!)
```

### Esempio 2: Loop con mouse (dal file pico_usb.txt incluso)

```
delay(1)
press(windows + d)
delay(1)
press(windows + r)
delay(2)
write(notepad)
press(enter)
delay(2)
write(Hello from PicoUSB!)
delay(1)
loop()
write(!)
move(5, 5)
delay(0.5)
```

### Esempio 3: Apri un URL nel browser (da example.txt)

```
delay(3)
press(windows + d)
delay(2)
press(windows + e)
delay(2)
press(control + l)
delay(2)
write(https://www.youtube.com/)
delay(2)
press(enter)
delay(2)
press(windows + d)
volume(100)
```

## Sviluppo

Se vuoi modificare il codice Python:

1. Crea un ambiente virtuale: `python -m venv .venv`
2. Attiva l'ambiente virtuale:
   - Windows: `.venv\Scripts\Activate.ps1`
   - Unix/Linux: `source .venv/bin/activate`
3. Installa le dipendenze: `pip install -r requirements-dev.txt` (se disponibile)

## Risoluzione Problemi

### Il dispositivo non entra in modalità boot

- Controlla che GPIO 3 sia correttamente collegato a GND
- Prova a usare un pin GND diverso
- Assicurati che il jumper wire sia ben inserito

### Il payload non viene eseguito

- Assicurati che GPIO 3 sia completamente disconnesso (non tocca GND)
- Verifica che `pico_usb.txt` non contenga errori di sintassi
- Aumenta i valori di `delay()` se il computer target è lento

### Dispositivo "bricked" (non risponde)

Se hai accidentalmente disabilitato l'USB drive senza failsafe, puoi provare a entrare in safe mode:

1. Collega GPIO 3 a GND
2. Inserisci il dispositivo
3. Oppure usa il REPL seriale e esegui:
   ```python
   import microcontroller
   microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
   microcontroller.reset()
   ```

### Il layout tastiera è sbagliato

- Verifica che `layout.txt` contenga il codice corretto per il tuo paese
- Ricorda: il layout deve corrispondere alla tastiera del **computer target**, non del tuo computer!

## Vantaggi di Questo Metodo

✅ **Semplice**: Serve solo un jumper wire  
✅ **Affidabile**: Nessun problema di timing con combinazioni di pulsanti  
✅ **Sicuro**: Chiara distinzione tra modalità operativa e configurazione  
✅ **Flessibile**: Facile cambiare modalità durante lo sviluppo

## Licenza

Copyright 2024 PicoUSB - Licensed under the Apache License, Version 2.0

## Disclaimer

⚠️ **IMPORTANTE**: Questo strumento è solo per scopi educativi e test di sicurezza autorizzati. L'uso non autorizzato di dispositivi BadUSB su sistemi che non possiedi o per cui non hai il permesso esplicito è illegale. Gli sviluppatori non sono responsabili per qualsiasi uso improprio di questo software.

## Crediti

- Layout tastiera generati usando [Circuitpython_Keyboard_Layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts)
- Basato sul progetto originale PicoUSB
