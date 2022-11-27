# SAVE_Client_Socket_Dice

Angaben fu ̈r das 4. Projekt
1. Schreiben Sie einen socket-client, der sich mit dem “wuerfel server” verbin- det (localhost, port 56701) und eine Serie von Wu ̈rfen (throw) anfordert:
Die Syntax ist:
throw zahl1 zahl2
zahl1: Anzahl der Wu ̈rfe
zahl2: Kennzahl fu ̈r die Zinkung des Wu ̈rfels
mit der Anfrage “help” erhalten Sie die mo ̈glichen Kennzahlen
Die Zahlen von 1-6 erhalten Sie in einer Kette ohne Trennzeichen.
2. Leiten Sie die daurch erhaltenen Daten an ein Statistkprogramm weiter, das die entsprechenden Analysen durchfu ̈hrt.
a) Entropie
b) Binomialverteilung (Mittelwert und Standardabweichung)
c) Test auf Reihenfolge, . . .
Versuchen Sie die Zinkung fu ̈r die entsprechende Kennzahl herauszufinden. Welches ist der wahrscheinlich ungezinkte Wu ̈rfel?
Mo ̈glicher Test auf 2er-runs beim Wu ̈rfel:
1. Za ̈hlen aller auftretenden Paare: 11 12 13 14 15 16
21 ... ...
61 ... 66
Ablegen der counts in einer 6x6 Matrix: Aij: Anzahl der gefundenen ij- Paare
2. Analyse der Matrix: Bestimmen der Ha ̈ufigkeit/Wahrscheinlichkeit des je- weiligen Paares. Vergleich mit der erwarteten Ha ̈ufigkeit