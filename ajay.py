from flask import Flask, request, render_template
from .plant_model import PlantModel

def all():
	app = Flask(__name__, static_url_path='/static')
	app.config['UPLOAD_FOLDER']='static/images'
	app.config['SECRET_KEY']='ajaysain'

	@app.route('/', methods=['POST', 'GET'])
	def img():
		result = ''
		if request.method=='POST':
			img = request.files['plant'].read()
			model_object = PlantModel()
			print('model created....')
			result = model_object.result(img)
			print(result)

			return render_template('home.html', result=result)
		return render_template('home.html', result=result)
	return app


