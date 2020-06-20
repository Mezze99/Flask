
import flask_sqlalchemy
from .models import Team, Player, Coach, Title, Sponsoring, Membership, Table

db = flask_sqlalchemy.SQLAlchemy()

teams = [Team(team_name="FC Barcelona", city="Barcelona"),
        Team(team_name="Real Madrid", city="Madrid"),
        Team(team_name="Bayern Munich", city="Munich"),
        Team(team_name="Manchester City", city="Manchester"),
        Team(team_name="AC Milano", city="Milano"),
        Team(team_name="Eintracht Frankfurt", city="Frankfurt")]

players = [Player(fname='Lionel', lname='Messi', pl_no=10, nationality="Argentina", pl_goals=16, team_id=1),
        Player(fname='Samuel', lname='Umtiti', pl_no=23, nationality="France", pl_goals=1, team_id=1),
        Player(fname='Sergio', lname='Busquets', pl_no=5, nationality="Spain", pl_goals=4, team_id=1),
        Player(fname='Arturo', lname='Vidal', pl_no=22, nationality="Chile", pl_goals=2, team_id=1),
        Player(fname='Antoine', lname='Griezmann', pl_no=17, nationality="France", pl_goals=9, team_id=1),
        Player(fname='Christiano', lname='Ronaldo', pl_no=7, nationality="Portugal", pl_goals=17, team_id=2),
        Player(fname='Gareth', lname='Bale', pl_no=11, nationality="Wales", pl_goals=7, team_id=2),
        Player(fname='Karim', lname='Benzema', pl_no=9, nationality="France", pl_goals=13, team_id=2),
        Player(fname='Toni', lname='Kroos', pl_no=8, nationality="German", pl_goals=1, team_id=2),
        Player(fname='James', lname='Rodríguez', pl_no=16, nationality="Columbia", pl_goals=4, team_id=2),
        Player(fname='Thomas', lname='Müller', pl_no=13, nationality="Germany", pl_goals=13, team_id=3),
        Player(fname='Jerome', lname='Boateng', pl_no=17, nationality="Germany", pl_goals=2, team_id=3),
        Player(fname='Manuel', lname='Neuer', pl_no=1, nationality="Germany", pl_goals=0, team_id=3),
        Player(fname='David', lname='Alaba', pl_no=27, nationality="Austria", pl_goals=4, team_id=3),
        Player(fname='Joshua', lname='Kimmich', pl_no=32, nationality="German", pl_goals=0, team_id=3),
        Player(fname='Robert', lname='Lewandowski', pl_no=9, nationality="Poland", pl_goals=22, team_id=3),
        Player(fname='Kevin', lname='De Bruyne', pl_no=10, nationality="Belgium", pl_goals=11, team_id=4),
        Player(fname='Leroy', lname='Sané', pl_no=19, nationality="German", pl_goals=6, team_id=4),
        Player(fname='Gabriel', lname='Jesus', pl_no=9, nationality="Brasilia", pl_goals=7, team_id=4),
        Player(fname='Sergio', lname='Agüero', pl_no=10, nationality="Argentina", pl_goals=15, team_id=4),
        Player(fname='Joao', lname='Cancelo', pl_no=10, nationality="Portugal", pl_goals=1, team_id=4),
        Player(fname='Zlatan', lname='Ibrahimovic', pl_no=21, nationality="Sweden", pl_goals=99, team_id=5),
        Player(fname='Ante', lname='Rebic', pl_no=18, nationality="Croatia", pl_goals=10, team_id=5),
        Player(fname='Gianluigi', lname='Donnarumma', pl_no=99, nationality="Italia", pl_goals=0, team_id=5),
        Player(fname='Simon', lname='Kjaer', pl_no=24, nationality="Denmark", pl_goals=0, team_id=5),
        Player(fname='Giacomo', lname='Bonaventura', pl_no=5, nationality="Italia", pl_goals=3, team_id=5),
        Player(fname='Martin', lname='Hinteregger', pl_no=13, nationality="Austria", pl_goals=3, team_id=6),
        Player(fname='André', lname='Silva', pl_no=33, nationality="Portugal", pl_goals=8, team_id=6),
        Player(fname='Sebastian', lname='Rode', pl_no=17, nationality="German", pl_goals=0, team_id=6),
        Player(fname='Kevin', lname='Trapp', pl_no=1, nationality="German", pl_goals=0, team_id=6)]

coaches = [Coach(first_name="Quique", last_name="Setién", nationality="Spain", id=1),
        Coach(first_name="Zinedine", last_name="Zidane", nationality="France", id=2),
        Coach(first_name="Hansi", last_name="Flick", nationality="German", id=3),
        Coach(first_name="Pep", last_name="Guardiola", nationality="Spain", id=4),
        Coach(first_name="Stefano", last_name="Pioli", nationality="Italia", id=5),
        Coach(first_name="Adi", last_name="Hütter", nationality="Austria", id=6)]

titles = [Title(year= "2013", winning_team="Bayern Munich"),
       Title(year= "2014", winning_team="Real Madrid"),
       Title(year= "2015", winning_team="FC Barcelona"),
       Title(year= "2016", winning_team="Real Madrid"),
       Title(year= "2017", winning_team="Real Madrid"),
       Title(year= "2018", winning_team="Real Madrid"),
       Title(year= "2019", winning_team="Eintracht Frankfurt"),
       Title(year= "2020", winning_team="AC Milano")]

sponsorings = [Sponsoring(start_date="20-06-2016", sponsor_name="Rakuten", team_id=1, contract=80),
            Sponsoring(start_date="04-07-2017", sponsor_name="Fly Emirates", team_id=2, contract=73),
            Sponsoring(start_date="02-06-2019", sponsor_name="Adidas", team_id=3, contract=69),
            Sponsoring(start_date="10-07-2009", sponsor_name="Etihad Airways", team_id=4, contract=65),
            Sponsoring(start_date="09-10-2015", sponsor_name="Fly Emirates", team_id=5, contract=40),
            Sponsoring(start_date="01-04-2020", sponsor_name="Deutsche Bank", team_id=6, contract=38)]

memberships = [Membership(number_members=144500, id=1),
            Membership(number_members=93200, id=2),
            Membership(number_members=293000, id=3),
            Membership(number_members=30000, id=4),
            Membership(number_members=20000, id=5),
            Membership(number_members=90000, id=6)]

tables = [Table(matches=10, wins=8, remis=1, defeats=1, points=25, id=1),
       Table(matches=10, wins=8, remis=0, defeats=2, points=24, id=2),
       Table(matches=10, wins=6, remis=1, defeats=3, points=19, id=3),
       Table(matches=10, wins=3, remis=2, defeats=5, points=11, id=4),
       Table(matches=10, wins=0, remis=4, defeats=6, points=4, id=5),
       Table(matches=10, wins=0, remis=2, defeats=8, points=2, id=6)]

def run_insert(teams=teams, players=players, coaches=coaches, titles=titles, sponsorings=sponsorings, memberships=memberships, tables=tables):
    for team in teams:
        db.session.add(team)
        db.session.commit()
    
    for player in players:
        db.session.add(player)
        db.session.commit()
    
    for coach in coaches:
        db.session.add(coach)
        db.session.commit()

    for title in titles:
        db.session.add(title)
        db.session.commit()
    
    for sponsoring in sponsorings:
        db.session.add(sponsoring)
        db.session.commit()

    for membership in memberships:
        db.session.add(membership)
        db.session.commit()

    for table in tables:
        db.session.add(table)
        db.session.commit()