# Tweekman

L'interfaccia consiste in uno script python che, per ora, gira in locale. Per avviarlo è sufficiente, in una finestra di terminale, entrare nella cartella contenente l?interfaccia e digitare `python tweekman.py` .
L'interfaccia è scritta in Python 3 e sfrutta `tkinter`, pacchetto GUI standard per python. L'unico altro modulo necessario è  `pandas`.

Sono presenti tutti i livelli concordati: **emozioni**, secondo il modello di Plutchik + love (il nome tweekman è rimasto da una precedente annotazione secondo Ekman. Magari lo cambio in Plutchtweet :) ), **ironia/sarcasmo**, **odio/offensività**, **contenitore/contenuto**. Il tweet compare nell'area grigia nella parte bassa dell'interfaccia. Per ogni tweet è possibile:

* spuntare il checkbox per ogni emozione che si ritiene sia presente;

* spuntare il checkbox se si ritiene vi sia ironia o sarcasmo. Poiché il sarcasmo è una forma di ironia (vedere punto 3 delle linee guida), qualora venisse annotato il sarcasmo, il tweet sarà annotato anche come ironico: non esiste sarcasmo senza ironia;

* spuntare il check di odio/offensività e contenitore/contenuto laddove necessario;

* se si ritiene che il tweet sia illeggibile o indecifrabile per qualsiasi motivo, cliccare su `INCOMPRENSIBILE` nella parte bassa dell'interfaccia.

* Cliccando su `Next ` verrà acquisita l'annotazione per il tweet corrente, e verrà mostrato il tweet successivo (nota: anche dopo aver premuto `INCOMPRENSIBILE` sarà necessario cliccare `Next`).

* Cliccando su `Save` il file `tweets.csv` sarà sovrascritto, e le annotazioni salvate.

Possono essere spuntati più check per ciascuna annotazione, nessuno è esclusivo, incluso il pulsante `INCOMPRENSIBILE`.

Al primo avvio lo script partirà dal primo tweet. Agli avvii successivi, l'annotazione riprenderà dall'ultimo tweet annotato. Ad ogni avvio verrà creata una copia del file csv, `tweets_old.csv`, per sicurezza.
Un file di backup `temp.csv` viene aggiornato ad ogni iterazione, in caso di crash improvviso. 

