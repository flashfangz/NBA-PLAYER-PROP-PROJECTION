data = """
WAS
Washington Wizards
62	23.45	8.36	4.77	2.87	1.98	0.89	2.16	47.09
TOR
Toronto Raptors
62	24.38	7.67	4.24	3.15	1.47	0.99	2.28	45.04
UTH
Utah Jazz
63	22.01	7.06	4.52	2.93	1.83	1.17	1.69	44.57
ATL
Atlanta Hawks
62	23.21	7.44	4.72	3.16	1.39	0.84	2.65	43.26
IND
Indiana Pacers
63	22.95	8.21	3.77	2.13	1.45	0.87	2.46	42.96
MEM
Memphis Grizzlies
63	21.45	8.59	3.73	3.08	1.69	0.90	2.36	42.76
NYK
New York Knicks
62	21.72	7.58	4.47	2.58	1.67	0.85	2.35	42.73
LAL
Los Angeles Lakers
64	21.77	8.08	4.24	2.93	1.56	0.75	2.06	42.70
DET
Detroit Pistons
61	21.97	7.51	4.45	2.71	1.58	0.66	1.82	42.56
GSW
Golden State Warriors
61	21.92	7.87	3.50	2.99	1.72	0.76	2.10	41.95
CHA
Charlotte Hornets
62	22.50	7.32	4.41	2.73	1.32	0.70	2.13	41.83
SAC
Sacramento Kings
61	22.57	7.23	3.91	3.11	1.48	0.67	1.81	41.75
CLE
Cleveland Cavaliers
62	21.83	7.96	4.09	2.45	1.55	0.65	2.62	41.50
BKN
Brooklyn Nets
62	21.79	7.89	4.19	2.81	1.32	0.66	2.00	41.48
SAS
San Antonio Spurs
62	19.41	8.14	4.22	2.56	1.71	0.78	2.17	40.81
MIA
Miami Heat
61	20.79	7.35	4.43	2.73	1.50	0.78	2.40	40.70
PHI
Philadelphia 76ers
62	20.18	8.35	3.67	2.49	1.51	0.86	2.29	40.53
LAC
Los Angeles Clippers
61	21.26	7.27	3.86	2.85	1.54	0.74	2.15	40.46
POR
Portland Trail Blazers
61	20.14	7.28	3.97	2.44	1.68	0.96	2.37	40.38
NOR
New Orleans Pelicans
62	20.45	7.42	4.46	3.06	1.37	0.83	2.47	40.17
MIL
Milwaukee Bucks
63	19.67	7.42	4.25	2.04	1.62	0.66	1.67	40.12
CHI
Chicago Bulls
62	20.83	7.12	4.52	2.81	1.37	0.72	2.37	40.05
MIN
Minnesota Timberwolves
62	20.46	7.52	3.75	2.46	1.62	0.73	2.34	39.82
HOU
Houston Rockets
62	19.12	7.77	3.86	2.39	1.54	0.90	2.13	39.42
BOS
Boston Celtics
61	19.95	7.78	3.69	2.68	1.48	0.59	1.87	39.16
PHO
Phoenix Suns
62	18.87	7.43	3.23	2.51	1.96	0.79	1.75	39.13
DAL
Dallas Mavericks
62	19.01	8.00	4.43	2.35	1.15	0.82	2.10	39.07
ORL
Orlando Magic
63	19.40	6.57	3.59	2.61	1.63	0.59	2.45	36.88
OKC
Oklahoma City Thunder
62	19.03	7.30	3.46	2.69	1.25	0.89	2.55	36.85
DEN
Denver Nuggets
62	18.26	7.16	3.54	2.04	1.37	0.84	2.35	36.44"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed