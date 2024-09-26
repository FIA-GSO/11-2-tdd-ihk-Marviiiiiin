# Grenzwertanalyse
Tipp: benutzen Sie einen [Tabellengenerator für Markdown](https://www.tablesgenerator.com/markdown_tables)

## Analyse

### 1
| # | erreichte punkte | gesamtpunkte | erwartetes Ergebnis |
|---|------------------|--------------|---------------------|
| 1 | 100              | 100          | 100                 |
| 2 | 50               | 100          | 50                  |
| 3 | 0                | 100          | 0                   |
| 4 | -1               | 100          | ValueError          |
| 5 | 0                | 5            | ValueError          |
| 6 | "test"           | 0            | TypeError           |
| 7 | 100              | "test"       | TypeError           |
| 8 | 101              | 100          | ValueError          |

### 2
| #  | prozentwert | erwartetes Ergebnis |
|----|-------------|---------------------|
| 1  | -1          | ValueError          |
| 2  | 101         | ValueError          |
| 3  | "text"      | TypeError           |
| 4  | 0           | "ungenügend"        |
| 5  | 29          | "ungenügend"        |
| 6  | 30          | "mangelhaft"        |
| 7  | 42          | "mangelhaft"        |
| 8  | 43          | "ausreichend"       |
| 9  | 66          | "ausreichend"       |
| 10 | 67          | "befriedigend"      |
| 11 | 80          | "befriedigend"      |
| 12 | 81          | "gut"               |
| 13 | 91          | "gut"               |
| 14 | 92          | "sehr gut"          |
| 15 | 100         | "sehr gut"          |
