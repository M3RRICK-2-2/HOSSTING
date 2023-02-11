from flask import Flask, render_template, request
init = Flask(__name__)
#initialize flask

#route your webpage
@init.route('/')

def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()
	return render_template('index.html',count=visitors_count)

# Render HTML with count variable

#route your webpage
@init.route('/',methods = ['POST'])

def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()
	test = request.form['text']
	api = 'https://covidstats-sdbd.onrender.com/?country='+test
	print(api)
	return render_template('index.html',emag = api, count = visitors_count)

	#complete the code

#add code for executing flask
if __name__ == "__main__":
	init.run()