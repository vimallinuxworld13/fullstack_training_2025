from flask import Flask, request, render_template

app = Flask(__name__)

# DB - in-place memory
studentDB = {

		1: {
			"id": 1,
			"name": "vimal",
			"mobile": 9829111123,
			"courses": ["QC", "AI"]
		},

		2: {
			"id": 2,
			"name": "eric",
			"mobile": 9829122222,
			"courses": ["AI"]
		},
 
		3: {
			"id": 3,
			"name": "tom",
			"mobile": 9829133333,
			"courses": ["Full Stack"]

		}



}

@app.route("/", methods=['GET'])
def lwhome():
	return  render_template("myhome.html")

@app.route("/students", methods=['GET'])
def lwstudentsinfo():
	return render_template("students_entire_info.html" , db=studentDB)

@app.route("/student/<index>", methods=['GET'])
def lwstudentinfo(index):
	if int(index) <= 0:
		return "Not exists"
	elif int(index) in studentDB:
		# return studentDB[int(index)]
		return render_template(
					"studentinfo.html", 
					stName=studentDB[int(index)]['name'], 
					stMob=studentDB[int(index)]['mobile'],
					stCourses=studentDB[int(index)]['courses'],
					stID=studentDB[int(index)]['id'],

				)
	else:
		return "Not exists"

@app.route("/student/create", methods=["POST"])
def lwstudentcreate():

	# print ( request.files )


	fh = request.files['myfile']

	if fh.mimetype == "image/jpeg":
		fh.save(f"templates/{fh.filename}")
	else:
		print("file type not supported ")
	

	# print ( dir(fh) )
	# print (fh.content_length,	fh.filename,	fh.mimetype,	fh.name )
	# print(fh)
	

	# print("method : " , request.method)
	# print("data : " , request.json)

	#print("JSON : " , request.json)
	#print("FORM : " , request.form)

	if request.form:
		result = request.form
		name = result['name']
		mob = result['mobile']
		courses = result['courses']
		# print ( result['myfile'] )
		
		nextId = list ( studentDB.keys() )[-1] + 1

		studentDB[ nextId ] = {
			"id": nextId,
			"name": name,
			"mobile": mobile,
			"courses": [courses]

		}

	
		print(result)

	elif request.json:
		studentDB[ list ( studentDB.keys() )[-1] + 1 ] =  request.json

	else:
		print("not supported")

	return "record created .."

@app.route("/student/delete/<index>", methods=["DELETE"] )
def lwstudentdelete(index):
	del studentDB[int(index)]
	return "record deleted .."


@app.route("/student/update/<item>/<index>", methods=["PATCH"])
def lwstudentpatch(item, index):
	data=request.json
	if item in data:
		print(data[item])
		studentDB[int(index)][item] = data[item]
		return f"mobile record patched .. {index}"
	else:
		return("key is not exists.. to patch")


@app.route("/student/updates/<index>" , methods=["PUT"])
def lwstudentput(index):
	data = request.json
	
	if int(index) in studentDB:
		studentDB[int(index)] = data
		return "entire record updated ..."
	else:
		return f"{index} id not exists.."



app.run()
