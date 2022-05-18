from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_o_four(error):
    '''Function to render the 404 page'''
    return  render_template('fourofour.html')
