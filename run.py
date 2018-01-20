#! /usr/bin/env python3
# coding: utf-8

""" Run Flask application """

from gpbapp import APP


if __name__ == "__main__":
    APP.run(debug=True)
