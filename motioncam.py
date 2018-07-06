import picamera
import os
import sys
import time
from gpiozero import MotionSensor

imgDir = "/mnt/security/motioncam0"

with picamera.PiCamera() as camera:

    def initCamera(camera):
        #camera settings
        #camera.resolution            = (SCREEN_WIDTH, SCREEN_HEIGHT)
        camera.framerate             = 24
        camera.sharpness             = 0
        camera.contrast              = 0
        camera.brightness            = 50
        camera.saturation            = 0
        camera.ISO                   = 0
        camera.video_stabilization   = False
        camera.exposure_compensation = 0
        camera.exposure_mode         = 'auto'
        camera.meter_mode            = 'average'
        camera.awb_mode              = 'auto'
        camera.image_effect          = 'none'
        camera.color_effects         = None
        camera.rotation              = 270
        camera.hflip                 = False
        camera.vflip                 = True
        camera.crop                  = (0.0, 0.0, 1.0, 1.0)

    def captureImage(camera,imageName):
        camera.capture(imgDir+"/"+imageName)

    def motion_start():
        print("Motion detected!")
        fileName = time.strftime("%Y%m%d-%H%M%S")+".png"
        captureImage(camera,fileName)

    def motion_stop():
        print("motion stopped")

    def monitor():
        try:
            initCamera(camera)
            pir = MotionSensor(21)
            pir.when_motion = motion_start
            pir.when_no_motion = motion_stop

            while True:
                pir.wait_for_motion()
        except BaseException:
            print("ERROR: unhandled exception")
        finally:
            camera.close()

    monitor()
    exit()