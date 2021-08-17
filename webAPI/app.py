from flask import Flask, jsonify, request, render_template
#from flask_cors import CORS
import buildJson


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
#CORS(app) # This will enable CORS for all routes


@app.route('/', methods=['GET'] )
def init():
    
    return render_template('base.html')


#@app.route('/test/<string:sname>', methods=['GET'])
#def newJson(sname):
#    return render_template('inWork.html')


@app.route('/test/<string:sname>', methods=['GET'])
def newJson(sname):
    list = buildJson.readsheet("Strukturtabelle_InKalkTierchenhaltung.xlsx", sname)
    print(type(list))
    print(type(jsonify(list)))

    return jsonify(list)


if __name__ == '__main__':
    # Linux und Docker
    app.run(host='0.0.0.0')
    #app.run(port=4000, debug=True)



