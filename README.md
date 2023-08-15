# pydeepzoom

An API for generating deepzoom tile pyramids from images given via URL. The API is a python implementation of the DeepZoomService from the HBZ (https://github.com/hbz/DeepZoomService)

## Installation

### Requirements

  - python3.8 +
  - libvips

#### 1. Create Virtual Environment

    python3 -m venv ./pydeepzoom

#### 2. Download pydeepzoom

    cd pydeepzoom
    git clone https://github.com/bjquast/pydeepzoom.git

#### 3. Setup

    cd pydeepzoom
    source ../bin/activate
    python setup.py develop
  
#### 4. Configuration

Edit ./pydeepzoom/config.ini to match your requirements:

    [tiles_cache]
    dir = ./tilescache
    tempdir = ./temp
    
    [allowed_domains]
    # a whitelist will exclude all domains not contained in it. If no whitelist is given, all domains exept for the blacklisted are allowed
    whitelist = example.com, www.example.com 
    # a blacklist will exclude all domains contained in it, even if they have been added to the whitelist
    blacklist = baddomain.org, anotherbaddomain.com 
    
    [images]
    known_formats = png, jpg, jpeg, tiff, tif, pnm, pgm, pbm
    
    
    [ssl_requests]
    sslverify = True
    
    [request_headers]
    user-agent = pydeepzoom

#### 5 Create the directories

Create the for temp files and the tilescache as set in config.ini. When using relative paths, the directories are relative to the dir where **production.ini** is in. For example:

config.ini contains:

    [tiles_cache]
    dir = ./tilescache
    tempdir = ./temp
    
go back to the second pydeepzom directory:

    cd ..

add both directories:

    mkdir ./tilescache
    mkdir ./temp

#### 6 Configure webserver

By default **production.ini** defines a subpath to your domain (**url_prefix**) and the https protocol (**url_scheme**):

    [server:main]
    use = egg:waitress#main
    port = 6550
    url_scheme = https
    url_prefix = /pydeepzoom

To use the API in production you can set up a proxy in your webserver that redirects from https://yourdomain/pydeepzoom to http://localhost:6550/pydeepzoom. Here is an example for Apache:

    #Proxy for pydeepzoom:
    ProxyPass /pydeepzoom http://localhost:6550/pydeepzoom connectiontimeout=5 timeout=300
    ProxyPassReverse /pydeepzoom http://localhost:6550/pydeepzoom
    ProxyPreserveHost On
    ProxyRequests Off

The configuration in **development.ini** allows you to use the API with the url **http://localhost:6550** for testing and development

#### 7 Start the Webservice

The API is started with:

    pserve production.ini

or

    pserve development.ini

A request to the API like:

    https://localhost/pydeepzoom/deepzoom?imageUrl=https://physalia.evolution.uni-bonn.de/dumping/Images/Blankenberge_Havenplein.tiff

should return a json response like this:

    {"Format": "jpeg", "Overlap": "1", "TileSize": "254", "Size": {"Height": "3125", "Width": "12617"}, "Url": "https://localhost/pydeepzoom/tilesCache/physalia_evolution_uni_bonn_de_dumping_Images_Blankenberge_Havenplein_tiff_files/"}

## Usage

See https://github.com/hbz/DeepZoomService#usage
    
