/*
  Arduino LSM9DS1 - Simple Gyroscope

  This example reads the gyroscope values from the LSM9DS1
  sensor and continuously prints them to the Serial Monitor
  or Serial Plotter.

  The circuit:
  - Arduino Nano 33 BLE Sense

  created 10 Jul 2019
  by Riccardo Rizzo

  This example code is in the public domain.
*/

#include <Arduino_LSM9DS1.h>
#include <model_gesture.tflite>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  Serial.print("Gyroscope sample rate = ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Gyroscope in degrees/second");
  Serial.println("X\tY\tZ");
}

void loop() {
    float x, y, z;

    if (IMU.gyroscopeAvailable()) {
        IMU.readGyroscope(x, y, z);
    }
    
    // x disponible
    // y disponible
    // z disponible
    
    modelo ya entrenado. (se entrena con es script de python)
    entran x,y,z
    ---------------------------------
    !                               !
    !                               !
    !      ML                       !
    !                               !
    !                               !    
    ---------------------------------
    salida: GESTURE (A | B | C)

    Serial.println("Movement detected: /n/t/t");
    Serial.println(GESTURE);
}
