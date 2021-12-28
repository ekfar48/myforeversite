from flask import Flask, request, send_file
import os
app = Flask(__name__)

site_home = """
<html>
    <head>
        <title>This site from LEIZD</title>
    </head>
    <body>
	<div id = "wrap">
		<header>
			<div class = "title">LEIZD</div>
		</header>
	</div>
	<style>
	body{
		background-image:  url("https://static.themoscowtimes.com/image/1360/55/595155.jpg")
	}	
	header{
		width: 100%;
		background: #000000;
		height: 90px;
		position: absolute;
		top: 0px;
		right: 0px ;
	}
	.title{
		font-size: 36px;
		padding-top: 10px;
		color: #ffffff;
		position: absolute;
		top: 8px;
		left: 70px ;
	}
	</style>
    </body>
</html>
"""

@app.route("/")
def home_view():
    return site_home

@app.route(f'/d/<string:file_ekfara>')
def download(file_ekfara):
    return send_file(f'//yy//'+file_ekfara)
    

if __name__ == "__main__":
        app.run()
