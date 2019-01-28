import sqlite3
conn = sqlite3.connect('health_dashboards.db')
c = conn.cursor()


# partner device count table
c.execute('''
CREATE TABLE partner_device_count (
 name TEXT NOT NULL,
 count INTEGER
);
''')

rows = [('2nd Watch', 115721),
        ('Epsilon', 115590),
        ('CDI', 95051),
        ('Wolters Kluwer', 93912),
        ('GE Software', 87811),
        ('BlazeClan', 21743),
        ('Carousel Industries', 20568),
        ('GreenPages', 14959),
        ('KAR Auction Services Inc', 13449),
        ('Pivot Technology Solutions', 11067)]

c.executemany('insert into partner_device_count values (?,?)', rows)
conn.commit()


# number of devices in each client
c.execute('''
CREATE TABLE devices_in_client (
 partner TEXT NOT NULL,
 client TEXT NOT NULL,
 count INTEGER
);
''')

rows = [('GE Software', 'PCE-CAP', 86573),
        ('CDI', 'Thomas Publishing Company', 72717),
        ('Wolters Kluwer', 'WoltersKluwer', 48056),
        ('2nd Watch', 'Sysco', 32708),
        ('2nd Watch', 'McDonald''s', 20463),
        ('Epsilon', 'STSX (STS)', 16564),
        ('2nd Watch', 'TCCC KO Consumer (RA)', 13880),
        ('Wolters Kluwer', 'GPO-CSS/PT/CT/ISAT', 12546),
        ('KAR Auction Services Inc', 'ITSS', 12080),
        ('Epsilon', 'DDML (Dream Mail)', 11724)]

c.executemany('insert into devices_in_client values (?,?,?)', rows)
conn.commit()

# alerts count
c.execute('''
CREATE TABLE alerts_count (
 client TEXT NOT NULL,
 alert_count INTEGER
);
''')

rows = [('KAR Auction Services Inc', 756354),
        ('Dell DCD', 544611),
        ('Viacom18-Voot', 478372),
        ('TheAA', 346309),
        ('Production', 290618),
        ('Test Environment', 269242),
        ('NIIT India', 261596),
        ('Howard County Community College HCCC', 223639),
        ('Novelis', 203515),
        ('Motorola', 189852)]

c.executemany('insert into alerts_count values (?,?)', rows)
conn.commit()

# tickets count
c.execute('''
CREATE TABLE tickets_count (
 partner TEXT NOT NULL,
 client TEXT NOT NULL,
 ticket_count INTEGER
);
''')

rows = [('NTL Shared Services', 'TheAA', 34177),
        ('BlazeClan', 'Bajaj (BFDL)', 6251),
        ('KAR Auction Services Inc', 'ITSS', 6221),
        ('NTT Legacy Infra', 'Novelis', 5361),
        ('NIIT-Tech', 'AgeUK', 3934),
        ('Ofcom', 'Ofcom', 3918),
        ('2nd Watch', 'McDonald''s', 3718),
        ('NTTDATA DCD', 'NDC', 3678),
        ('BlazeClan', 'Viacom18-Voot', 3575),
        ('NTT Legacy Infra', 'Jabil Circuit Inc', 3500)]

c.executemany('insert into tickets_count values (?,?,?)', rows)
conn.commit()

# New client addition
c.execute('''
CREATE TABLE new_client_addition (
 id INTEGER,
 name TEXT NOT NULL,
 service provider TEXT NOT NUll,
 partner TEXT NOT NULL,
 created by email TEXT NOT NULL
);
''')

rows = [('698594','NetEnrich Go','NetEnrich Inc','NetEnrich Corporate','shyam.rangaraju@netenrich.com'),
        ('698599','SailPoint Technologies Inc.','OpsRamp Inc','Critical Start','mike@criticalstart.com'),
        ('698604','Confidential Communications International','NetEnrich Inc','GB Tech','sandeep.khadke@netenrich.com')]
c.executemany('insert into new_client_addition values (?,?,?,?,?)', rows)
conn.commit()


c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())
