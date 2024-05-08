data = """
DET
Detroit Pistons
62	26.91	6.20	9.03	2.81	2.12	0.59	3.06	52.97
SAS
San Antonio Spurs
63	26.92	6.39	9.17	3.14	2.02	0.51	3.39	52.54
WAS
Washington Wizards
62	25.30	6.64	9.77	3.02	1.81	0.69	2.99	52.43
UTH
Utah Jazz
63	23.40	6.43	10.54	3.08	1.97	0.77	3.20	51.95
POR
Portland Trail Blazers
61	25.17	6.22	8.96	2.63	1.97	0.76	3.32	50.94
LAL
Los Angeles Lakers
64	25.56	6.26	9.05	3.37	1.97	0.34	2.85	50.73
PHO
Phoenix Suns
63	25.67	5.74	8.92	3.43	2.06	0.57	3.15	50.68
MIL
Milwaukee Bucks
63	25.97	6.23	8.54	2.84	1.76	0.52	2.98	50.12
GSW
Golden State Warriors
62	24.80	6.08	8.55	3.00	1.87	0.67	2.50	50.04
ORL
Orlando Magic
63	26.24	5.40	7.98	2.98	2.21	0.52	3.11	49.77
MEM
Memphis Grizzlies
63	24.13	7.17	8.48	3.17	1.84	0.63	3.34	49.52
BKN
Brooklyn Nets
63	25.87	6.21	8.22	3.65	1.55	0.56	2.87	49.11
SAC
Sacramento Kings
62	23.90	6.47	9.14	2.81	1.81	0.55	3.36	49.09
CHA
Charlotte Hornets
62	24.23	6.65	9.28	3.31	1.39	0.61	3.07	49.06
ATL
Atlanta Hawks
62	24.14	6.20	9.13	3.26	1.68	0.63	3.18	49.03
DAL
Dallas Mavericks
63	23.82	6.66	9.06	2.73	1.65	0.53	3.07	48.87
TOR
Toronto Raptors
63	22.18	6.37	10.08	2.66	1.66	0.58	3.14	48.52
PHI
Philadelphia 76ers
62	23.69	6.10	8.84	2.68	1.70	0.88	3.51	48.50
HOU
Houston Rockets
62	25.27	6.18	7.54	3.04	1.56	0.81	2.82	48.29
OKC
Oklahoma City Thunder
62	23.88	6.37	8.47	3.47	1.69	0.63	3.32	47.87
BOS
Boston Celtics
62	24.42	6.39	8.14	3.21	1.57	0.49	2.78	47.70
CLE
Cleveland Cavaliers
62	24.31	5.67	7.57	2.96	2.18	0.51	3.15	47.39
DEN
Denver Nuggets
63	24.22	5.94	8.44	2.87	1.63	0.41	2.77	47.36
IND
Indiana Pacers
64	24.84	6.22	7.47	2.63	1.47	0.72	3.09	46.99
MIN
Minnesota Timberwolves
63	22.71	5.68	8.42	2.38	1.96	0.66	3.33	46.69
NOR
New Orleans Pelicans
62	24.34	5.18	9.14	3.33	1.50	0.42	3.34	46.69
MIA
Miami Heat
62	23.06	5.73	8.73	3.10	1.52	0.65	3.18	46.36
NYK
New York Knicks
62	22.34	5.96	8.47	2.55	1.62	0.61	2.76	46.13
LAC
Los Angeles Clippers
61	25.16	5.51	8.23	3.08	1.23	0.45	3.25	45.91
CHI
Chicago Bulls
63	21.55	5.37	8.95	3.02	1.22	0.58	3.33	43.49
"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed