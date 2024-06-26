# Алгоритм Крускала

## Як запустити скрипт?

```
python3 main.py
```

## Результати виконання алгоритму Крускала

Для графів із щільністю від 0.5 до 1.0 і кількістю вершин від 20 до 200. Записані середні значення для 20 різних випадкових графів із однаковими вхідними аргументами для матриці суміжності і списків суміжності


| Density | Vertices | Avg Time from matrix (ms) | Avg Time from list (ms) | Avg Edges |
| ------- | -------- | ------------------------- | ----------------------- | --------- |
| 0.5     | 20       | 0.3025                    | 0.40225999999999995     | 60.4      |
| 0.5     | 40       | 0.73824                   | 1.8143                  | 130.2     |
| 0.5     | 60       | 3.1780999999999997        | 4.92332                 | 203.0     |
| 0.5     | 80       | 7.28116                   | 10.350920000000002      | 280.0     |
| 0.5     | 100      | 11.87414                  | 18.738040000000005      | 361.0     |
| 0.5     | 120      | 20.067479999999996        | 32.42284                | 439.4     |
| 0.5     | 140      | 31.11416                  | 51.84818                | 518.8     |
| 0.5     | 160      | 46.36563999999999         | 77.87956                | 598.2     |
| 0.5     | 180      | 60.015280000000004        | 107.53343999999997      | 678.8     |
| 0.5     | 200      | 78.48859999999999         | 141.84256               | 757.8     |
| 0.6     | 20       | 0.59724                   | 0.97432                 | 60.2      |
| 0.6     | 40       | 1.8086000000000002        | 2.48772                 | 130.0     |
| 0.6     | 60       | 2.6268000000000002        | 5.591319999999999       | 204.6     |
| 0.6     | 80       | 7.182200000000002         | 12.93758                | 285.2     |
| 0.6     | 100      | 12.82912                  | 22.25416                | 365.6     |
| 0.6     | 120      | 21.787020000000002        | 37.934599999999996      | 444.0     |
| 0.6     | 140      | 34.69994000000001         | 63.52302000000001       | 525.8     |
| 0.6     | 160      | 53.1217                   | 96.64168000000001       | 607.2     |
| 0.6     | 180      | 94.8996                   | 172.63009999999997      | 686.8     |
| 0.6     | 200      | 131.65906                 | 234.26727999999997      | 769.4     |
| 0.7     | 20       | 0.20148000000000002       | 0.40226000000000006     | 61.0      |
| 0.7     | 40       | 1.7642399999999998        | 3.4198999999999997      | 134.0     |
| 0.7     | 60       | 5.767559999999999         | 8.92634                 | 210.6     |
| 0.7     | 80       | 12.77554                  | 20.63434                | 291.4     |
| 0.7     | 100      | 22.51184                  | 39.64824                | 370.2     |
| 0.7     | 120      | 36.787839999999996        | 65.87458000000001       | 448.2     |
| 0.7     | 140      | 60.52208                  | 111.65802               | 529.4     |
| 0.7     | 160      | 82.37339999999999         | 148.32652               | 610.2     |
| 0.7     | 180      | 105.44270000000002        | 195.1741                | 689.0     |
| 0.7     | 200      | 148.72571999999997        | 275.02626               | 771.4     |
| 0.8     | 20       | 0.85518                   | 1.233308                | 61.4      |
| 0.8     | 40       | 1.7977800000000002        | 3.9940799999999994      | 136.6     |
| 0.8     | 60       | 5.64082                   | 11.85886                | 212.4     |
| 0.8     | 80       | 14.069480000000002        | 23.604580000000002      | 294.0     |
| 0.8     | 100      | 27.42396                  | 45.79541999999999       | 373.6     |
| 0.8     | 120      | 43.92086                  | 81.21485999999999       | 454.2     |
| 0.8     | 140      | 94.45439999999999         | 181.45113999999995      | 534.6     |
| 0.8     | 160      | 108.87708                 | 201.91378               | 614.2     |
| 0.8     | 180      | 143.04073999999997        | 275.38823999999994      | 695.8     |
| 0.8     | 200      | 163.59958                 | 303.84075999999993      | 773.0     |
| 0.9     | 20       | 0.39586                   | 0.61476                 | 63.4      |
| 0.9     | 40       | 2.21432                   | 4.34868                 | 135.2     |
| 0.9     | 60       | 6.405000000000001         | 12.108279999999999      | 217.4     |
| 0.9     | 80       | 15.20408                  | 25.486320000000003      | 297.4     |
| 0.9     | 100      | 25.16832                  | 45.73706000000001       | 377.4     |
| 0.9     | 120      | 43.480080000000015        | 77.93460000000002       | 456.2     |
| 0.9     | 140      | 65.17365999999998         | 120.85843999999997      | 537.0     |
| 0.9     | 160      | 101.36902                 | 188.44131999999993      | 619.4     |
| 0.9     | 180      | 133.06748                 | 252.36410000000006      | 696.0     |
| 0.9     | 200      | 178.32943999999998        | 336.54689999999994      | 777.6     |
| 1.0     | 20       | 0.79186                   | 0.50416                 | 62.6      |
| 1.0     | 40       | 4.04932                   | 4.461039999999999       | 139.6     |
| 1.0     | 60       | 8.05628                   | 14.025379999999998      | 217.4     |
| 1.0     | 80       | 18.47144                  | 29.93512                | 296.4     |
| 1.0     | 100      | 29.78036000000001         | 53.55744                | 379.0     |
| 1.0     | 120      | 49.94492                  | 94.52306                | 457.8     |
| 1.0     | 140      | 83.81807999999998         | 151.42752               | 538.4     |
| 1.0     | 160      | 130.72163999999998        | 235.95292000000003      | 619.6     |
| 1.0     | 180      | 163.31209999999996        | 306.0706200000001       | 697.6     |
| 1.0     | 200      | 224.69099999999997        | 424.48992               | 779.2     |
