# Grenzwertanalyse
Tipp: benutzen Sie einen [Tabellengenerator für Markdown](https://www.tablesgenerator.com/markdown_tables)

## Analyse

### 1
| # | erreichte punkte | gesamtpunkte | erwartetes Ergebnis |
|---|------------------|--------------|---------------------|
| 1 | 10               | 100          | 10                  |
| 2 | 2,5              | 100          | 2,5                 |
| 3 | 0                | 100          | 0                   |
| 4 | 100              | 100          | 100                 |
| 5 | -5               | 100          | ValueError          |
| 6 | 1                | -100         | ValueError          |
| 7 | "cool"           | 0            | TypeError           |
| 8 | 10               | "cool"       | TypeError           |
| 9 | 1000             | 100          | ValueError          |

### 2
| #  | prozentwert | erwartetes Ergebnis |
|----|-------------|---------------------|
| 2  | -5          | ValueError          |
| 3  | 110         | ValueError          |
| 4  | "text"      | TypeError           |
| 5  | 0           | "ungenügend"        |
| 6  | 30          | "mangelhaft"        |
| 7  | 43          | "ausreichend"       |
| 8  | 67          | "befriedigend"      |
| 9  | 81          | "gut"               |
| 10 | 92          | "sehr gut"          |
| 11 | 100         | "sehr gut"          |
