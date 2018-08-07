from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	likes_beer_pong=False
	senders=["mtvjesse","kyle","905 shooter","holden cuming"]
	return render_template(
		"index.html",
		senders=senders,
		likes_beer_pong = likes_beer_pong
		)


    

if __name__ == '__main__':
   app.run(debug = True)