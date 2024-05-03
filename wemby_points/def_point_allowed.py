data = """
WAS
Washington Wizards
64	26.54	18.44	4.38	0.67	1.01	2.54	3.11	62.78
SAS
San Antonio Spurs
64	26.49	15.92	3.73	0.97	1.32	2.15	2.49	59.11
UTH
Utah Jazz
64	25.08	13.95	4.07	0.82	1.19	2.39	2.66	56.01
CHA
Charlotte Hornets
64	25.02	16.53	3.95	1.02	1.20	2.30	3.02	58.26
DAL
Dallas Mavericks
64	24.75	15.12	4.29	1.37	1.42	1.64	2.77	55.74
POR
Portland Trail Blazers
63	24.39	15.12	4.47	1.20	1.61	3.08	2.89	60.42
PHI
Philadelphia 76ers
64	24.01	13.88	3.80	0.98	1.00	2.42	2.68	53.95
GSW
Golden State Warriors
63	23.62	14.44	5.17	0.99	1.28	2.09	2.80	56.01
DEN
Denver Nuggets
64	23.25	14.29	4.48	0.96	1.39	1.87	2.70	54.20
DET
Detroit Pistons
63	23.22	15.00	4.66	0.74	1.58	3.22	2.93	59.68
TOR
Toronto Raptors
64	22.97	15.46	4.29	0.86	1.16	2.55	2.69	56.40
BOS
Boston Celtics
63	22.91	13.41	4.31	1.09	1.09	1.54	2.51	50.85
MIL
Milwaukee Bucks
65	22.84	14.64	4.81	1.19	1.14	1.71	2.48	53.69
HOU
Houston Rockets
64	22.75	14.47	4.22	1.20	1.25	2.69	3.47	54.79
OKC
Oklahoma City Thunder
64	22.70	16.20	4.83	0.87	1.11	2.21	3.27	56.08
MEM
Memphis Grizzlies
65	22.60	15.18	3.94	0.92	1.32	3.25	3.12	57.32
NOR
New Orleans Pelicans
64	22.57	14.95	4.61	0.98	1.24	2.47	2.96	55.60
IND
Indiana Pacers
65	22.52	14.29	4.73	0.69	1.20	2.40	3.21	54.35
ATL
Atlanta Hawks
64	22.48	15.48	3.93	0.75	1.62	2.50	2.76	56.55
BKN
Brooklyn Nets
65	22.20	14.46	4.01	0.93	1.31	2.32	2.16	54.30
CHI
Chicago Bulls
64	22.10	14.21	4.58	1.18	1.23	2.16	2.30	53.89
MIN
Minnesota Timberwolves
65	21.51	13.24	4.15	1.14	1.43	2.05	2.56	51.50
LAL
Los Angeles Lakers
66	21.48	15.04	4.58	1.27	1.54	2.14	2.89	54.55
PHO
Phoenix Suns
64	21.42	13.30	4.66	0.81	1.29	1.67	2.86	50.39
CLE
Cleveland Cavaliers
64	20.89	15.12	3.76	1.03	1.26	2.43	2.78	52.96
ORL
Orlando Magic
65	20.83	13.68	3.60	0.62	1.55	2.24	3.03	50.99
LAC
Los Angeles Clippers
63	20.51	14.57	4.65	0.97	1.48	1.70	2.52	51.99
SAC
Sacramento Kings
63	20.35	14.48	4.60	0.67	1.32	1.96	2.23	52.24
MIA
Miami Heat
64	19.96	14.37	3.19	0.98	1.10	1.87	2.20	48.70
NYK
New York Knicks
64	19.71	13.12	3.25	1.12	1.19	2.17	2.59	47.82"""

team_points_allowed = {}
lines = data.strip().split('\n')

for i in range(0, len(lines), 3):
    team_abbr = lines[i]
    points_allowed = float(lines[i + 2].split('\t')[1])
    team_points_allowed[team_abbr] = points_allowed
