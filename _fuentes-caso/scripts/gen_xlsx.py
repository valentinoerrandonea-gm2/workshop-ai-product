#!/usr/bin/env python3
"""Genera catalogo-productos.xlsx con el desorden del canon, tal cual."""
from pathlib import Path

from openpyxl import Workbook

OUT = Path(__file__).resolve().parents[2] / "caso-makerlab" / "material-cliente" / "catalogo-productos.xlsx"

# (SKU, Producto, Categoria, Precio, Stock) — el desorden es A PROPÓSITO (ver canon.md)
PRODUCTOS = [
    ("ARD-UNO-R3", "Arduino UNO R3", "Placas Arduino", 28500, 42),
    ("ARD-NANO", "Arduino Nano", "placas arduino", "$24.900", 18),
    ("ARD-MEGA", "Arduino Mega 2560", "Placas", 52300, 7),
    ("ESP-NODEMCU", "NodeMCU ESP8266", "Placas Arduino", 19800, 25),
    ("RPI-4B-4GB", "Raspberry Pi 4B 4GB", "Placas Raspberry Pi", 145000, 3),
    ("RPI-ZERO-W", "Raspberry Pi Zero W", "RASPBERRY", "$38.000", 0),
    ("SEN-DHT22", "Sensor temperatura y humedad DHT22", "Sensores", 8900, 31),
    ("SEN-HCSR04", "Sensor ultrasónico HC-SR04", "sensores", 4200, 55),
    ("SEN-PIR", "Sensor de movimiento PIR HC-SR501", "SENSORES Y MODULOS", 5100, 12),
    ("SEN-LDR", "Fotorresistencia LDR 5mm", "Sensores", 800, None),
    ("LCD-1602-I2C", "Display LCD 16x2 con I2C", "Modulos", 9700, 22),
    ("DRV-L298N", "Driver de motores L298N", "Modulos y comunicacion", 6800, 19),
    ("MOT-TT-DC", "Motor DC TT con reductora", "Actuadores", 3500, 40),
    ("MOT-SG90", "Servo SG90 9g", "Actuadores y motores", 4900, 28),
    ("CHS-2WD", "Chasis robot 2WD con ruedas", "Actuadores", 16500, 9),
    ("PRT-830", "Protoboard 830 puntos", "Accesorios", 6200, 60),
    ("JMP-MM-40", "Jumpers macho-macho x40", "Accesorios", 3800, 75),
    ("JMP-MH-40", "Jumpers macho-hembra x40", "accesorios", 3800, 68),
    ("LED-5MM-X10", "Pack 10 LEDs 5mm surtidos", "Accesorios", 2100, 90),
    ("RES-220-X25", "Pack 25 resistencias 220 ohm", "Accesorios", 1500, None),
    ("BTN-12MM", "Pulsador táctil 12mm", "Accesorios", 600, 120),
    ("BAT-4AA", "Portapilas 4xAA con cable", "Accesorios", 2900, 35),
    ("PSU-5V-2A", "Fuente 5V 2A micro USB", "Accesorios", 7400, 14),
    ("ARD-UNO-R3", "ARDUINO UNO R3 ORIGINAL", "Placas Arduino", "$31.200", 6),
]

CURSOS = [
    ("Semáforo inteligente", "Inicial",
     "ARD-UNO-R3, PRT-830, LED-5MM-X10, RES-220-X25, BTN-12MM, JMP-MM-40", 89900),
    ("Estación meteorológica IoT", "Intermedio",
     "ESP-NODEMCU, SEN-DHT22, LCD-1602-I2C, PRT-830, JMP-MH-40, PSU-5V-2A", 149900),
    ("Robot evita-obstáculos", "Avanzado",
     "ARD-UNO-R3, CHS-2WD, MOT-TT-DC x2, DRV-L298N, SEN-HCSR04, BAT-4AA, JMP-MH-40", 189900),
]


def main() -> None:
    wb = Workbook()

    ws = wb.active
    ws.title = "productos"
    ws.append(["SKU", "Producto", "Categoria", "Precio", "Stock"])
    for fila in PRODUCTOS:
        ws.append(list(fila))

    ws2 = wb.create_sheet("cursos")
    ws2.append(["Curso", "Nivel", "SKUs del kit", "Precio final"])
    for fila in CURSOS:
        ws2.append(list(fila))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"OK → {OUT}")


if __name__ == "__main__":
    main()
