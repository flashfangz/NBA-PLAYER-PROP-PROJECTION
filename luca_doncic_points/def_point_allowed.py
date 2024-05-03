data = """
SAS
San Antonio Spurs
64	27.02	6.36	9.17	3.13	2.06	0.50	3.32	52.77
DET
Detroit Pistons
63	26.99	6.13	9.06	2.85	2.07	0.58	3.08	52.81
MIL
Milwaukee Bucks
65	26.22	6.24	8.66	2.94	1.72	0.52	3.00	50.42
ORL
Orlando Magic
65	26.16	5.49	7.99	2.97	2.21	0.53	3.17	49.78
BKN
Brooklyn Nets
65	25.93	6.12	8.22	3.69	1.53	0.54	2.98	48.83
PHO
Phoenix Suns
64	25.54	5.80	9.04	3.41	2.04	0.58	3.14	50.78
LAL
Los Angeles Lakers
66	25.46	6.24	9.05	3.39	1.92	0.33	2.80	50.47
HOU
Houston Rockets
64	25.28	6.25	7.43	3.08	1.57	0.82	2.85	48.25
LAC
Los Angeles Clippers
63	25.25	5.57	8.22	3.14	1.22	0.45	3.25	46.02
WAS
Washington Wizards
64	25.21	6.65	9.63	2.96	1.79	0.67	2.99	52.03
POR
Portland Trail Blazers
63	25.18	6.13	8.95	2.66	1.96	0.73	3.34	50.69
GSW
Golden State Warriors
63	24.70	6.07	8.58	3.00	1.90	0.65	2.47	50.03
MEM
Memphis Grizzlies
65	24.51	7.15	8.47	3.25	1.83	0.62	3.31	49.84
IND
Indiana Pacers
65	24.49	6.22	7.41	2.59	1.47	0.70	3.04	46.54
BOS
Boston Celtics
63	24.46	6.35	8.13	3.18	1.60	0.49	2.81	47.74
DAL
Dallas Mavericks
64	24.23	6.76	9.15	2.81	1.63	0.51	3.12	49.37
DEN
Denver Nuggets
64	24.17	5.92	8.35	2.89	1.59	0.40	2.77	47.00
NOR
New Orleans Pelicans
64	24.13	5.07	9.14	3.30	1.49	0.40	3.35	46.24
CLE
Cleveland Cavaliers
64	24.11	5.64	7.62	2.93	2.16	0.49	3.14	47.12
ATL
Atlanta Hawks
64	24.07	6.16	9.05	3.29	1.66	0.63	3.16	48.75
CHA
Charlotte Hornets
64	24.05	6.69	9.23	3.30	1.38	0.61	3.06	48.83
OKC
Oklahoma City Thunder
64	23.80	6.36	8.38	3.48	1.68	0.61	3.31	47.56
SAC
Sacramento Kings
63	23.76	6.48	9.27	2.78	1.80	0.54	3.39	49.07
UTH
Utah Jazz
64	23.70	6.39	10.53	3.15	1.97	0.75	3.18	52.14
MIA
Miami Heat
64	23.55	5.85	8.94	3.17	1.50	0.66	3.15	47.31
PHI
Philadelphia 76ers
64	23.44	6.12	8.69	2.65	1.71	0.87	3.51	48.05
MIN
Minnesota Timberwolves
65	22.81	5.60	8.47	2.36	1.92	0.63	3.43	46.46
TOR
Toronto Raptors
64	22.19	6.29	10.08	2.65	1.65	0.58	3.15	48.40
NYK
New York Knicks
64	22.00	5.86	8.40	2.51	1.59	0.64	2.76	45.56
CHI
Chicago Bulls
64	21.61	5.51	8.91	3.08	1.24	0.56	3.30	43.69
"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed
