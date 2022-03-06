import sys
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Query, sessionmaker

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)
    # degree = Column(Integer, default=30)
    # state = Column(String(20), default='Sunny')

app = Flask(__name__)
engine = create_engine("sqlite:///weather.db", echo=True,
    connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

query = Query(City, session)

@app.route('/')
def index():
    all_rows = query.all()
    for row in all_rows:
        print(f"City id: {row.id}, name: {row.name}")
    return render_template('index.html', all_rows=all_rows)

# Boston, 9, Chilly
# New York, 32, Sunny
# Edmonton, -15, Cold
@app.route('/add', methods=['POST'])
def add_city():
    city_name = request.form['city_name']
    # new_info = City(name=city_name, state="Sunny", degree=10)
    new_info = City(name=city_name)
    session.add(new_info)
    session.commit()
    return redirect(url_for('index'))

# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run(debug=True)
