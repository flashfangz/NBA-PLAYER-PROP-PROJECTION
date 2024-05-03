data = """
UTH
Utah Jazz
63	27.01	9.44	4.82	3.14	1.73	1.45	2.20	52.91
IND
Indiana Pacers
64	26.89	10.89	4.45	1.80	1.27	1.38	2.67	51.91
WAS
Washington Wizards
62	26.23	10.82	5.02	2.13	1.30	1.18	2.63	51.55
CHA
Charlotte Hornets
62	25.40	10.98	5.03	2.45	1.39	1.12	2.89	50.76
DAL
Dallas Mavericks
63	25.74	10.80	4.76	2.31	1.50	0.96	2.81	50.41
ATL
Atlanta Hawks
62	24.98	10.50	4.67	2.72	1.45	1.22	2.28	50.32
DET
Detroit Pistons
62	25.29	9.97	4.31	2.40	1.45	1.16	2.29	49.26
SAC
Sacramento Kings
62	26.13	10.12	4.80	2.46	1.41	0.89	3.19	49.18
HOU
Houston Rockets
62	23.77	10.64	4.21	2.16	1.38	1.57	2.78	48.92
GSW
Golden State Warriors
62	23.82	10.79	4.69	2.36	1.52	1.02	2.54	48.88
TOR
Toronto Raptors
63	24.10	10.41	4.45	2.59	1.28	1.25	2.40	48.46
CHI
Chicago Bulls
63	24.01	11.13	3.93	2.66	1.29	1.32	2.69	48.40
SAS
San Antonio Spurs
63	23.28	10.56	4.66	2.42	1.37	1.01	2.67	47.41
PHO
Phoenix Suns
63	24.70	9.59	3.55	2.32	1.71	1.05	2.55	47.26
PHI
Philadelphia 76ers
62	22.75	11.57	4.31	2.21	0.91	1.37	2.80	47.14
OKC
Oklahoma City Thunder
62	23.64	10.77	4.28	2.20	1.34	1.01	2.99	47.04
MIL
Milwaukee Bucks
63	24.10	10.16	3.75	2.81	1.26	1.25	2.54	46.91
POR
Portland Trail Blazers
61	23.20	9.77	4.48	2.05	1.49	1.25	2.99	46.87
LAL
Los Angeles Lakers
64	24.19	9.62	4.44	2.74	1.28	1.04	2.52	46.83
MEM
Memphis Grizzlies
63	23.47	10.50	4.00	2.52	1.48	1.15	3.13	46.83
DEN
Denver Nuggets
63	23.06	10.22	4.01	2.08	1.27	1.13	1.96	46.58
NOR
New Orleans Pelicans
62	22.99	10.71	3.93	2.29	1.05	1.32	2.53	46.32
LAC
Los Angeles Clippers
61	21.80	10.46	4.53	2.09	1.30	1.19	2.56	46.06
MIA
Miami Heat
62	22.96	9.77	4.58	2.35	1.30	1.02	2.84	45.67
CLE
Cleveland Cavaliers
62	22.33	10.15	3.99	2.24	1.31	1.10	2.45	45.28
BKN
Brooklyn Nets
63	22.31	10.58	4.30	2.16	1.11	0.95	2.57	45.07
NYK
New York Knicks
62	23.92	8.94	4.45	2.88	1.20	0.97	2.81	45.02
ORL
Orlando Magic
63	20.96	9.63	3.79	1.90	1.25	1.03	2.88	42.16
MIN
Minnesota Timberwolves
63	21.34	9.30	3.20	2.14	1.27	1.11	2.39	42.05
BOS
Boston Celtics
62	19.66	9.85	3.99	2.22	1.03	0.83	1.99	41.06
"""
team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed