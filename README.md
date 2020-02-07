# RasPi-TemperatureSensorScript
Python script to get air condition(temperature, humidity) using Raspberry pi 3 and HTU21D-F

## Requirement

- [Raspberry Pi3 Model B](https://www.amazon.co.jp/gp/product/B01CHJRAMM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
    - Raspbian GNU/Linux 9.11 (stretch)

- [HTU21D-F](https://www.switch-science.com/catalog/1799/)

## Install

Enable I2C in Raspi3, install i2c python library.

    sudo raspi-config
 -> Interfacing Options -> I2C -> enable

    sudo apt-get -y install python-smbus i2c-tools


##  Pin connections

|Raspi 3  |HTU21D-F  |Note  |
|---|---|---|
|3V3  |3V3  ||
|GND  |GND  ||
|GPIO2(PinNo.3)  |SDA  |pull-up in HTU21D-F|
|GPIO3(PinNo.5)  |SCL  |pull-up in HTU21D-F|

## Usage 

    $ python3 HTU21D.py
    Temperature   : 18.28
    Humidity   : 44.87

