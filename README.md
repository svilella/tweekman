# Tweekman

L?interfaccia consiste in uno script python che, per ora, gira in locale. Per avviarlo � sufficiente, in una finestra di terminale, entrare nella cartella contenente l?interfaccia e digitare `python tweekman.py` .
L?interfaccia � scritta in Python 3 e sfrutta `tkinter`, pacchetto GUI standard per python. L?unico altro modulo necessario �  `pandas`.

Sono presenti tutti i livelli concordati: **emozioni**, secondo il modello di Ekman + love, **ironia/sarcasmo**, **odio/offensivit�**,** contenitore/contenuto**. Il tweet compare nell?area grigia nella parte bassa dell?interfaccia. Per ogni tweet � possibile:

* spuntare il checkbox per ogni emozione che si ritiene sia presente;

* spuntare il checkbox se si ritiene vi sia ironia o sarcasmo. Poich� il sarcasmo � una forma di ironia (vedere punto 3 delle linee guida), qualora venisse annotato il sarcasmo, il tweet sar� annotato anche come ironico: non esiste sarcasmo senza ironia;

* spuntare il check di odio/offensivit� e contenitore/contenuto laddove necessario;

* se si ritiene che il tweet sia illeggibile o indecifrabile per qualsiasi motivo, cliccare su `INCOMPRENSIBILE` nella parte bassa dell?interfaccia.

* Cliccando su `Next `verr� acquisita l'annotazione per il tweet corrente, e verr� mostrato il tweet successivo (nota: anche dopo aver premuto `INCOMPRENSIBILE` sar� necessario cliccare `Next`).

* Cliccando su `Save` il file `tweets.csv` sar� sovrascritto, e le annotazioni salvate.

Possono essere spuntati pi� check per ciascuna annotazione, nessuno � esclusivo, incluso il pulsante `INCOMPRENSIBILE`.

Al primo avvio lo script partir� dal primo tweet. Agli avvii successivi, l'annotazione riprender� dall'ultimo tweet annotato. Ad ogni avvio verr� creata una copia del file csv,`tweets_old.csv`, per sicurezza.
Un file di backup `temp.csv` viene aggiornato ad ogni iterazione, in caso di crash improvviso. 

