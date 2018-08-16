from flask import Flask, render_template
app = Flask(__name__)

#Without render_template
@app.route('/BMI/<int:weight>/<int:height>')
def BMI(weight, height):
    height_in_meter = height/100
    BMI = weight / (height_in_meter ** 2)
    if BMI < 16:
        condition = "Severely underweight"
    elif BMI < 18.5:
        condition = "Underweight"
    elif BMI < 25:
        condition = "Normal"
    elif BMI < 30:
        condition = "Overweight"
    else:
        condition = "Severely overweight"
    return("Your BMI is {:.2f}. You are {}".format(BMI, condition))

#With render_template
@app.route('/BMI_/<int:weight>/<int:height>')
def BMI_with_render_template(weight, height):
    
    height_in_meter = height/100
    BMI = round(weight / (height_in_meter ** 2), 2)

    return render_template('BMI.html', BMI = BMI)

if __name__ == '__main__':
  app.run(debug=True)
 