from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/skill'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class Skill(db.Model):
    __tablename__ = 'skill'

    
    Skill_id = db.Column(db.Integer, primary_key=True)
    Skill_name = db.Column(db.String(64), nullable=False)
    Skill_desc = db.Column(db.String(255), nullable=False)
    Date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    



    def json(self):
        return {"skill_id": self.skill_id, "skill_name": self.skill_name, "skill_desc": self.skill_desc, "skill_status": self.skill_status}



#https://teamtreehouse.com/community/what-is-the-difference-between-json-and-jsonparse#:~:text=The%20difference%20is%3A,)%20JavaScript%20object(s).
@app.route("/skill")
def get_all():
    #list
    skilllist = skill.query.all()
    if len(skilllist):
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    
                    #turn python data into javascript object
                    "books": [skill.json() for skill in skilllist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no skills."
        }
    ), 404
    
    

@app.route("/addskill", methods=['GET','POST'])
def create_book():
    
    skill_name = "Finance"
    skill_desc = "pivot table"
    skill_status = "virtual"
    skill_type = "Sales"
    
    skill = Skill(skill_name = skill_name,skill_desc = skill_desc, skill_status = skill_status,skill_type = skill_type)
    
    try:
        db.session.add(skill)
        db.session.commit()
        
        return('skill added successfully')
        
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the skill."
            }
        ), 500


@app.route("/deleteskill/<string:skill_name>", methods=['GET','DELETE'])
def delete_book(skill_name):
    
    skill = Skill.query.filter_by(skill_name=skill_name).first()
    if skill:
        db.session.delete(skill)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skill_name": skill_name + 'has been successfully deleted'
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                 "skill_name": skill_name
            },
            "message": "skill not found."
        }
    ), 404
    

@app.route("/updateskill/<string:skill_name>", methods=['GET','PUT'])
def update_book(skill_name):
    skill = skill.query.filter_by(skill_name=skill_name).first()
    if skill:
        skill.skill_name = 'Fintech'
        skill.skill_desc = 'Finance analytics'
        skill.skill_status = 'F2F'
        skill.skill_type = skill.skill_type
        #data = request.get_json()
        #if data['skill_name'] != "":
        #    skill.skill_name = data['skill_name']
        #if data['skill_desc'] != "":
        #    skill.skill_desc = data['skill_desc']
        #if data['skill_status'] != "":
        #    skill.skill_status = data['skill_status']
        #if data['skill_type'] != "":
        #   skill.skill_type = data['skill_type']
           
        db.session.commit()
        
        return jsonify(
            {
                "code": 200,
                "data": "skill has been added successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "isbn13": skill
            },
            "message": "skill not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
