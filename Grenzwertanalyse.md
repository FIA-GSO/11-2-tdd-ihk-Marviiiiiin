# Grenzwertanalyse
Tipp: benutzen Sie einen [Tabellengenerator für Markdown](https://www.tablesgenerator.com/markdown_tables)

## Analyse

### 1
| # | erreichte punkte | gesamtpunkte | erwartetes Ergebnis |
|---|------------------|--------------|---------------------|
| 1 | 10               | 100          | 10%                 |
| 2 | 2,5              | 100          | 2,5%                |
| 3 | 0                | 100          | 0%                  |
| 4 | -5               | 100          | ValueError          |
| 5 | 1                | -100         | ValueError          |
| 6 | "cool"           | 0            | TypeError           |
| 7 | 10               | "cool"       | TypeError           |
| 8 | 1000             | 100          | ValueError          |

### 2
| # | prozentwert | erwartetes Ergebnis |
|---|-------------|---------------------|
| 1 | 81          | "gut"               |
| 2 | -5          | ValueError          |
| 3 | 110         | ValueError          |
| 4 | "text"      | TypeError           |
