data = """
WAS
Washington Wizards
60	26.95	18.34	4.56	0.67	0.98	2.53	3.09	63.24
POR
Portland Trail Blazers
58	24.23	15.19	4.39	1.10	1.62	3.12	2.88	60.38
DET
Detroit Pistons
59	23.19	15.18	4.73	0.75	1.59	3.21	2.97	59.93
CHA
Charlotte Hornets
60	25.50	16.89	3.85	0.98	1.22	2.30	3.06	59.04
SAS
San Antonio Spurs
60	26.10	15.73	3.69	0.91	1.26	2.17	2.45	58.35
MEM
Memphis Grizzlies
60	22.71	15.23	3.95	0.94	1.35	3.28	3.14	57.66
ATL
Atlanta Hawks
59	22.90	15.36	3.97	0.82	1.60	2.48	2.76	56.77
GSW
Golden State Warriors
59	23.66	14.58	5.26	0.93	1.29	2.16	2.82	56.58
TOR
Toronto Raptors
60	23.01	15.16	4.31	0.88	1.16	2.59	2.49	56.43
OKC
Oklahoma City Thunder
59	22.89	16.12	4.85	0.88	1.12	2.23	3.19	56.37
UTH
Utah Jazz
60	24.88	13.94	3.99	0.85	1.21	2.50	2.70	56.02
DAL
Dallas Mavericks
60	24.81	15.20	4.22	1.42	1.44	1.70	2.85	55.95
NOR
New Orleans Pelicans
61	22.63	14.82	4.61	1.00	1.21	2.41	2.97	55.22
LAL
Los Angeles Lakers
61	21.22	15.30	4.51	1.16	1.62	2.16	2.94	54.75
DEN
Denver Nuggets
60	23.59	14.19	4.59	0.98	1.42	1.82	2.78	54.44
HOU
Houston Rockets
59	22.87	14.30	4.12	1.18	1.27	2.57	3.34	54.39
BKN
Brooklyn Nets
59	22.10	14.35	4.13	1.00	1.28	2.32	2.14	54.18
MIL
Milwaukee Bucks
61	22.97	14.64	4.81	1.23	1.21	1.69	2.50	53.95
PHI
Philadelphia 76ers
59	24.25	13.78	3.86	1.00	1.00	2.32	2.69	53.85
IND
Indiana Pacers
61	22.34	14.13	4.80	0.65	1.17	2.34	3.20	53.83
CHI
Chicago Bulls
60	21.87	13.93	4.46	1.20	1.22	2.10	2.21	53.03
SAC
Sacramento Kings
59	20.33	14.46	4.63	0.62	1.36	2.02	2.25	52.52
CLE
Cleveland Cavaliers
59	20.89	15.15	3.62	0.93	1.22	2.43	2.95	52.50
LAC
Los Angeles Clippers
58	20.78	14.36	4.60	0.98	1.58	1.70	2.58	52.17
ORL
Orlando Magic
60	21.05	13.95	3.69	0.59	1.58	2.18	3.01	51.60
MIN
Minnesota Timberwolves
60	21.24	12.93	4.26	1.13	1.37	2.03	2.51	50.84
PHO
Phoenix Suns
59	21.40	13.23	4.73	0.77	1.29	1.77	2.85	50.70
BOS
Boston Celtics
59	22.73	13.32	4.16	1.15	1.09	1.58	2.58	50.38
MIA
Miami Heat
59	19.72	14.61	3.17	0.99	1.17	1.95	2.21	49.16
NYK
New York Knicks
60	19.90	13.23	3.22	1.15	1.24	2.18	2.48	48.39"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed

